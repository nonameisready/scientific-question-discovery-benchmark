#!/usr/bin/env python3
"""Baselines B5/B6 — evidence-tension pairs, two language realizations.

A deterministic, LLM-free detector finds pairs of pre-cutoff abstracts
about the same catalogued object that take opposite stances on the same
chemical species or spectral feature (detection vs. non-detection /
upper limit / doubt). The SAME pairs are then verbalized two ways:

  --mode template   (B6) a fixed template turns each pair into a
                    reconciliation question. Zero LLM anywhere: the
                    question generator has no weights to be contaminated.
  --mode llm        (B5) the pair's two abstracts are handed to an LLM
                    whose ONLY job is to verbalize the detected tension
                    as one precise falsifiable question. The evidence
                    structure is fixed before the LLM sees anything.

B5 and B6 therefore isolate the language-realization layer: any
performance gap between them is attributable to phrasing, not to
evidence selection. This is an evidence-structure-LITE probe (object
co-mention + stance cues on abstracts), not a reimplementation of the
evidence-graph system of the pilot submission.

    python baselines/tension_pair.py --corpus data/corpus/past_corpus_large.jsonl \
        --cutoff 2020-12-31 --domain exoplanet_atmospheres \
        --n 125 --mode template --out submissions/tension_template_L1
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from common import load_past_corpus, submission_record, write_submission  # noqa: E402

from benchmark.specificity import OBJECT_RE, SPECIES  # noqa: E402

API_URL = "https://api.openai.com/v1/chat/completions"

POS_RE = re.compile(
    r"\b(detect(ion|ed)? of|we detect|evidence (of|for)|confirm(ed|ation)?|"
    r"we find|presence of|consistent with the presence|significant absorption|"
    r"strong (absorption|emission|signal))\b", re.IGNORECASE)
NEG_RE = re.compile(
    r"\b(no evidence|non-?detection|do(es)? not detect|upper limits?|rule[sd]? out|"
    r"absence of|featureless|flat (transmission )?spectrum|not confirm(ed)?|"
    r"fail(s|ed)? to (confirm|detect)|inconsistent with|cast(s)? doubt|"
    r"no significant)\b", re.IGNORECASE)

TEMPLATE = (
    "Analyses [{bib_a}] and [{bib_b}] of {obj}'s atmosphere reach potentially "
    "conflicting conclusions regarding {species}: one reports \"{snip_a}\", "
    "while the other reports \"{snip_b}\". Under what observational or "
    "methodological conditions can these results be reconciled, and which "
    "currently untested assumption drives the disagreement?")

LLM_PROMPT = """\
You verbalize scientific tensions. For each numbered evidence pair below you
get two abstracts about the same object that take opposite stances on the same
species/feature. Using ONLY the provided abstracts (no outside knowledge, and
nothing published after {cutoff}), write ONE precise, falsifiable research
question per pair that targets the disagreement and names the object and
species. End every question with '?'.

