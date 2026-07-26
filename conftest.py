"""Root conftest: make the repo root importable (benchmark/, paper3/)."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
