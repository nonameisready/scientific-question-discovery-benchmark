"""Benchmark metrics.

Formal definitions (n = number of frozen questions; see the paper,
Section "Benchmark Metrics"):

  future_attention_rate   |outcome != not_addressed| / n        ("Coverage")
  answered_rate           |outcome = answered| / n
  partial_rate            |outcome = partially_addressed| / n
  posed_but_open_rate     |outcome = posed_but_open| / n
  not_addressed_rate      |outcome = not_addressed| / n
  premise_refutation_rate |premise_status = refuted| / n
  evidence strength       mean # independent supporting papers per engaged
                          question, and the fraction supported by >= 2
                          independent papers (multi_source_rate)
  first_engagement_lag    years from the cutoff to the earliest judge-cited
                          supporting paper (a *lower bound* on how quickly
                          the community engaged; descriptive only)
  mean_lead_time_years    years between question submission and the first
                          time the community *independently poses* the same
                          question. Requires community-posing dates that v1
                          does not reliably have -> reported as null, never
                          approximated.

All rates are over n, so the four outcome rates sum to 1 and
future_attention_rate = 1 - not_addressed_rate.
"""

from __future__ import annotations

import json
from pathlib import Path

from .schemas import bibcode_year, load_jsonl


def _rate(count: int, n: int) -> float:
    return round(count / n, 4) if n else 0.0


def compute_metrics(outcomes: list[dict], *, benchmark_version: str,
                    cutoff_date: str, protocol_version: str = "1.0") -> dict:
    n = len(outcomes)
    by_outcome = {label: 0 for label in
                  ("answered", "partially_addressed", "posed_but_open", "not_addressed")}
    by_premise: dict[str, int] = {}
    support_counts: list[int] = []
    lags: list[int] = []
    sims: list[float] = []
    cutoff_year = int(cutoff_date[:4])

    for o in outcomes:
        by_outcome[o["outcome"]] += 1
        by_premise[o["premise_status"]] = by_premise.get(o["premise_status"], 0) + 1
        bibs = o["supporting_bibcodes"]
        if o["outcome"] != "not_addressed":
            support_counts.append(len(bibs))
        if bibs:
            lags.append(min(bibcode_year(b) for b in bibs) - cutoff_year)
        if o.get("retrieval_top_similarity") is not None:
            sims.append(o["retrieval_top_similarity"])

    engaged = n - by_outcome["not_addressed"]
    return {
        "benchmark_version": benchmark_version,
        "protocol_version": protocol_version,
        "cutoff_date": cutoff_date,
        "n_questions": n,
        "future_attention_rate": _rate(engaged, n),
        "answered_rate": _rate(by_outcome["answered"], n),
        "partial_rate": _rate(by_outcome["partially_addressed"], n),
        "posed_but_open_rate": _rate(by_outcome["posed_but_open"], n),
        "not_addressed_rate": _rate(by_outcome["not_addressed"], n),
        "premise_refutation_rate": _rate(by_premise.get("refuted", 0), n),
        "premise_status_counts": dict(sorted(by_premise.items())),
        "mean_retrieval_support_count":
            round(sum(support_counts) / len(support_counts), 2) if support_counts else 0.0,
        "multi_source_rate":
            _rate(sum(1 for c in support_counts if c >= 2), n),
        "mean_top1_retrieval_similarity":
            round(sum(sims) / len(sims), 4) if sims else None,
        "first_engagement_lag_years": {
            "mean": round(sum(lags) / len(lags), 2),
            "min": min(lags),
            "max": max(lags),
            "note": "lower bound from judge-cited evidence only",
        } if lags else None,
        "mean_lead_time_years": None,
    }


def compute_from_file(annotations_file: str | Path, **kwargs) -> dict:
    return compute_metrics(load_jsonl(annotations_file), **kwargs)


def save_metrics(metrics: dict, out_file: str | Path) -> None:
    Path(out_file).parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False)
        f.write("\n")
