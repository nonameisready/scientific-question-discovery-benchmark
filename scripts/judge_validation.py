#!/usr/bin/env python3
"""Judge reliability validation (Paper 2, judge-validation section).

Four experiments answering "why should anyone trust an LLM judge?":

  E1 mismatch    Pair each question with ANOTHER question's retrieved
                 evidence. A judge with discriminative power must collapse
                 to not_addressed; one that tracks mere topical similarity
                 will not. This bounds how much of the reported engagement
                 is real.
  E2 multimodel  Re-judge the sample with two further model families and
                 report pairwise Cohen's kappa, Fleiss' kappa, and —
                 the number that actually matters — whether the paper's
                 conclusions still hold under each judge.
  E3 selfconsist Re-run the same model twice more: temperature 0 is not
                 determinism, and every rate carries that noise.
  E4 prompt      Two semantically equivalent rewrites of the judge prompt,
                 including one where the label names are replaced by
                 neutral codes (L1-L4 / P1-P5), so a judge that keys off
                 the emotive value of "answered" is exposed.

    python scripts/judge_validation.py sample     # build the frozen sample
    python scripts/judge_validation.py e1 ... e4  # run (resumable)
    python scripts/judge_validation.py report

Requires OPENAI_API_KEY. Every stage skips existing output files.
"""

import argparse
import json
import random
import sys
from itertools import combinations
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark.judging import JUDGE_PROMPT, judge_all  # noqa: E402
from benchmark.schemas import load_jsonl, write_jsonl  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "judge_validation"
CORPUS = ROOT / "data" / "corpus" / "future_corpus_large_frozen_window.jsonl"

# (system label, questions file, retrieval file, annotations file)
SYSTEMS = [
    ("evidence_graph", "data/questions/astronomy_questions_v1.jsonl",
     "data/retrieval/evidence_graph_10_L_top8.jsonl",
     "data/annotations/outcomes_evidence_graph_10_L.jsonl"),
    ("direct_llm", "submissions/direct_llm_L1/questions.jsonl",
     "data/retrieval/direct_llm_L_top8.jsonl",
     "data/annotations/outcomes_direct_llm_L.jsonl"),
    ("citation_leader", "submissions/citation_leader_L1/questions.jsonl",
     "data/retrieval/citation_leader_L_top8.jsonl",
     "data/annotations/outcomes_citation_leader_L.jsonl"),
    ("random_claim", "submissions/random_claim_L1/questions.jsonl",
     "data/retrieval/random_claim_L_top8.jsonl",
     "data/annotations/outcomes_random_claim_L.jsonl"),
    ("tension_llm", "submissions/tension_llm_L1/questions.jsonl",
     "data/retrieval/tension_llm_L_top8.jsonl",
     "data/annotations/outcomes_tension_llm_L.jsonl"),
    ("tension_template", "submissions/tension_template_L1/questions.jsonl",
     "data/retrieval/tension_template_L_top8.jsonl",
     "data/annotations/outcomes_tension_template_L.jsonl"),
]
OUTCOMES = ["answered", "partially_addressed", "posed_but_open", "not_addressed"]
PER_SYSTEM = 16          # stratified: 4 per outcome label where available
ALT_MODELS = ["gpt-4o", "gpt-4-turbo"]
SEED = 20260812

# --- E4 prompt variants -----------------------------------------------------

PROMPT_REWORDED = """\
Your task: decide how the scientific literature published AFTER a cutoff date
responded to a research question that was written BEFORE that date, using only
the candidate abstracts supplied.

Give two separate labels.

First label, outcome — the fate of the question itself:
  answered              later work substantially settled it
  partially_addressed   clear directly relevant progress, core issue unsettled
  posed_but_open        later work raises the same question without settling it
  not_addressed         no candidate abstract engages it substantively

Second label, premise_status — the fate of the assumption the question rests on:
  supported        later evidence upholds the premise
  refuted          later evidence falsifies it
  weakened         later evidence seriously undermines it without falsifying
  still_plausible  the premise went untested
  not_applicable   there is no contestable premise

Constraints: cite only bibcodes present among the candidates; shared subject
matter alone is not engagement — the abstract must speak to the question's
actual test or premise; a question settled BY overturning its premise takes
outcome=answered with premise_status=refuted.

Reply in JSON with keys: outcome, premise_status, evidence (list of
{bibcode, relevance}, at most 5, possibly empty), rationale (two sentences).
"""

