#!/usr/bin/env python3
"""Baseline 1 — random claims.

Sample random pre-cutoff papers and template their headline result into a
robustness question. This is the floor: no evidence aggregation, no
tension detection, no ranking signal beyond chance.

    python baselines/random_claim.py --corpus data/corpus/past_corpus.jsonl \
        --cutoff 2020-12-31 --domain exoplanet_atmospheres \
        --n 10 --seed 0 --out submissions/random_claim_v1
"""

import argparse
import random

from common import load_past_corpus, submission_record, write_submission

TEMPLATE = ("Is the main result reported in \"{title}\" robust to independent "
            "reanalysis with different modeling assumptions?")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--cutoff", required=True)
    parser.add_argument("--domain", required=True)
    parser.add_argument("--n", type=int, default=10)
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    papers = load_past_corpus(args.corpus, args.cutoff)
    rng = random.Random(args.seed)
    picks = rng.sample(papers, args.n)
    records = [
        submission_record(i + 1, TEMPLATE.format(title=p["title"]),
                          "baseline_random_claim_v1", args.cutoff, args.domain,
                          [p["paper_id"]])
        for i, p in enumerate(picks)
    ]
    write_submission(args.out, records, "baseline_random_claim_v1")


if __name__ == "__main__":
    main()
