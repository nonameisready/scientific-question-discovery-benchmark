"""Deterministic specificity rubric (benchmark.specificity)."""

from benchmark.specificity import OUTCOME_WEIGHTS, saf, score_question


def test_broad_question_scores_zero():
    s = score_question("How can we better understand exoplanet atmospheres?")
    assert s["specificity"] == 0


def test_q008_style_question_scores_three():
    s = score_question(
        "Is the strongly subsolar terminator water abundance retrieved for "
        "HD 209458 b a property of the atmosphere or an artifact of retrieval "
        "assumptions, as tested by comparing independent retrieval frameworks?")
    assert s == {"s_object": 1, "s_quantity": 1, "s_test": 1, "specificity": 3}


def test_object_only_scores_one():
    s = score_question("What will JWST reveal about WASP-121 b?")
    assert s["s_object"] == 1
    assert s["s_test"] == 0


def test_saf_weights_outcomes():
    questions = [
        {"question_id": "q_001",
         "question": "Is the subsolar water abundance of HD 209458 b an "
                     "artifact, or an artifact of retrieval assumptions?"},
        {"question_id": "q_002",
         "question": "How can we better understand exoplanet atmospheres?"},
    ]
    outcomes = [
        {"question_id": "q_001", "outcome": "answered"},
        {"question_id": "q_002", "outcome": "answered"},
    ]
    report = saf(questions, outcomes)
    assert report["n"] == 2
    # broad question contributes 0 despite being answered
    contributions = {p["question_id"]: p["saf_contribution"]
                     for p in report["per_question"]}
    assert contributions["q_002"] == 0.0
    assert contributions["q_001"] == 1.0
    assert report["saf"] == 0.5
    assert set(OUTCOME_WEIGHTS) == {
        "answered", "partially_addressed", "posed_but_open", "not_addressed"}