PROMPT_NEUTRAL = """\
You classify how a body of later literature relates to an earlier research
question, using only the candidate abstracts supplied. Assign two codes.

Code A (question status):
  L1  the later literature substantially resolved the question
  L2  substantial directly-relevant progress; the core question stays open
  L3  the later literature independently raises the same question, unresolved
  L4  no candidate abstract engages the question substantively

Code B (status of the assumption the question presupposes):
  P1  later evidence confirms the assumption
  P2  later evidence falsifies the assumption
  P3  later evidence substantially undermines it without falsifying it
  P4  the assumption was never directly tested
  P5  the question presupposes nothing contestable

Rules: cite only bibcodes from the candidates; topical overlap alone does not
count as engagement; if the question is resolved by overturning its
assumption, use L1 with P2.

Return JSON: {"outcome": "L1"|"L2"|"L3"|"L4",
"premise_status": "P1"|"P2"|"P3"|"P4"|"P5",
"evidence": [{"bibcode": str, "relevance": str}], "rationale": str}
"""
CODE_MAP = {"L1": "answered", "L2": "partially_addressed",
            "L3": "posed_but_open", "L4": "not_addressed",
            "P1": "supported", "P2": "refuted", "P3": "weakened",
            "P4": "still_plausible", "P5": "not_applicable"}

# --- agreement statistics ---------------------------------------------------


def cohen_kappa(a: list[str], b: list[str]) -> float:
    labels = sorted(set(a) | set(b))
    n = len(a)
    if n == 0:
        return float("nan")
    observed = sum(1 for x, y in zip(a, b) if x == y) / n
    expected = sum((a.count(v) / n) * (b.count(v) / n) for v in labels)
    return round((observed - expected) / (1 - expected), 4) if expected < 1 else 1.0


def fleiss_kappa(rater_columns: list[list[str]]) -> float:
    """rater_columns: one list of labels per rater, all same length/order."""
    n_items, n_raters = len(rater_columns[0]), len(rater_columns)
    labels = sorted({v for col in rater_columns for v in col})
    counts = [[sum(1 for col in rater_columns if col[i] == v) for v in labels]
              for i in range(n_items)]
    p_i = [(sum(c * c for c in row) - n_raters) / (n_raters * (n_raters - 1))
           for row in counts]
    p_bar = sum(p_i) / n_items
    p_j = [sum(row[j] for row in counts) / (n_items * n_raters)
           for j in range(len(labels))]
    p_e = sum(p * p for p in p_j)
    return round((p_bar - p_e) / (1 - p_e), 4) if p_e < 1 else 1.0


def percent_agreement(a: list[str], b: list[str]) -> float:
    return round(sum(1 for x, y in zip(a, b) if x == y) / len(a), 4) if a else 0.0

# --- sampling ---------------------------------------------------------------


def build_sample() -> dict:
    """Frozen stratified sample: PER_SYSTEM questions per system, spread
    across the outcome labels the default judge assigned."""
    rng = random.Random(SEED)
    sample = {}
    for name, qfile, rfile, afile in SYSTEMS:
        outs = {o["question_id"]: o for o in load_jsonl(ROOT / afile)}
        by_label = {label: sorted(q for q, o in outs.items()
                                  if o["outcome"] == label) for label in OUTCOMES}
        picked: list[str] = []
        per_label = max(1, PER_SYSTEM // len(OUTCOMES))
        for label in OUTCOMES:
            pool = by_label[label]
            picked += rng.sample(pool, min(per_label, len(pool)))
        remaining = sorted(set(outs) - set(picked))
        while len(picked) < min(PER_SYSTEM, len(outs)) and remaining:
            picked.append(remaining.pop(rng.randrange(len(remaining))))
        sample[name] = {"questions_file": qfile, "retrieval_file": rfile,
                        "annotations_file": afile, "question_ids": sorted(picked)}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "sample.json").write_text(json.dumps(sample, indent=2), encoding="utf-8")
    total = sum(len(v["question_ids"]) for v in sample.values())
    print(f"OK: frozen validation sample of {total} questions -> {OUT/'sample.json'}")
    return sample


