#!/usr/bin/env python3
"""Score specificity + SAF for one evaluated submission.

    python scripts/score_specificity.py \
        --questions submissions/direct_llm_L1/questions.jsonl \
        --annotations data/annotations/outcomes_direct_llm_L.jsonl \
        --out results/direct_llm_L/specificity.json

Deterministic (no API). See benchmark/specificity.py for the rubric.
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark.schemas import load_jsonl  # noqa: E402
from benchmark.specificity import saf  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--questions", required=True)
    parser.add_argument("--annotations", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    report = saf(load_jsonl(args.questions), load_jsonl(args.annotations))
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"OK: n={report['n']} mean_spec={report['mean_specificity']} "
          f"components={report['component_rates']} SAF={report['saf']} -> {args.out}")


if __name__ == "__main__":
    main()
