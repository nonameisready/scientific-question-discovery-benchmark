"""Metric computation: synthetic fixture + released astronomy v1 results."""

import json

from benchmark import PROTOCOL_VERSION
from benchmark.metrics import compute_metrics, compute_from_file

SYNTHETIC = [
    {"question_id": "a", "outcome": "answered", "premise_status": "refuted",
     "supporting_bibcodes": ["2025A&A...700A.105B", "2023ApJ...900...10X"],
     "retrieval_top_similarity": 0.7},
    {"question_id": "b", "outcome": "partially_addressed", "premise_status": "supported",
     "supporting_bibcodes": ["2021ApJ...900...11X"], "retrieval_top_similarity": 0.6},
    {"question_id": "c", "outcome": "posed_but_open", "premise_status": "still_plausible",
     "supporting_bibcodes": ["2022ApJ...900...12X"], "retrieval_top_similarity": 0.5},
    {"question_id": "d", "outcome": "not_addressed", "premise_status": "still_plausible",
     "supporting_bibcodes": [], "retrieval_top_similarity": 0.4},
]


def test_synthetic_metrics():
    m = compute_metrics(SYNTHETIC, benchmark_version="test", cutoff_date="2020-12-31")
    assert m["n_questions"] == 4
    assert m["future_attention_rate"] == 0.75
    assert m["answered_rate"] == 0.25
    assert m["partial_rate"] == 0.25
    assert m["posed_but_open_rate"] == 0.25
    assert m["not_addressed_rate"] == 0.25
    assert m["premise_refutation_rate"] == 0.25
    assert m["mean_retrieval_support_count"] == round(4 / 3, 2)
    assert m["multi_source_rate"] == 0.25
    # earliest evidence years: 2023, 2021, 2022 -> lags 3, 1, 2
    assert m["first_engagement_lag_years"]["mean"] == 2.0
    assert m["mean_lead_time_years"] is None


def test_outcome_rates_sum_to_one():
    m = compute_metrics(SYNTHETIC, benchmark_version="test", cutoff_date="2020-12-31")
    total = (m["answered_rate"] + m["partial_rate"] + m["posed_but_open_rate"]
             + m["not_addressed_rate"])
    assert abs(total - 1.0) < 1e-9
    assert abs(m["future_attention_rate"] - (1 - m["not_addressed_rate"])) < 1e-9


def test_astronomy_v1_headline_numbers(cfg, root):
    m = compute_from_file(root / cfg.annotations_file,
                          benchmark_version=cfg.benchmark_version,
                          cutoff_date=cfg.cutoff_date)
    assert m["n_questions"] == 10
    assert m["future_attention_rate"] == 1.0
    assert m["answered_rate"] == 0.2
    assert m["partial_rate"] == 0.7
    assert m["posed_but_open_rate"] == 0.1
    assert m["not_addressed_rate"] == 0.0
    assert m["premise_refutation_rate"] == 0.1


def test_released_metrics_json_reproduces(cfg, root):
    committed = json.loads((root / cfg.results_dir / "metrics.json").read_text())
    recomputed = compute_from_file(root / cfg.annotations_file,
                                   benchmark_version=cfg.benchmark_version,
                                   cutoff_date=cfg.cutoff_date,
                                   protocol_version=PROTOCOL_VERSION)
    assert committed == recomputed
