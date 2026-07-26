#!/usr/bin/env python3
"""Retrieve top-k future evidence for every frozen question.

    python scripts/retrieve_future_evidence.py --config configs/astronomy_2020.yaml \
        --corpus data/corpus/future_corpus.jsonl

Requires OPENAI_API_KEY and a future-corpus JSONL of
{paper_id, title, abstract, pubdate} built with scripts/prepare_corpus.py.
Refuses to overwrite an existing (frozen) retrieval file unless --force.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark.config import BenchmarkConfig  # noqa: E402
from benchmark.retrieval import retrieve  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="configs/astronomy_2020.yaml")
    parser.add_argument("--corpus", required=True,
                        help="future-corpus JSONL (paper_id, title, abstract, pubdate)")
    parser.add_argument("--force", action="store_true",
                        help="overwrite an existing retrieval file")
    args = parser.parse_args()
    cfg = BenchmarkConfig.load(args.config)
    if Path(cfg.retrieval_file).exists() and not args.force:
        raise SystemExit(
            f"{cfg.retrieval_file} exists and is frozen; released retrieval runs "
            "are never overwritten (use --force only for a NEW instance file)")
    records = retrieve(
        cfg.questions_file, args.corpus, cfg.retrieval_file,
        model=cfg.retrieval.model, top_k=cfg.retrieval.top_k,
        corpus_id=Path(args.corpus).stem,
        corpus_start=cfg.retrieval.corpus_start,
        corpus_end=cfg.retrieval.corpus_end)
    print(f"OK: retrieved top-{cfg.retrieval.top_k} for {len(records)} questions "
          f"-> {cfg.retrieval_file}")


if __name__ == "__main__":
    main()
