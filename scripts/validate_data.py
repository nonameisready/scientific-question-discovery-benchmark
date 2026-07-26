#!/usr/bin/env python3
"""Release-data validation (run in CI on every change).

Checks, per benchmark instance config:
  1. JSONL well-formedness and schema conformance for all three files
  2. unique question_ids, aligned across files
  3. no cutoff violations in question source evidence
  4. no pre-cutoff documents in the future-evidence retrieval records
  5. judge citations restricted to the retrieved candidates
  6. future-corpus window strictly after the cutoff
  7. committed metrics.json matches recomputation from the annotations

    python scripts/validate_data.py --config configs/astronomy_2020.yaml
"""

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark import PROTOCOL_VERSION  # noqa: E402
from benchmark.config import BenchmarkConfig  # noqa: E402
from benchmark.leakage import run_all_checks  # noqa: E402
from benchmark.metrics import compute_from_file  # noqa: E402
from benchmark.schemas import validate_file  # noqa: E402


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--config", default="configs/astronomy_2020.yaml")
    args = parser.parse_args()
    cfg = BenchmarkConfig.load(args.config)

    validate_file(cfg.questions_file, "question")
    validate_file(cfg.retrieval_file, "retrieval")
    validate_file(cfg.annotations_file, "outcome")
    print("schemas: OK")

    run_all_checks(cfg.questions_file, cfg.retrieval_file, cfg.annotations_file,
                   cfg.future_corpus_manifest, cfg.cutoff_date)
    print("temporal isolation: OK")

    metrics_path = Path(cfg.results_dir) / "metrics.json"
    if metrics_path.exists():
        committed = json.loads(metrics_path.read_text(encoding="utf-8"))
        recomputed = compute_from_file(cfg.annotations_file,
                                       benchmark_version=cfg.benchmark_version,
                                       cutoff_date=cfg.cutoff_date,
                                       protocol_version=PROTOCOL_VERSION)
        if committed != recomputed:
            diff = {k for k in set(committed) | set(recomputed)
                    if committed.get(k) != recomputed.get(k)}
            raise SystemExit(f"metrics.json does not match recomputation; differing keys: {diff}")
        print("released metrics reproduce: OK")
    print(f"all release-data checks passed for {cfg.benchmark_version}")


if __name__ == "__main__":
    main()
