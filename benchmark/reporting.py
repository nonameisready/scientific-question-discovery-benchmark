"""Benchmark report generation: per-question CSV, markdown report, and
leaderboard entry."""

from __future__ import annotations

import csv
import json
from pathlib import Path

from .schemas import bibcode_year, load_jsonl


def per_question_rows(questions: list[dict], outcomes: list[dict]) -> list[dict]:
    qmap = {q["question_id"]: q for q in questions}
    rows = []
    for o in sorted(outcomes, key=lambda o: qmap[o["question_id"]].get("rank", 0)):
        q = qmap[o["question_id"]]
        bibs = o["supporting_bibcodes"]
        rows.append({
            "question_id": o["question_id"],
            "rank": q.get("rank", ""),
            "outcome": o["outcome"],
            "premise_status": o["premise_status"],
            "n_supporting_papers": len(bibs),
            "first_evidence_year": min((bibcode_year(b) for b in bibs), default=""),
            "top1_similarity": o.get("retrieval_top_similarity", ""),
            "question": q["question"],
        })
    return rows


def write_csv(rows: list[dict], out_file: str | Path) -> None:
    Path(out_file).parent.mkdir(parents=True, exist_ok=True)
    with open(out_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def build_report(metrics: dict, questions: list[dict], outcomes: list[dict],
                 out_file: str | Path) -> None:
    qmap = {q["question_id"]: q for q in questions}
    lines = [
        f"# Historical Backtesting Report — {metrics['benchmark_version']}",
        "",
        f"Protocol v{metrics['protocol_version']} | cutoff {metrics['cutoff_date']} | "
        f"{metrics['n_questions']} frozen questions",
        "",
        "## Headline metrics",
        "",
        "| Metric | Value |",
        "|---|---|",
        f"| Future attention rate (coverage) | {metrics['future_attention_rate']:.0%} |",
        f"| Answered | {metrics['answered_rate']:.0%} |",
        f"| Partially addressed | {metrics['partial_rate']:.0%} |",
        f"| Posed but open | {metrics['posed_but_open_rate']:.0%} |",
        f"| Not addressed | {metrics['not_addressed_rate']:.0%} |",
        f"| Premise refutation rate | {metrics['premise_refutation_rate']:.0%} |",
        f"| Mean supporting papers per engaged question | {metrics['mean_retrieval_support_count']} |",
        f"| Multi-source evidence rate | {metrics['multi_source_rate']:.0%} |",
        "",
        "## Per-question outcomes",
        "",
    ]
    for o in sorted(outcomes, key=lambda o: qmap[o["question_id"]].get("rank", 0)):
        q = qmap[o["question_id"]]
        lines += [
            f"### rank {q.get('rank', '?')} — {o['question_id']}: "
            f"{o['outcome']} (premise: {o['premise_status']})",
            "",
            f"**{q['question']}**",
            "",
            f"- rationale: {o['rationale']}",
        ]
        for ev in o.get("evidence", []):
            lines.append(f"- [{ev['bibcode']}] {ev['relevance']}")
        lines.append("")
    Path(out_file).parent.mkdir(parents=True, exist_ok=True)
    Path(out_file).write_text("\n".join(lines), encoding="utf-8")


def update_leaderboard(metrics: dict, system_name: str,
                       leaderboard_file: str | Path) -> None:
    path = Path(leaderboard_file)
    board = {"benchmark": "scientific-question-backtesting", "entries": []}
    if path.exists():
        board = json.loads(path.read_text(encoding="utf-8"))
    entry = {
        "system": system_name,
        "benchmark_version": metrics["benchmark_version"],
        "n_questions": metrics["n_questions"],
        "future_attention_rate": metrics["future_attention_rate"],
        "answered_rate": metrics["answered_rate"],
        "premise_refutation_rate": metrics["premise_refutation_rate"],
        "mean_lead_time_years": metrics["mean_lead_time_years"],
    }
    board["entries"] = [e for e in board["entries"]
                        if not (e["system"] == system_name
                                and e["benchmark_version"] == metrics["benchmark_version"])]
    board["entries"].append(entry)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(board, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
