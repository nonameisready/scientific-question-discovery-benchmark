#!/usr/bin/env python3
"""Baseline 3 — review-paper future work.

Extract explicitly posed open questions / future-work statements from
pre-cutoff review papers. This baseline represents what the community
itself already said should be investigated — a strong reference point:
a discovery system is only interesting if it beats questions that were
already written down.

Heuristic extraction (no LLM): sentences from review abstracts that end
with '?' or open with a future-work cue.

    python baselines/review_future_work.py --corpus data/corpus/past_corpus.jsonl \
        --cutoff 2020-12-31 --domain exoplanet_atmospheres \
        --n 10 --out submissions/review_future_work_v1
"""

import argparse
import re

from common import load_past_corpus, submission_record, write_submission

REVIEW_CUE = re.compile(r"\breview\b|\boverview\b|\bprogress\b", re.I)
FUTURE_CUE = re.compile(
    r"^(future|further|it remains|open questions?|a key question|whether)\b", re.I)


def extract_questions(abstract: str) -> list[str]:
    sentences = re.split(r"(?<=[.?!])\s+", abstract or "")
    out = []
    for s in sentences:
        s = s.strip()
        if s.endswith("?"):
            out.append(s)
        elif FUTURE_CUE.match(s) and len(s) > 60:
            out.append(f"{s.rstrip('.')} — how can this be resolved observationally?")
    return out


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--cutoff", required=True)
    parser.add_argument("--domain", required=True)
    parser.add_argument("--n", type=int, default=10)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    papers = load_past_corpus(args.corpus, args.cutoff)
    reviews = [p for p in papers
               if REVIEW_CUE.search(f"{p.get('title', '')} {p.get('abstract', '')}")]
    records = []
    for p in reviews:
        for q in extract_questions(p.get("abstract", "")):
            records.append(submission_record(
                len(records) + 1, q, "baseline_review_future_work_v1",
                args.cutoff, args.domain, [p["paper_id"]]))
            if len(records) >= args.n:
                break
        if len(records) >= args.n:
            break
    if not records:
        raise SystemExit("no future-work questions extracted; corpus may lack reviews")
    write_submission(args.out, records, "baseline_review_future_work_v1")


if __name__ == "__main__":
    main()
