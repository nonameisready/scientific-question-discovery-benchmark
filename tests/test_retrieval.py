"""Retrieval records: future-only documents, citation containment,
and cosine-similarity sanity."""

from benchmark.leakage import check_citation_containment, check_future_documents
from benchmark.retrieval import cosine
from benchmark.schemas import bibcode_year


def test_retrieved_documents_are_post_cutoff(retrieval, cfg):
    check_future_documents(retrieval, cfg.cutoff_date)
    for r in retrieval:
        for doc in r["documents"]:
            assert bibcode_year(doc["bibcode"]) >= 2021


def test_judge_citations_within_retrieved_candidates(retrieval, outcomes):
    check_citation_containment(retrieval, outcomes)


def test_retrieval_window_is_post_cutoff(retrieval, cfg):
    for r in retrieval:
        assert r["retrieval_corpus_start"] > cfg.cutoff_date


def test_top1_similarity_recorded_and_sane(retrieval):
    for r in retrieval:
        assert 0.0 < r["top1_similarity"] < 1.0


def test_cosine():
    assert cosine([1, 0], [1, 0]) == 1.0
    assert cosine([1, 0], [0, 1]) == 0.0
    assert cosine([0, 0], [1, 1]) == 0.0
