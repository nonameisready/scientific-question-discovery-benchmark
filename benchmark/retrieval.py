"""Future-evidence retrieval: embed frozen questions and future-corpus
abstracts, return the top-k most similar post-cutoff papers per question.

Retrieval is deliberately simple and fully specified so that benchmark
instances are comparable: cosine similarity between OpenAI
text-embedding-3-small vectors of the question text and of
"title + abstract" (truncated to 6,000 characters), top-k = 8 by default.

Requires OPENAI_API_KEY and a future-corpus JSONL of
{paper_id, title, abstract, pubdate} records. The astronomy v1 corpus is
rebuilt from its manifest with scripts/prepare_corpus.py (ADS API).
"""

from __future__ import annotations

import math
import os
import time
from pathlib import Path

from .schemas import load_jsonl, write_jsonl

EMBEDDINGS_URL = "https://api.openai.com/v1/embeddings"
BATCH = 256


def cosine(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    return dot / (na * nb) if na and nb else 0.0


def embed(texts: list[str], model: str) -> list[list[float]]:
    import requests  # runtime dependency only for live retrieval

    headers = {
        "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
        "Content-Type": "application/json",
    }
    vectors: list[list[float]] = []
    for start in range(0, len(texts), BATCH):
        batch = texts[start:start + BATCH]
        for attempt in range(4):
            resp = requests.post(EMBEDDINGS_URL, headers=headers,
                                 json={"model": model, "input": batch}, timeout=120)
            if resp.status_code == 429 or resp.status_code >= 500:
                time.sleep(2 ** (attempt + 1))
                continue
            resp.raise_for_status()
            vectors.extend(item["embedding"] for item in resp.json()["data"])
            break
        else:
            resp.raise_for_status()
    return vectors


def retrieve(questions_file: str | Path, corpus_file: str | Path,
             out_file: str | Path, *, model: str = "text-embedding-3-small",
             top_k: int = 8, corpus_id: str = "", corpus_start: str = "",
             corpus_end: str = "") -> list[dict]:
    """Run top-k retrieval for every frozen question and write the
    retrieval records (with per-document scores) to out_file."""
    questions = load_jsonl(questions_file)
    papers = load_jsonl(corpus_file)
    paper_vecs = embed(
        [f"{p.get('title', '')} {p.get('abstract', '')}"[:6000] for p in papers], model)
    question_vecs = embed([q["question"] for q in questions], model)

    records = []
    for q, qv in zip(questions, question_vecs):
        sims = sorted(
            ((cosine(qv, pv), p) for pv, p in zip(paper_vecs, papers)),
            key=lambda t: -t[0])
        records.append({
            "question_id": q["question_id"],
            "retrieval_model": model,
            "retrieval_corpus": corpus_id,
            "retrieval_corpus_start": corpus_start,
            "retrieval_corpus_end": corpus_end,
            "top_k": top_k,
            "top1_similarity": round(sims[0][0], 4) if sims else None,
            "documents": [
                {"rank": i + 1, "bibcode": p["paper_id"], "score": round(s, 4)}
                for i, (s, p) in enumerate(sims[:top_k])
            ],
        })
    write_jsonl(out_file, records)
    return records
