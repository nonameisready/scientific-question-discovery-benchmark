#!/usr/bin/env python3
"""Blinded human-annotation package, and scoring against the LLM judge.

    python scripts/human_annotation.py build   # writes annotation/ packets
    python scripts/human_annotation.py score   # after sheets are filled in

The package deliberately reuses the frozen judge-validation sample
(results/judge_validation/sample.json), so every human label lines up
item-for-item with gpt-4.1, the two alternative judge models, and the
self-consistency reruns.

Blinding, in the order that matters to a reviewer:
  - system identity is replaced by sys_A..sys_F and the mapping is written
    to a separate decode file annotators must not open;
  - items from all systems are interleaved in one shuffled order;
  - no LLM label, rationale, or citation appears anywhere in the packet;
  - candidate abstracts are shuffled within each item, so retrieval rank
    carries no signal.

Two annotators should label independently, without discussing. Scoring
reports human-human agreement (the ceiling for this task) alongside
human-LLM agreement (the number that decides whether the judge is
adequate).
"""

import argparse
import csv
import json
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark.schemas import load_jsonl  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
SAMPLE = ROOT / "results" / "judge_validation" / "sample.json"
CORPUS = ROOT / "data" / "corpus" / "future_corpus_large_frozen_window.jsonl"
PACK = ROOT / "annotation"
SEED = 512026
ANNOTATORS = ("annotator_1", "annotator_2")

CODEBOOK = """\
# 标注手册 / Annotation codebook — historical backtesting outcomes

> 中英对照版。术语代码（`answered` 等）保持英文原样填写，说明为中英双语。
> Bilingual. Label codes are always written in English; explanations are given
> in Chinese and English.

## 中文速览

你看到的是一个写于 **2021 年之前**的科研问题，加上最多 8 篇**之后**发表的论文摘要。
**只根据这些摘要判断**，不要上网查——AI 裁判当时看到的就是这几篇。

每题给**两个独立标签**：

| `outcome` 问题本身的命运 | 含义 |
|---|---|
| `answered` | 已解决：后续文献实质性解决了它，你现在能说出答案 |
| `partially_addressed` | 部分推进：有直接相关的实质进展，核心问题仍未解决 |
| `posed_but_open` | 被提出但未解决：后续文献也提出了同一问题，但没解决 |
| `not_addressed` | 未被触及：没有摘要实质涉及它（**同话题不算**） |

| `premise_status` 它依赖的假设的命运 | 含义 |
|---|---|
| `supported` | 假设被证实 |
| `refuted` | 假设被推翻 |
| `weakened` | 假设被动摇，但未彻底证伪 |
| `still_plausible` | 假设未被直接检验过 |
| `not_applicable` | 这个问题不依赖任何可争议的假设 |

**最容易犯的错：把「同话题」当成「有人研究了这个问题」。** 摘要讲同一颗行星、
同一个分子都**不算**，必须碰到这个问题真正要检验的东西，或它依赖的那个假设。

一个问题可以**正因为**假设被推翻而得到解决：`answered` + `refuted` 是合理组合。

`confidence` 填 1（没把握）/ 2（一般）/ 3（很有把握）；`notes` 写你犹豫在哪里。

---

## English version

You will see a research question written **before 2021**, and up to eight
abstracts of papers published **after** it. Judge only from these abstracts.
You do not need to know the field's later history; if an abstract does not
show it, it did not happen for our purposes.

Assign **two independent labels** per item.

## Label 1 — outcome: what happened to the question?

| Code | Meaning | Test to apply |
|---|---|---|
| `answered` | The literature substantially resolved it | Could you now state the answer, citing these abstracts? |
| `partially_addressed` | Substantial directly-relevant progress, core question still open | Real progress on *this* question, but no resolution |
| `posed_but_open` | Later work independently raises the same question without resolving it | The abstracts ask it too, and leave it open |
| `not_addressed` | No abstract engages it substantively | Same topic is **not** engagement |

**The single most common error is confusing topic overlap with engagement.**
An abstract about the same planet, or the same molecule, does not count
unless it bears on the question's actual test or its premise.

## Label 2 — premise_status: what happened to the assumption the question rests on?

| Code | Meaning |
|---|---|
| `supported` | Later evidence confirms the premise |
| `refuted` | Later evidence falsifies it |
| `weakened` | Later evidence seriously undermines it without falsifying |
| `still_plausible` | The premise was never directly tested |
| `not_applicable` | The question rests on no contestable premise |

A question can be `answered` **because** its premise was `refuted` — that
combination is expected, not a contradiction.

## Worked examples

*Question:* "Is the strongly subsolar terminator water abundance retrieved for
HD 209458 b a property of the atmosphere, or an artifact of retrieval
assumptions?"
*Abstracts:* three independent reanalyses converging on a solar abundance.
→ `answered` + `refuted` (the question is settled, and settled by overturning
the premise it challenged).

*Question:* the same question.
*Abstracts:* several papers measuring water in *other* hot Jupiters.
→ `not_addressed` (same topic, different object — no bearing on this test).

*Question:* "How do inhomogeneous terminators bias retrieved abundances?"
*Abstracts:* papers demonstrating the bias exists in general, none resolving
the specific case asked about.
→ `partially_addressed` + `still_plausible`.

## Procedure

1. Work through items **in the order given**; do not skip ahead.
2. Do **not** discuss items with the other annotator until both sheets are done.
3. Do **not** look up the papers online — abstracts only. The LLM judge saw
   exactly these abstracts, so any extra knowledge you use breaks the
   comparison.
4. Enter `confidence` as 1 (low) / 2 (medium) / 3 (high). Low-confidence items
   are analysed separately — they are informative, not failures.
5. Use `notes` freely, especially where you hesitated.

Budget roughly 2–3 minutes per item.
"""

