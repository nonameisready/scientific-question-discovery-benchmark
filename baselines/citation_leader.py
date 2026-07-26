#!/usr/bin/env python3
"""Baseline 4 — citation leaders.

Take the most-cited pre-cutoff papers and template their headline result
into a follow-up question. Tests whether simply chasing prominence
matches structured evidence analysis. Requires a `citation_count` field
in the corpus records (available from the ADS `citation` field at corpus
build time).

    python baselines/citation_leader.py --corpus data/corpus/past_corpus.jsonl \
        --cutoff 2020-12-31 --domain exoplanet_atmospheres \
        --n 10 --out submissions/citation_leader_v1
"""

import argparse

from common import load_past_corpus, submission_record, write_submission

TEMPLATE = ("Does the central conclusion of the highly cited study \"{title}\" hold "
            "under independent datasets and alternative analysis assumptions?")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--cutoff", required=True)
    parser.add_argument("--domain", required=True)
    parser.add_argument("--n", type=int, default=10)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    papers = load_past_corpus(args.corpus, args.cutoff)
    ranked = sorted(papers, key=lambda p: p.get("citation_count", 0), reverse=True)
    if not ranked or ranked[0].get("citation_count") is None:
        raise SystemExit("corpus records lack citation_count; rebuild with citations")
    records = [
        submission_record(i + 1, TEMPLATE.format(title=p["title"]),
                          "baseline_citation_leader_v1", args.cutoff, args.domain,
                          [p["paper_id"]])
        for i, p in enumerate(ranked[:args.n])
    ]
    write_submission(args.out, records, "baseline_citation_leader_v1")


if __name__ == "__main__":
    main()
