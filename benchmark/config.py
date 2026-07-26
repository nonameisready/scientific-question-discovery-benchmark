"""Benchmark run configuration.

A benchmark instance is fully described by one YAML config
(e.g. configs/astronomy_2020.yaml): where the frozen questions live,
the cutoff, the future window, retrieval settings, and output paths.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class RetrievalConfig:
    model: str = "text-embedding-3-small"
    top_k: int = 8
    corpus_start: str = "2021-01-01"
    corpus_end: str = "2026-07-01"


@dataclass
class BenchmarkConfig:
    benchmark_version: str
    cutoff_date: str
    domain: str
    questions_file: str
    retrieval_file: str
    annotations_file: str
    results_dir: str
    future_corpus_manifest: str
    past_corpus_manifest: str
    judge_model: str = "gpt-4.1"
    retrieval: RetrievalConfig = field(default_factory=RetrievalConfig)

    @classmethod
    def load(cls, path: str | Path) -> "BenchmarkConfig":
        with open(path, encoding="utf-8") as f:
            raw = yaml.safe_load(f)
        retrieval = RetrievalConfig(**raw.pop("retrieval", {}))
        return cls(retrieval=retrieval, **raw)
