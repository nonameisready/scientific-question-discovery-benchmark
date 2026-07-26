"""Shared helpers for baseline question generators.

Every baseline consumes only pre-cutoff corpus records
({paper_id, title, abstract, pubdate, [citation_count]}) and writes a
frozen submission in the benchmark's question format.
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark.schemas import bibcode_year, load_jsonl, write_jsonl  # noqa: E402


def load_past_corpus(path: str | Path, cutoff_date: str) -> list[dict]:
    """Load a corpus file and hard-fail on any post-cutoff record."""
    cutoff_year = int(cutoff_date[:4])
    papers = load_jsonl(path)
    for p in papers:
        if bibcode_year(p["paper_id"]) > cutoff_year:
            raise SystemExit(
                f"leakage: {p['paper_id']} postdates cutoff {cutoff_date}; "
                "baselines may only read the past corpus")
    return papers


def submission_record(i: int, question: str, system: str, cutoff_date: str,
                      domain: str, source_ids: list[str]) -> dict:
    return {
        "question_id": f"q_{i:03d}",
        "question": question,
        "domain": domain,
        "cutoff_date": cutoff_date,
        "generated_at": date.today().isoformat(),
        "generation_system": system,
        "source_evidence_ids": source_ids,
        "rank": i,
        "frozen": True,
    }


def write_submission(out_dir: str | Path, records: list[dict], system: str) -> None:
    out = Path(out_dir)
    write_jsonl(out / "questions.jsonl", records)
    print(f"OK: {len(records)} frozen questions -> {out / 'questions.jsonl'} "
          f"(system: {system}); validate with scripts/validate_cutoff.py before evaluation")
