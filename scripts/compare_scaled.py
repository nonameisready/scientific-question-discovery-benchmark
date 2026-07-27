#!/usr/bin/env python3
"""Compare v1 (n=10) and v1L (scaled) evaluation runs.

    python scripts/compare_scaled.py --out results/astronomy_v1L/comparison.json

Reads the per-run metrics/annotations already on disk (no API access),
computes exact Clopper--Pearson 95% intervals for every rate, and
two-sided Fisher exact tests for the cross-system contrasts the paper
discusses. Pure stdlib: exact binomial/hypergeometric arithmetic.
"""

import argparse
import json
from math import comb
from pathlib import Path


def clopper_pearson(k: int, n: int, alpha: float = 0.05) -> tuple[float, float]:
    """Exact binomial CI via bisection on the beta quantiles' defining sums."""
    if n == 0:
        return (0.0, 1.0)

    def cdf_at_most(k_: int, n_: int, p: float) -> float:
        return sum(comb(n_, i) * p**i * (1 - p) ** (n_ - i) for i in range(k_ + 1))

    def solve(f, lo: float, hi: float) -> float:
        for _ in range(200):
            mid = (lo + hi) / 2
            if f(mid) > 0:
                lo = mid
            else:
                hi = mid
        return (lo + hi) / 2

    lower = 0.0 if k == 0 else solve(
        lambda p: cdf_at_most(k - 1, n, p) - (1 - alpha / 2), 0.0, 1.0)
    upper = 1.0 if k == n else solve(
        lambda p: cdf_at_most(k, n, p) - alpha / 2, 0.0, 1.0)
    return (round(lower, 4), round(upper, 4))


def fisher_two_sided(k1: int, n1: int, k2: int, n2: int) -> float:
    """Two-sided Fisher exact test on [[k1, n1-k1], [k2, n2-k2]]."""
    total, successes = n1 + n2, k1 + k2
    denom = comb(total, n1)

    def p_table(x: int) -> float:
        return comb(successes, x) * comb(total - successes, n1 - x) / denom

    lo = max(0, successes - (total - n1))
    hi = min(successes, n1)
    observed = p_table(k1)
    p = sum(p_table(x) for x in range(lo, hi + 1)
            if p_table(x) <= observed * (1 + 1e-9))
    return round(min(1.0, p), 5)


def counts(annotations_file: str) -> dict:
    rows = [json.loads(line) for line in open(annotations_file, encoding="utf-8")]
    n = len(rows)
    outcome = {label: sum(1 for r in rows if r["outcome"] == label)
               for label in ("answered", "partially_addressed",
                             "posed_but_open", "not_addressed")}
    premise = {label: sum(1 for r in rows if r["premise_status"] == label)
               for label in ("supported", "refuted", "weakened",
                             "still_plausible", "not_applicable")}
    return {"n": n, "outcome": outcome, "premise": premise,
            "engaged": n - outcome["not_addressed"]}


RUNS = {
    "v1": {
        "evidence_graph_adjudicated": "data/annotations/outcomes_v1.jsonl",
        "evidence_graph_judge_only": "data/annotations/outcomes_evidence_graph_rebuilt_v1.jsonl",
        "random_claim": "data/annotations/outcomes_random_claim_v1.jsonl",
        "review_future_work": "data/annotations/outcomes_review_future_work_v1.jsonl",
        "citation_leader": "data/annotations/outcomes_citation_leader_v1.jsonl",
        "direct_llm": "data/annotations/outcomes_direct_llm_v1.jsonl",
    },
    "v1L": {
        "evidence_graph_judge_only": "data/annotations/outcomes_evidence_graph_10_L.jsonl",
        "random_claim": "data/annotations/outcomes_random_claim_L.jsonl",
        "review_future_work": "data/annotations/outcomes_review_future_work_L.jsonl",
        "citation_leader": "data/annotations/outcomes_citation_leader_L.jsonl",
        "direct_llm": "data/annotations/outcomes_direct_llm_L.jsonl",
    },
}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="results/astronomy_v1L/comparison.json")
    args = parser.parse_args()

    report: dict = {"instances": {}, "contrasts": {}}
    for instance, runs in RUNS.items():
        report["instances"][instance] = {}
        for system, path in runs.items():
            if not Path(path).exists():
                continue
            c = counts(path)
            n = c["n"]
            rates = {}
            for name, k in (("engaged", c["engaged"]),
                            ("answered", c["outcome"]["answered"]),
                            ("posed_but_open", c["outcome"]["posed_but_open"]),
                            ("refuted", c["premise"]["refuted"])):
                rates[name] = {"k": k, "n": n, "rate": round(k / n, 4),
                               "ci95": clopper_pearson(k, n)}
            report["instances"][instance][system] = rates

    L = report["instances"].get("v1L", {})

    def contrast(name: str, sys1: str, sys2: str, metric: str) -> None:
        if sys1 not in L or sys2 not in L:
            return
        a, b = L[sys1][metric], L[sys2][metric]
        report["contrasts"][name] = {
            "metric": metric,
            sys1: f"{a['k']}/{a['n']}", sys2: f"{b['k']}/{b['n']}",
            "fisher_p_two_sided": fisher_two_sided(a["k"], a["n"], b["k"], b["n"]),
        }

    contrast("random_vs_direct_llm_engagement", "random_claim", "direct_llm", "engaged")
    contrast("random_vs_citation_leader_engagement", "random_claim",
             "citation_leader", "engaged")
    contrast("citation_leader_vs_direct_llm_answered", "citation_leader",
             "direct_llm", "answered")
    contrast("citation_leader_vs_random_answered", "citation_leader",
             "random_claim", "answered")
    contrast("citation_leader_vs_random_refuted", "citation_leader",
             "random_claim", "refuted")

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
    print(f"OK -> {args.out}")
    for instance, systems in report["instances"].items():
        for system, rates in systems.items():
            summary = ", ".join(
                f"{m} {v['k']}/{v['n']} {v['ci95']}" for m, v in rates.items())
            print(f"  [{instance}] {system}: {summary}")
    for name, c in report["contrasts"].items():
        print(f"  contrast {name}: p={c['fisher_p_two_sided']}")


if __name__ == "__main__":
    main()
