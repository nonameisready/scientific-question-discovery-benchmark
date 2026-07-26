"""The released astronomy v1 data files conform to the benchmark schemas."""

import pytest

from benchmark.schemas import (
    SchemaError,
    bibcode_year,
    validate_file,
    validate_outcome,
    validate_question,
)


def test_released_questions_validate(cfg, root):
    rows = validate_file(root / cfg.questions_file, "question")
    assert len(rows) == 10


def test_released_retrieval_validates(cfg, root):
    rows = validate_file(root / cfg.retrieval_file, "retrieval")
    assert len(rows) == 10
    assert all(r["top_k"] == 8 for r in rows)


def test_released_outcomes_validate(cfg, root):
    rows = validate_file(root / cfg.annotations_file, "outcome")
    assert len(rows) == 10
    assert all(r["adjudication_status"] == "reviewed" for r in rows)


def test_bibcode_year_parsing():
    assert bibcode_year("2021PhDT.........4S") == 2021
    assert bibcode_year("2026ASTCS..1160070G") == 2026
    with pytest.raises(SchemaError):
        bibcode_year("not-a-bibcode")


def test_unfrozen_question_rejected():
    record = {
        "question_id": "q_x", "question": "Is X true?", "domain": "d",
        "cutoff_date": "2020-12-31", "generated_at": "2026-01-01",
        "generation_system": "s", "frozen": False,
    }
    with pytest.raises(SchemaError, match="frozen"):
        validate_question(record)


def test_engaged_outcome_requires_evidence():
    record = {
        "question_id": "q_x", "outcome": "answered", "premise_status": "supported",
        "supporting_bibcodes": [], "rationale": "r", "judge_model": "m",
        "adjudication_status": "reviewed",
    }
    with pytest.raises(SchemaError, match="requires supporting evidence"):
        validate_outcome(record)
