#!/usr/bin/env python3
"""Judge outcomes for every question against its retrieved future evidence.

    python scripts/judge_outcomes.py --config configs/astronomy_2020.yaml \
        --corpus data/corpus/future_corpus.jsonl

Requires OPENAI_API_KEY. Judge output is constrained (labels validated,
citations restricted to the retrieved candidates) and marked unreviewed:
human adjudication is required before results are released.
Refuses to overwrite an existing (frozen) annotations file unless --out
points elsewhere.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark.config import BenchmarkConfig  # noqa: E402
from benchmark.judging import judge_all  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="configs/astronomy_2020.yaml")
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--out", default=None,
                        help="output annotations file (default: config value)")
    args = parser.parse_args()
    cfg = BenchmarkConfig.load(args.config)
    out = Path(args.out or cfg.annotations_file)
    if out.exists():
        raise SystemExit(
            f"{out} exists and is frozen; released annotation runs are never "
            "overwritten (pass --out for a new run)")
    records = judge_all(cfg.questions_file, cfg.retrieval_file, args.corpus, out,
                        model=cfg.judge_model)
    print(f"OK: judged {len(records)} questions -> {out} (adjudication required)")


if __name__ == "__main__":
    main()
