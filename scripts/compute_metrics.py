#!/usr/bin/env python3
"""Compute benchmark metrics from an annotations file.

    python scripts/compute_metrics.py \
        --annotations data/annotations/outcomes_v1.jsonl
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark import PROTOCOL_VERSION  # noqa: E402
from benchmark.metrics import compute_from_file, save_metrics  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--annotations", required=True)
    parser.add_argument("--benchmark-version", default="astronomy_v1")
    parser.add_argument("--cutoff", default="2020-12-31")
    parser.add_argument("--out", default=None, help="optional metrics.json path")
    args = parser.parse_args()
    metrics = compute_from_file(args.annotations,
                                benchmark_version=args.benchmark_version,
                                cutoff_date=args.cutoff,
                                protocol_version=PROTOCOL_VERSION)
    print(json.dumps(metrics, indent=2))
    if args.out:
        save_metrics(metrics, args.out)
        print(f"-> {args.out}")


if __name__ == "__main__":
    main()
