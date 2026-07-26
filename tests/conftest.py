import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from benchmark.config import BenchmarkConfig  # noqa: E402
from benchmark.schemas import load_jsonl  # noqa: E402


@pytest.fixture(scope="session")
def cfg():
    return BenchmarkConfig.load(ROOT / "configs" / "astronomy_2020.yaml")


@pytest.fixture(scope="session")
def questions(cfg):
    return load_jsonl(ROOT / cfg.questions_file)


@pytest.fixture(scope="session")
def retrieval(cfg):
    return load_jsonl(ROOT / cfg.retrieval_file)


@pytest.fixture(scope="session")
def outcomes(cfg):
    return load_jsonl(ROOT / cfg.annotations_file)


@pytest.fixture(scope="session")
def root():
    return ROOT