Return JSON: {{"questions": [{{"pair": int, "question": str}}]}}
"""


def _sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+", text or "") if s.strip()]


def _cue_snippet(abstract: str, species: str, cue_re: re.Pattern) -> str | None:
    for sentence in _sentences(abstract):
        if species.lower() in sentence.lower() and cue_re.search(sentence):
            snip = re.sub(r"\s+", " ", sentence)
            return (snip[:137] + "...") if len(snip) > 140 else snip
    return None


def detect_pairs(papers: list[dict], limit: int) -> list[dict]:
    """Deterministic tension-pair detection. Sorted for reproducibility."""
    by_object: dict[str, list[dict]] = {}
    for p in sorted(papers, key=lambda p: p["paper_id"]):
        text = f"{p.get('title', '')} {p.get('abstract', '')}"
        for match in {m.group(0) for m in OBJECT_RE.finditer(text)}:
            key = re.sub(r"\s+", " ", match.upper()).strip()
            by_object.setdefault(key, []).append(p)

    pairs, used = [], set()
    for obj in sorted(by_object):
        group = by_object[obj]
        if len(group) < 2:
            continue
        for species in SPECIES:
            hits_pos, hits_neg = [], []
            for p in group:
                abstract = p.get("abstract", "")
                if species.lower() not in abstract.lower():
                    continue
                snip_pos = _cue_snippet(abstract, species, POS_RE)
                snip_neg = _cue_snippet(abstract, species, NEG_RE)
                if snip_pos and not snip_neg:
                    hits_pos.append((p, snip_pos))
                elif snip_neg:
                    hits_neg.append((p, snip_neg))
            for (pa, sa), (pb, sb) in zip(hits_pos, hits_neg):
                if pa["paper_id"] == pb["paper_id"]:
                    continue
                dedup = (obj, pa["paper_id"], pb["paper_id"])
                pair_used = (pa["paper_id"], pb["paper_id"])
                if dedup in used or any(u in used for u in pair_used):
                    continue
                used.add(dedup)
                used.update(pair_used)
                pairs.append({"object": obj, "species": species,
                              "pos": pa, "pos_snip": sa,
                              "neg": pb, "neg_snip": sb})
                if len(pairs) >= limit:
                    return pairs
    return pairs


def verbalize_llm(pairs: list[dict], cutoff: str, model: str,
                  batch_size: int = 10) -> list[str]:
    import requests

    questions: list[str] = []
    for start in range(0, len(pairs), batch_size):
        batch = pairs[start:start + batch_size]
        blocks = []
        for i, pr in enumerate(batch, start=1):
            blocks.append(
                f"PAIR {i} — object {pr['object']}, species {pr['species']}\n"
                f"[{pr['pos']['paper_id']}] {pr['pos'].get('title', '')}\n"
                f"{pr['pos'].get('abstract', '')[:1100]}\n"
                f"[{pr['neg']['paper_id']}] {pr['neg'].get('title', '')}\n"
                f"{pr['neg'].get('abstract', '')[:1100]}")
        body = {
            "model": model,
            "response_format": {"type": "json_object"},
            "temperature": 0,
            "messages": [
                {"role": "system", "content": LLM_PROMPT.format(cutoff=cutoff)},
                {"role": "user", "content": "\n\n".join(blocks)},
            ],
        }
        resp = requests.post(
            API_URL, json=body, timeout=300,
            headers={"Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"})
        resp.raise_for_status()
        payload = json.loads(resp.json()["choices"][0]["message"]["content"])
        by_index = {q["pair"]: q["question"].strip() for q in payload["questions"]}
        for i, pr in enumerate(batch, start=1):
            text = by_index.get(i, "")
            if not text.endswith("?"):
                text = TEMPLATE.format(
                    bib_a=pr["pos"]["paper_id"], bib_b=pr["neg"]["paper_id"],
                    obj=pr["object"], species=pr["species"],
                    snip_a=pr["pos_snip"], snip_b=pr["neg_snip"])
            questions.append(text)
    return questions


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--cutoff", required=True)
    parser.add_argument("--domain", required=True)
    parser.add_argument("--n", type=int, default=125)
    parser.add_argument("--mode", choices=["template", "llm"], required=True)
    parser.add_argument("--model", default="gpt-4.1",
                        help="LLM for --mode llm verbalization")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    papers = load_past_corpus(args.corpus, args.cutoff)
    pairs = detect_pairs(papers, args.n)
    if not pairs:
        raise SystemExit("no tension pairs detected in this corpus")

    if args.mode == "template":
        system = "baseline_tension_template_v1"
        questions = [TEMPLATE.format(
            bib_a=pr["pos"]["paper_id"], bib_b=pr["neg"]["paper_id"],
            obj=pr["object"], species=pr["species"],
            snip_a=pr["pos_snip"], snip_b=pr["neg_snip"]) for pr in pairs]
    else:
        system = f"baseline_tension_llm_{args.model}_v1"
        questions = verbalize_llm(pairs, args.cutoff, args.model)

    records = [
        submission_record(i + 1, q, system, args.cutoff, args.domain,
                          [pr["pos"]["paper_id"], pr["neg"]["paper_id"]])
        for i, (q, pr) in enumerate(zip(questions, pairs))
    ]
    write_submission(args.out, records, system)


if __name__ == "__main__":
    main()