README = """\
# Blinded annotation package

**Do not open `decode.json` until both annotation sheets are complete.**
It maps the anonymised system codes back to real systems, and reading it
before annotating destroys the blinding this validation depends on.

## Files

| File | What to do with it |
|---|---|
| `codebook.md` | Read first, in full. |
| `annotation_packet.md` | The 90 items, in fixed order. Read here. |
| `annotator_1_sheet.csv`, `annotator_2_sheet.csv` | One per person. Fill `outcome`, `premise_status`, `confidence`, `notes`. |
| `decode.json` | Sealed until both sheets are done. |

## Steps

1. Two people read `codebook.md`.
2. Each fills their own sheet independently, no discussion.
3. Run `python scripts/human_annotation.py score`, which reports
   human-human agreement and human-LLM agreement.
4. Meet, resolve disagreements, and record the reasoning in the
   `notes` column of a merged sheet named `adjudicated_sheet.csv`
   (same columns). This becomes the released adjudication log.

If only one annotator is available the package still works: you get
human-LLM agreement but no human-human ceiling, and the paper must say so.
"""


def build(seed: int = SEED) -> None:
    sample = json.loads(SAMPLE.read_text(encoding="utf-8"))
    papers = {p["paper_id"]: p for p in load_jsonl(CORPUS)}
    rng = random.Random(seed)

    system_names = sorted(sample)
    # Letters are assigned at random, not by sorted system name: a fixed
    # assignment leaks the mapping the moment any one code is disclosed.
    letters = [f"sys_{chr(ord('A') + i)}" for i in range(len(system_names))]
    rng.shuffle(letters)
    codes = dict(zip(system_names, letters))

    items = []
    for name in system_names:
        spec = sample[name]
        questions = {q["question_id"]: q
                     for q in load_jsonl(ROOT / spec["questions_file"])}
        retrieval = {r["question_id"]: r
                     for r in load_jsonl(ROOT / spec["retrieval_file"])}
        for qid in spec["question_ids"]:
            docs = [papers[d["bibcode"]] for d in retrieval[qid]["documents"]
                    if d["bibcode"] in papers]
            rng.shuffle(docs)
            items.append({"system_code": codes[name], "source_system": name,
                          "question_id": qid,
                          "question": questions[qid]["question"], "docs": docs})
    rng.shuffle(items)
    for i, item in enumerate(items, start=1):
        item["item_id"] = f"item_{i:03d}"

    PACK.mkdir(parents=True, exist_ok=True)
    lines = ["# Annotation packet", "",
             f"{len(items)} items. Labels and definitions: see `codebook.md`. "
             "Record answers in your own CSV sheet.", ""]
    for item in items:
        lines += [f"## {item['item_id']}", "",
                  f"**Question ({item['system_code']}):** {item['question']}", "",
                  f"Candidate post-cutoff abstracts ({len(item['docs'])}):", ""]
        for j, d in enumerate(item["docs"], start=1):
            abstract = " ".join((d.get("abstract") or "").split())
            lines += [f"**[{j}] {d.get('title', '')}** ({d.get('pubdate', '')})", "",
                      abstract, ""]
        lines += ["---", ""]
    (PACK / "annotation_packet.md").write_text("\n".join(lines), encoding="utf-8")

    for who in ANNOTATORS:
        with open(PACK / f"{who}_sheet.csv", "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["item_id", "outcome", "premise_status", "confidence", "notes"])
            for item in items:
                w.writerow([item["item_id"], "", "", "", ""])

    (PACK / "codebook.md").write_text(CODEBOOK, encoding="utf-8")
    (PACK / "README.md").write_text(README, encoding="utf-8")
    decode = {item["item_id"]: {"system": item["source_system"],
                                "system_code": item["system_code"],
                                "question_id": item["question_id"]}
              for item in items}
    (PACK / "decode.json").write_text(json.dumps(decode, indent=2), encoding="utf-8")
    (PACK / "blinding_meta.json").write_text(json.dumps(
        {"seed": seed, "n_items": len(items),
         "note": "Item order and system codes are regenerated whenever the "
                 "previous mapping is exposed; the question set is unchanged so "
                 "labels stay aligned with the judge runs."},
        indent=2), encoding="utf-8")
    print(f"OK: {len(items)} blinded items -> {PACK}/")
    print("     annotation_packet.md, codebook.md, README.md, "
          f"{len(ANNOTATORS)} sheets, decode.json (sealed)")


def _read_sheet(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, encoding="utf-8") as f:
        return {r["item_id"]: r for r in csv.DictReader(f)
                if (r.get("outcome") or "").strip()}


def score() -> None:
    sys.path.insert(0, str(ROOT / "scripts"))
    from judge_validation import ALT_MODELS, cohen_kappa, percent_agreement

    decode = json.loads((PACK / "decode.json").read_text(encoding="utf-8"))
    sample = json.loads(SAMPLE.read_text(encoding="utf-8"))
    sheets = {who: _read_sheet(PACK / f"{who}_sheet.csv") for who in ANNOTATORS}
    sheets = {k: v for k, v in sheets.items() if v}
    if not sheets:
        raise SystemExit("no completed annotation sheets found in annotation/")

    llm: dict[str, dict[str, dict]] = {}
    for model in ["gpt-4.1"] + ALT_MODELS:
        table = {}
        for name, spec in sample.items():
            path = (ROOT / spec["annotations_file"] if model == "gpt-4.1" else
                    ROOT / "results" / "judge_validation" /
                    f"e2_{model.replace('.', '').replace('-', '')}_{name}.jsonl")
            if path.exists():
                for r in load_jsonl(path):
                    table[(name, r["question_id"])] = r
        llm[model] = table

    report: dict = {"n_items_labelled": {k: len(v) for k, v in sheets.items()}}
    for field in ("outcome", "premise_status"):
        block: dict = {}
        if len(sheets) == 2:
            a, b = ANNOTATORS
            common = [i for i in sheets[a] if i in sheets[b]]
            if common:
                block["human_human"] = {
                    "n": len(common),
                    "percent_agreement": percent_agreement(
                        [sheets[a][i][field] for i in common],
                        [sheets[b][i][field] for i in common]),
                    "cohen_kappa": cohen_kappa(
                        [sheets[a][i][field] for i in common],
                        [sheets[b][i][field] for i in common]),
                }
        for who, sheet in sheets.items():
            for model, table in llm.items():
                pairs = []
                for item_id, row in sheet.items():
                    meta = decode[item_id]
                    key = (meta["system"], meta["question_id"])
                    if key in table:
                        pairs.append((row[field], table[key][field]))
                if pairs:
                    block[f"{who}_vs_{model}"] = {
                        "n": len(pairs),
                        "percent_agreement": percent_agreement(
                            [p[0] for p in pairs], [p[1] for p in pairs]),
                        "cohen_kappa": cohen_kappa(
                            [p[0] for p in pairs], [p[1] for p in pairs]),
                    }
        hh = block.get("human_human", {}).get("cohen_kappa")
        hl = [v["cohen_kappa"] for k, v in block.items() if "_vs_gpt-4.1" in k]
        if hh and hl:
            block["llm_vs_human_ceiling_ratio"] = round(
                (sum(hl) / len(hl)) / hh, 3) if hh else None
        report[field] = block

    # Post-stratification: when only the stratified subset was labelled,
    # reweight each stratum by its share of the full 90-item sample so the
    # reported agreement estimates the population rather than the
    # disagreement-enriched subset.
    subset_path = ROOT / "results" / "judge_validation" / "subset.json"
    if subset_path.exists():
        spec = json.loads(subset_path.read_text(encoding="utf-8"))
        stratum_of = {(i["system"], i["question_id"]): i["stratum"]
                      for i in spec["items"]}
        weights = {k: v["weight"] for k, v in spec["strata"].items()}
        for field in ("outcome", "premise_status"):
            for who, sheet in sheets.items():
                for model, table in llm.items():
                    hits: dict[str, list[int]] = {}
                    for item_id, row in sheet.items():
                        meta = decode[item_id]
                        key = (meta["system"], meta["question_id"])
                        if key not in stratum_of or key not in table:
                            continue
                        bucket = hits.setdefault(stratum_of[key], [])
                        bucket.append(int(row[field] == table[key][field]))
                    covered = sum(len(v) for v in hits.values())
                    expected = sum(st["sampled"] for st in spec["strata"].values())
                    if len(hits) < len(weights) or covered < 0.8 * expected:
                        # Too little of the stratified subset was labelled for
                        # post-stratification to mean anything; reporting it
                        # anyway would dress up a handful of items as a
                        # population estimate.
                        continue
                    weighted = sum(weights[s] * (sum(v) / len(v))
                                   for s, v in hits.items() if v)
                    report[field][f"{who}_vs_{model}_stratum_weighted"] = {
                        "weighted_percent_agreement": round(weighted, 4),
                        "per_stratum": {s: {"n": len(v),
                                            "agreement": round(sum(v) / len(v), 4)}
                                        for s, v in hits.items()},
                        "note": "post-stratified to the 90-item sample; "
                                "stratum D = judges disagreed, A = judges agreed",
                    }

    out = ROOT / "results" / "judge_validation" / "human_agreement.json"
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    print(f"\nOK -> {out}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("stage", choices=["build", "score"])
    parser.add_argument("--seed", type=int, default=SEED,
                        help="reshuffle order and re-letter system codes")
    args = parser.parse_args()
    build(args.seed) if args.stage == "build" else score()


if __name__ == "__main__":
    main()