def load_sample() -> dict:
    return json.loads((OUT / "sample.json").read_text(encoding="utf-8"))

# --- experiments ------------------------------------------------------------


def run_e1() -> None:
    """Mismatched-evidence control."""
    sample = load_sample()
    for name, spec in sample.items():
        out_file = OUT / f"e1_{name}.jsonl"
        if out_file.exists():
            continue
        records = load_jsonl(ROOT / spec["retrieval_file"])
        ids = spec["question_ids"]
        subset = [r for r in records if r["question_id"] in ids]
        # rotate documents by half the subset length: every question gets
        # another question's evidence, deterministically.
        shift = max(1, len(subset) // 2)
        shuffled = []
        for i, r in enumerate(subset):
            donor = subset[(i + shift) % len(subset)]
            shuffled.append({**r, "documents": donor["documents"],
                             "donor_question_id": donor["question_id"]})
        tmp = OUT / f"e1_{name}_retrieval.jsonl"
        write_jsonl(tmp, shuffled)
        print(f"E1 {name}: judging {len(shuffled)} mismatched pairs")
        judge_all(ROOT / spec["questions_file"], tmp, CORPUS, out_file,
                  prompt_id="mismatch_control")


CONCLUSION_SYSTEMS = ["direct_llm", "random_claim", "tension_llm", "tension_template"]
CONCLUSION_N = 40


def build_conclusion_sample() -> dict:
    """Unstratified random sample for conclusion robustness.

    The main validation sample is stratified by outcome label *within each
    system*, which equalises every system's label mix and therefore destroys
    exactly the between-system rate differences the paper's conclusions are
    about. Conclusion robustness needs an unstratified draw."""
    rng = random.Random(SEED + 1)
    spec_by_name = {n: (q, r, a) for n, q, r, a in SYSTEMS}
    sample = {}
    for name in CONCLUSION_SYSTEMS:
        qfile, rfile, afile = spec_by_name[name]
        ids = sorted(o["question_id"] for o in load_jsonl(ROOT / afile))
        sample[name] = {"questions_file": qfile, "retrieval_file": rfile,
                        "annotations_file": afile,
                        "question_ids": sorted(rng.sample(ids, min(CONCLUSION_N, len(ids))))}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "conclusion_sample.json").write_text(json.dumps(sample, indent=2),
                                                encoding="utf-8")
    print(f"OK: unstratified conclusion sample "
          f"({sum(len(v['question_ids']) for v in sample.values())} questions)")
    return sample


def run_e2c() -> None:
    """Cross-model judging on the unstratified conclusion sample."""
    path = OUT / "conclusion_sample.json"
    sample = (json.loads(path.read_text(encoding="utf-8")) if path.exists()
              else build_conclusion_sample())
    for model in ALT_MODELS:
        tag = model.replace(".", "").replace("-", "")
        for name, spec in sample.items():
            out_file = OUT / f"e2c_{tag}_{name}.jsonl"
            if out_file.exists():
                continue
            print(f"E2c {model} / {name}: {len(spec['question_ids'])} questions")
            judge_all(ROOT / spec["questions_file"], ROOT / spec["retrieval_file"],
                      CORPUS, out_file, model=model,
                      only_ids=set(spec["question_ids"]))


def run_e2() -> None:
    """Cross-model agreement."""
    sample = load_sample()
    for model in ALT_MODELS:
        tag = model.replace(".", "").replace("-", "")
        for name, spec in sample.items():
            out_file = OUT / f"e2_{tag}_{name}.jsonl"
            if out_file.exists():
                continue
            print(f"E2 {model} / {name}: {len(spec['question_ids'])} questions")
            judge_all(ROOT / spec["questions_file"], ROOT / spec["retrieval_file"],
                      CORPUS, out_file, model=model,
                      only_ids=set(spec["question_ids"]))


