"""Constraint enforcement on raw judge responses (benchmark.judging.constrain)."""

import pytest

from benchmark.judging import CitationError, constrain

ALLOWED = {"2022ApJ...111....1A", "2023A&A...222....2B"}


def _raw(**overrides):
    raw = {
        "outcome": "partially_addressed",
        "premise_status": "supported",
        "evidence": [{"bibcode": "2022ApJ...111....1A", "relevance": "tests the premise"}],
        "rationale": "Direct follow-up observations.",
    }
    raw.update(overrides)
    return raw


def test_valid_response_passes_through():
    rec = constrain(_raw(), ALLOWED, "q_001")
    assert rec["outcome"] == "partially_addressed"
    assert rec["supporting_bibcodes"] == ["2022ApJ...111....1A"]
    assert rec["adjudication_status"] == "unreviewed"


def test_unknown_labels_degrade_conservatively_and_flag():
    rec = constrain(_raw(outcome="solved", premise_status="proven", evidence=[]),
                    ALLOWED, "q_001")
    assert rec["outcome"] == "not_addressed"
    assert rec["premise_status"] == "not_applicable"
    assert rec["adjudication_status"] == "needs_review"


def test_stray_citation_raises():
    bad = _raw(evidence=[{"bibcode": "2024Natur.999....9Z", "relevance": "invented"}])
    with pytest.raises(CitationError):
        constrain(bad, ALLOWED, "q_001")


def test_not_addressed_with_citations_drops_evidence_and_flags():
    contradictory = _raw(outcome="not_addressed")
    rec = constrain(contradictory, ALLOWED, "q_001")
    assert rec["outcome"] == "not_addressed"
    assert rec["supporting_bibcodes"] == []
    assert rec["evidence"] == []
    assert rec["adjudication_status"] == "needs_review"


def test_second_attempt_strips_and_logs_stray_citations():
    bad = _raw(evidence=[
        {"bibcode": "2024Natur.999....9Z", "relevance": "invented"},
        {"bibcode": "2022ApJ...111....1A", "relevance": "real candidate"},
    ])
    bad["_strip_stray_citations"] = True
    rec = constrain(bad, ALLOWED, "q_001")
    assert rec["supporting_bibcodes"] == ["2022ApJ...111....1A"]
    assert rec["citation_violations"] == ["2024Natur.999....9Z"]
    assert rec["adjudication_status"] == "needs_review"
