"""End-to-end temporal-isolation audit of the released instance."""

import pytest

from benchmark.leakage import (
    LeakageError,
    check_citation_containment,
    check_future_window,
    check_id_alignment,
    run_all_checks,
)


def test_full_release_passes_all_checks(cfg, root):
    run_all_checks(root / cfg.questions_file, root / cfg.retrieval_file,
                   root / cfg.annotations_file, root / cfg.future_corpus_manifest,
                   cfg.cutoff_date)


def test_future_window_starts_after_cutoff(cfg, root):
    check_future_window(root / cfg.future_corpus_manifest, cfg.cutoff_date)
    with pytest.raises(LeakageError):
        check_future_window(root / cfg.future_corpus_manifest, "2021-12-31")


def test_stray_judge_citation_detected():
    retrieval = [{"question_id": "a",
                  "documents": [{"bibcode": "2022ApJ...900...12X"}]}]
    outcomes = [{"question_id": "a",
                 "supporting_bibcodes": ["2023MNRAS.500...1Z"]}]
    with pytest.raises(LeakageError, match="outside the retrieved"):
        check_citation_containment(retrieval, outcomes)


def test_unknown_question_id_detected():
    with pytest.raises(LeakageError, match="unknown question_ids"):
        check_id_alignment(
            [{"question_id": "a"}],
            [{"question_id": "a"}],
            [{"question_id": "b"}])


def test_ids_aligned_across_release(questions, retrieval, outcomes):
    qids = {q["question_id"] for q in questions}
    assert {r["question_id"] for r in retrieval} == qids
    assert {o["question_id"] for o in outcomes} == qids
