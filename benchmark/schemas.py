"""Record schemas and validators for the benchmark's three core data files.

The benchmark is model-agnostic: any question-discovery system interacts
with it only through these records. All files are JSONL (one record per
line, UTF-8).

  QUESTION    data/questions/*.jsonl        frozen question submissions
  RETRIEVAL   data/retrieval/*.jsonl        future-evidence retrieval runs
  OUTCOME     data/annotations/*.jsonl      outcome labels + premise status

Outcome taxonomy (two independent dimensions — see docs/outcome_taxonomy.md):

  outcome         answered | partially_addressed | posed_but_open | not_addressed
  premise_status  supported | refuted | weakened | still_plausible | not_applicable

Keeping the dimensions separate lets a record express e.g.
outcome=answered AND premise_status=refuted (the question was resolved
*by* the community falsifying its underlying premise).
"""

from __future__ import annotations

import json
import re
from pathlib import Path

OUTCOME_LABELS = ("answered", "partially_addressed", "posed_but_open", "not_addressed")
PREMISE_LABELS = ("supported", "refuted", "weakened", "still_plausible", "not_applicable")

# ADS bibcodes: YYYYJJJJJVVVVMPPPPA (19 chars, year prefix is what we rely on)
BIBCODE_RE = re.compile(r"^\d{4}\S{15}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

QUESTION_REQUIRED = (
    "question_id", "question", "domain", "cutoff_date",
    "generated_at", "generation_system", "frozen",
)
RETRIEVAL_REQUIRED = (
    "question_id", "retrieval_model", "retrieval_corpus_start",
    "retrieval_corpus_end", "top_k", "documents",
)
OUTCOME_REQUIRED = (
    "question_id", "outcome", "premise_status", "supporting_bibcodes",
    "rationale", "judge_model", "adjudication_status",
)


class SchemaError(ValueError):
    """A record does not conform to the benchmark schema."""


def bibcode_year(bibcode: str) -> int:
    if not BIBCODE_RE.match(bibcode or ""):
        raise SchemaError(f"malformed bibcode: {bibcode!r}")
    return int(bibcode[:4])


def _require(record: dict, keys: tuple[str, ...], kind: str) -> None:
    missing = [k for k in keys if k not in record]
    if missing:
        raise SchemaError(f"{kind} record {record.get('question_id')!r} missing {missing}")


def validate_question(record: dict) -> None:
    _require(record, QUESTION_REQUIRED, "question")
    if not DATE_RE.match(record["cutoff_date"]):
        raise SchemaError(f"cutoff_date not YYYY-MM-DD: {record['cutoff_date']!r}")
    if record["frozen"] is not True:
        raise SchemaError(f"{record['question_id']}: questions must be frozen before evaluation")
    if not str(record["question"]).strip().endswith("?"):
        raise SchemaError(f"{record['question_id']}: question text must end with '?'")
    for bib in record.get("source_evidence_ids", []):
        bibcode_year(bib)


def validate_retrieval(record: dict) -> None:
    _require(record, RETRIEVAL_REQUIRED, "retrieval")
    if not isinstance(record["top_k"], int) or record["top_k"] < 1:
        raise SchemaError(f"{record['question_id']}: top_k must be a positive integer")
    for doc in record["documents"]:
        if "bibcode" not in doc:
            raise SchemaError(f"{record['question_id']}: retrieval document missing bibcode")
        bibcode_year(doc["bibcode"])


def validate_outcome(record: dict) -> None:
    _require(record, OUTCOME_REQUIRED, "outcome")
    if record["outcome"] not in OUTCOME_LABELS:
        raise SchemaError(f"{record['question_id']}: unknown outcome {record['outcome']!r}")
    if record["premise_status"] not in PREMISE_LABELS:
        raise SchemaError(
            f"{record['question_id']}: unknown premise_status {record['premise_status']!r}")
    for bib in record["supporting_bibcodes"]:
        bibcode_year(bib)
    if record["outcome"] == "not_addressed" and record["supporting_bibcodes"]:
        raise SchemaError(
            f"{record['question_id']}: not_addressed must not cite supporting evidence")
    if record["outcome"] != "not_addressed" and not record["supporting_bibcodes"]:
        raise SchemaError(
            f"{record['question_id']}: outcome {record['outcome']} requires supporting evidence")


def load_jsonl(path: str | Path) -> list[dict]:
    rows = []
    with open(path, encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise SchemaError(f"{path}:{i}: invalid JSON ({exc})") from exc
    return rows


def write_jsonl(path: str | Path, rows: list[dict]) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def validate_file(path: str | Path, kind: str) -> list[dict]:
    """Validate every record in a JSONL file; returns the records."""
    validator = {
        "question": validate_question,
        "retrieval": validate_retrieval,
        "outcome": validate_outcome,
    }[kind]
    rows = load_jsonl(path)
    seen: set[str] = set()
    for row in rows:
        validator(row)
        qid = row["question_id"]
        if qid in seen:
            raise SchemaError(f"duplicate question_id {qid!r} in {path}")
        seen.add(qid)
    return rows
