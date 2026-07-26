"""Temporal-isolation (leakage) checks.

The protocol's validity rests on strict separation between what a system
saw (the past corpus, up to the cutoff) and what it is judged against
(the future corpus, strictly after the cutoff). These checks are run in
CI on every change to the released data.

  1. Every question's cutoff_date matches the benchmark instance cutoff.
  2. Every source_evidence_id predates or equals the cutoff year.
  3. Every retrieved / judge-cited document postdates the cutoff year.
  4. Judge-cited bibcodes are a subset of the retrieved candidates.
  5. question_ids are unique and consistent across the three files.
  6. The future-corpus window starts after the cutoff.
"""

from __future__ import annotations

import json
from pathlib import Path

from .schemas import bibcode_year, load_jsonl


class LeakageError(ValueError):
    """A temporal-isolation rule was violated."""


def cutoff_year(cutoff_date: str) -> int:
    return int(cutoff_date[:4])


def check_question_cutoffs(questions: list[dict], cutoff_date: str) -> None:
    year = cutoff_year(cutoff_date)
    for q in questions:
        if q["cutoff_date"] != cutoff_date:
            raise LeakageError(
                f"{q['question_id']}: cutoff_date {q['cutoff_date']} != instance cutoff {cutoff_date}")
        for bib in q.get("source_evidence_ids", []):
            if bibcode_year(bib) > year:
                raise LeakageError(
                    f"{q['question_id']}: source evidence {bib} postdates cutoff {cutoff_date}")


def check_future_documents(retrieval: list[dict], cutoff_date: str) -> None:
    year = cutoff_year(cutoff_date)
    for r in retrieval:
        for doc in r["documents"]:
            if bibcode_year(doc["bibcode"]) <= year:
                raise LeakageError(
                    f"{r['question_id']}: retrieved document {doc['bibcode']} "
                    f"is not strictly after cutoff {cutoff_date}")


def check_citation_containment(retrieval: list[dict], outcomes: list[dict]) -> None:
    retrieved = {r["question_id"]: {d["bibcode"] for d in r["documents"]} for r in retrieval}
    for o in outcomes:
        pool = retrieved.get(o["question_id"])
        if pool is None:
            raise LeakageError(f"{o['question_id']}: outcome has no retrieval record")
        stray = [b for b in o["supporting_bibcodes"] if b not in pool]
        if stray:
            raise LeakageError(
                f"{o['question_id']}: judge cited bibcodes outside the retrieved "
                f"candidates: {stray}")


def check_id_alignment(questions: list[dict], retrieval: list[dict],
                       outcomes: list[dict]) -> None:
    qids = [q["question_id"] for q in questions]
    if len(qids) != len(set(qids)):
        raise LeakageError("duplicate question_ids in questions file")
    qset = set(qids)
    for name, rows in (("retrieval", retrieval), ("outcomes", outcomes)):
        extra = {r["question_id"] for r in rows} - qset
        if extra:
            raise LeakageError(f"{name} file references unknown question_ids: {sorted(extra)}")


def check_future_window(manifest_path: str | Path, cutoff_date: str) -> None:
    with open(manifest_path, encoding="utf-8") as f:
        manifest = json.load(f)
    window = manifest["validation_window"]
    if int(window["min"]) <= cutoff_year(cutoff_date):
        raise LeakageError(
            f"future corpus window starts {window['min']}, not after cutoff {cutoff_date}")


def run_all_checks(questions_file: str | Path, retrieval_file: str | Path,
                   annotations_file: str | Path, future_manifest: str | Path,
                   cutoff_date: str) -> None:
    questions = load_jsonl(questions_file)
    retrieval = load_jsonl(retrieval_file)
    outcomes = load_jsonl(annotations_file)
    check_question_cutoffs(questions, cutoff_date)
    check_future_documents(retrieval, cutoff_date)
    check_citation_containment(retrieval, outcomes)
    check_id_alignment(questions, retrieval, outcomes)
    check_future_window(future_manifest, cutoff_date)