def run_e3() -> None:
    """Self-consistency: same model, same settings, repeated."""
    sample = load_sample()
    for rep in (1, 2):
        for name, spec in sample.items():
            out_file = OUT / f"e3_rep{rep}_{name}.jsonl"
            if out_file.exists():
                continue
            print(f"E3 rep{rep} / {name}")
            judge_all(ROOT / spec["questions_file"], ROOT / spec["retrieval_file"],
                      CORPUS, out_file, prompt_id=f"selfconsistency_rep{rep}",
                      only_ids=set(spec["question_ids"]))


def run_e4() -> None:
    """Prompt perturbation, including label-name blinding."""
    sample = load_sample()
    for variant, prompt in (("reworded", PROMPT_REWORDED),
                            ("neutral", PROMPT_NEUTRAL)):
        for name, spec in sample.items():
            out_file = OUT / f"e4_{variant}_{name}.jsonl"
            if out_file.exists():
                continue
            print(f"E4 {variant} / {name}")
            # L1-L4 / P1-P5 are decoded inside judge_all, before validation.
            judge_all(ROOT / spec["questions_file"],
                      ROOT / spec["retrieval_file"], CORPUS, out_file,
                      prompt=prompt, prompt_id=f"prompt_{variant}",
                      label_map=CODE_MAP if variant == "neutral" else None,
                      only_ids=set(spec["question_ids"]))

# --- reporting --------------------------------------------------------------


def _labels(path: Path, ids: list[str], field: str) -> list[str]:
    rows = {r["question_id"]: r for r in load_jsonl(path)}
    return [rows[i][field] for i in ids if i in rows]


def _aligned(paths: list[Path], ids: list[str], field: str) -> list[list[str]]:
    tables = [{r["question_id"]: r[field] for r in load_jsonl(p)} for p in paths]
    common = [i for i in ids if all(i in t for t in tables)]
    return [[t[i] for i in common] for t in tables]


