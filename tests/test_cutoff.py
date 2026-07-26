"""Temporal-isolation checks on the released questions."""

import pytest

from benchmark.leakage import LeakageError, check_question_cutoffs
from benchmark.schemas import bibcode_year


def test_all_questions_use_instance_cutoff(questions, cfg):
    check_question_cutoffs(questions, cfg.cutoff_date)


def test_all_source_evidence_predates_cutoff(questions, cfg):
    cutoff_year = int(cfg.cutoff_date[:4])
    for q in questions:
        assert q["source_evidence_ids"], q["question_id"]
        for bib in q["source_evidence_ids"]:
            assert bibcode_year(bib) <= cutoff_year, (q["question_id"], bib)


def test_post_cutoff_source_evidence_rejected(cfg):
    bad = [{
        "question_id": "q_bad", "cutoff_date": cfg.cutoff_date,
        "source_evidence_ids": ["2023ApJ...900...10X"],
    }]
    with pytest.raises(LeakageError, match="postdates cutoff"):
        check_question_cutoffs(bad, cfg.cutoff_date)


def test_all_questions_frozen(questions):
    assert all(q["frozen"] is True for q in questions)
