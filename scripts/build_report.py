#!/usr/bin/env python3
"""Build the full benchmark report (metrics.json, per-question CSV,
report.md, leaderboard entry) for a benchmark instance.

    python scripts/build_report.py --config configs/astronomy_2020.yaml
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark.run import main  # noqa: E402

if __name__ == "__main__":
    main()