def report() -> dict:
    sample = load_sample()
    rep: dict = {"sample_size": sum(len(v["question_ids"]) for v in sample.values())}

    # E1 -------------------------------------------------------------------
    normal_engaged = mismatch_engaged = normal_n = mismatch_n = 0
    per_system_e1 = {}
    for name, spec in sample.items():
        ids = spec["question_ids"]
        base = _labels(ROOT / spec["annotations_file"], ids, "outcome")
        mism_path = OUT / f"e1_{name}.jsonl"
        if not mism_path.exists():
            continue
        mism = _labels(mism_path, ids, "outcome")
        b_eng = sum(1 for x in base if x != "not_addressed")
        m_eng = sum(1 for x in mism if x != "not_addressed")
        normal_engaged += b_eng; normal_n += len(base)
        mismatch_engaged += m_eng; mismatch_n += len(mism)
        per_system_e1[name] = {"normal_engaged": f"{b_eng}/{len(base)}",
                               "mismatched_engaged": f"{m_eng}/{len(mism)}"}
    if normal_n:
        rep["E1_mismatch_control"] = {
            "normal_engagement_rate": round(normal_engaged / normal_n, 4),
            "mismatched_engagement_rate": round(mismatch_engaged / mismatch_n, 4),
            "normal": f"{normal_engaged}/{normal_n}",
            "mismatched": f"{mismatch_engaged}/{mismatch_n}",
            "per_system": per_system_e1,
        }

    # E2 -------------------------------------------------------------------
    e2: dict = {"pairwise_cohen_kappa": {}, "fleiss_kappa": {},
                "percent_agreement": {}, "conclusion_robustness": {}}
    for field in ("outcome", "premise_status"):
        cols: dict[str, list[str]] = {"gpt-4.1": [], **{m: [] for m in ALT_MODELS}}
        for name, spec in sample.items():
            ids = spec["question_ids"]
            paths = [ROOT / spec["annotations_file"]]
            paths += [OUT / f"e2_{m.replace('.', '').replace('-', '')}_{name}.jsonl"
                      for m in ALT_MODELS]
            if not all(p.exists() for p in paths):
                continue
            aligned = _aligned(paths, ids, field)
            for key, vals in zip(cols, aligned):
                cols[key] += vals
        judges = [k for k in cols if cols[k]]
        if len(judges) < 2:
            continue
        for x, y in combinations(judges, 2):
            e2["pairwise_cohen_kappa"][f"{field}:{x}|{y}"] = cohen_kappa(cols[x], cols[y])
            e2["percent_agreement"][f"{field}:{x}|{y}"] = percent_agreement(cols[x], cols[y])
        e2["fleiss_kappa"][field] = fleiss_kappa([cols[j] for j in judges])

    # do the paper's conclusions survive a judge swap?
    for model in ["gpt-4.1"] + ALT_MODELS:
        rates = {}
        for name, spec in sample.items():
            ids = spec["question_ids"]
            path = (ROOT / spec["annotations_file"] if model == "gpt-4.1"
                    else OUT / f"e2_{model.replace('.', '').replace('-', '')}_{name}.jsonl")
            if not path.exists():
                continue
            outs = _labels(path, ids, "outcome")
            prem = _labels(path, ids, "premise_status")
            if not outs:
                continue
            rates[name] = {
                "engaged": round(sum(1 for o in outs if o != "not_addressed") / len(outs), 3),
                "answered": round(sum(1 for o in outs if o == "answered") / len(outs), 3),
                "refuted": round(sum(1 for p in prem if p == "refuted") / len(prem), 3),
            }
        checks = {}
        if {"tension_llm", "direct_llm"} <= rates.keys():
            checks["tension_llm_refutes_more_than_direct_llm"] = (
                rates["tension_llm"]["refuted"] > rates["direct_llm"]["refuted"])
            checks["tension_llm_answers_more_than_direct_llm"] = (
                rates["tension_llm"]["answered"] > rates["direct_llm"]["answered"])
        if {"direct_llm", "random_claim"} <= rates.keys():
            checks["direct_llm_engages_more_than_random"] = (
                rates["direct_llm"]["engaged"] > rates["random_claim"]["engaged"])
        if {"tension_template", "direct_llm"} <= rates.keys():
            checks["structure_only_answers_more_than_direct_llm"] = (
                rates["tension_template"]["answered"] > rates["direct_llm"]["answered"])
        e2["conclusion_robustness"][model] = {"rates": rates, "checks": checks}
    rep["E2_cross_model"] = e2

    # E3 / E4 --------------------------------------------------------------
    for key, prefixes in (("E3_self_consistency", ["e3_rep1", "e3_rep2"]),
                          ("E4_prompt_perturbation", ["e4_reworded", "e4_neutral"])):
        block = {}
        for prefix in prefixes:
            for field in ("outcome", "premise_status"):
                base_all, var_all = [], []
                for name, spec in sample.items():
                    path = OUT / f"{prefix}_{name}.jsonl"
                    if not path.exists():
                        continue
                    ids = spec["question_ids"]
                    aligned = _aligned([ROOT / spec["annotations_file"], path], ids, field)
                    base_all += aligned[0]; var_all += aligned[1]
                if base_all:
                    block[f"{prefix}:{field}"] = {
                        "percent_agreement": percent_agreement(base_all, var_all),
                        "cohen_kappa": cohen_kappa(base_all, var_all),
                        "n": len(base_all)}
        rep[key] = block

    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "report.json").write_text(json.dumps(rep, indent=2, ensure_ascii=False),
                                     encoding="utf-8")
    print(json.dumps(rep, indent=2, ensure_ascii=False))
    return rep


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=["sample", "e1", "e2", "e2c", "e3", "e4",
                                          "all", "report"])
    args = parser.parse_args()
    if args.stage in ("sample", "all") or not (OUT / "sample.json").exists():
        build_sample()
    if args.stage in ("e1", "all"):
        run_e1()
    if args.stage in ("e2", "all"):
        run_e2()
    if args.stage in ("e2c", "all"):
        run_e2c()
    if args.stage in ("e3", "all"):
        run_e3()
    if args.stage in ("e4", "all"):
        run_e4()
    if args.stage in ("report", "all"):
        report()


if __name__ == "__main__":
    main()
