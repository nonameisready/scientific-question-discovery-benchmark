#!/usr/bin/env python3
"""Validate that a question submission respects temporal isolation.

    python scripts/validate_cutoff.py \
        --questions data/questions/astronomy_questions_v1.jsonl \
        --cutoff 2020-12-31
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark.leakage import check_question_cutoffs  # noqa: E402
from benchmark.schemas import validate_file  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--questions", required=True)
    parser.add_argument("--cutoff", required=True)
    args = parser.parse_args()
    questions = validate_file(args.questions, "question")
    check_question_cutoffs(questions, args.cutoff)
    print(f"OK: {len(questions)} questions frozen, all source evidence <= {args.cutoff}")


if __name__ == "__main__":
    main()
