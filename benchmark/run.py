"""One-command benchmark run.

    python -m benchmark.run --config configs/astronomy_2020.yaml

Stages:
  1. schema validation + leakage checks (always)
  2. retrieval  (skipped if the retrieval file already exists; live runs
                 need OPENAI_API_KEY and a prepared future corpus)
  3. judging    (skipped if the annotations file already exists)
  4. metrics + per-question CSV + markdown report + leaderboard entry

Released benchmark instances ship frozen retrieval and annotation files,
so a full offline reproduction of the metrics and report requires no API
access at all.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from . import PROTOCOL_VERSION
from .config import BenchmarkConfig
from .leakage import run_all_checks
from .metrics import compute_from_file, save_metrics
from .reporting import build_report, per_question_rows, update_leaderboard, write_csv
from .schemas import load_jsonl, validate_file


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="configs/astronomy_2020.yaml")
    parser.add_argument("--system", default="evidence_graph_v1",
                        help="system name for the leaderboard entry")
    parser.add_argument("--skip-leaderboard", action="store_true")
    args = parser.parse_args()
    cfg = BenchmarkConfig.load(args.config)

    print(f"[1/4] validating schemas and temporal isolation ({cfg.benchmark_version})")
    validate_file(cfg.questions_file, "question")
    validate_file(cfg.retrieval_file, "retrieval")
    validate_file(cfg.annotations_file, "outcome")
    run_all_checks(cfg.questions_file, cfg.retrieval_file, cfg.annotations_file,
                   cfg.future_corpus_manifest, cfg.cutoff_date)
    print("      all checks passed")

    if not Path(cfg.retrieval_file).exists():
        raise SystemExit(
            "[2/4] no retrieval file: run scripts/retrieve_future_evidence.py first")
    print("[2/4] retrieval file present (frozen)")
    if not Path(cfg.annotations_file).exists():
        raise SystemExit(
            "[3/4] no annotations file: run scripts/judge_outcomes.py first")
    print("[3/4] annotations file present (frozen)")

    print("[4/4] computing metrics and building report")
    metrics = compute_from_file(cfg.annotations_file,
                                benchmark_version=cfg.benchmark_version,
                                cutoff_date=cfg.cutoff_date,
                                protocol_version=PROTOCOL_VERSION)
    results = Path(cfg.results_dir)
    save_metrics(metrics, results / "metrics.json")
    questions = load_jsonl(cfg.questions_file)
    outcomes = load_jsonl(cfg.annotations_file)
    write_csv(per_question_rows(questions, outcomes), results / "per_question_results.csv")
    build_report(metrics, questions, outcomes, results / "report.md")
    if not args.skip_leaderboard:
        update_leaderboard(metrics, args.system, results.parent / "leaderboard.json")
    print(json.dumps(metrics, indent=2))
    print(f"results -> {results}/")


if __name__ == "__main__":
    main()
