"""Constrained outcome judging with citation validation.

An LLM judge reads a frozen question plus its top-k retrieved future
abstracts and emits a two-dimensional label:

  outcome         answered | partially_addressed | posed_but_open | not_addressed
  premise_status  supported | refuted | weakened | still_plausible | not_applicable

Constraints enforced *outside* the model:
  - the judge may cite only bibcodes from the provided candidates
    (violations raise, they are never silently dropped);
  - unknown labels fall back to the most conservative value
    (not_addressed / not_applicable) and are flagged for adjudication;
  - every record carries judge_model and judge_protocol so runs are
    comparable and never silently overwritten.

Judged labels are drafts: the release pipeline requires human
adjudication (data/annotations/adjudication_*.jsonl) before results are
published. See docs/annotation_guidelines.md.
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path

from .schemas import OUTCOME_LABELS, PREMISE_LABELS, load_jsonl, write_jsonl

API_URL = "https://api.openai.com/v1/chat/completions"
JUDGE_PROTOCOL = "sqb-v1"

JUDGE_PROMPT = """\
You judge whether post-cutoff scientific literature engaged with a research
question that was generated from pre-cutoff evidence only.

You get the question and candidate abstracts (each with a bibcode). Assign
TWO independent labels.

outcome — did future science engage the question?
  answered              the literature substantially resolved it (state the resolution)
  partially_addressed   substantial directly-relevant progress; core question open
  posed_but_open        the literature independently poses essentially the same
                        question without resolving it
  not_addressed         none of the abstracts engage the question substantively

premise_status — what happened to the question's underlying premise?
  supported        future evidence confirms the premise
  refuted          future evidence falsifies the premise
  weakened         future evidence casts substantial doubt without falsifying
  still_plausible  the premise was not directly tested
  not_applicable   the question does not rest on a contestable premise

Rules:
- Cite ONLY bibcodes from the provided candidates; never invent evidence.
- Similar topic is not engagement: the abstract must bear on the question's
  actual test or premise.
- A question can be answered *because* its premise was refuted; use
  outcome=answered, premise_status=refuted in that case.

Return JSON:
  outcome            one of the four outcome labels
  premise_status     one of the five premise labels
  evidence           [{bibcode, relevance: one sentence}] max 5, may be empty
  rationale          two sentences: what the post-cutoff literature did
"""


class CitationError(ValueError):
    """The judge cited a bibcode outside the retrieved candidates."""


def _call_judge(model: str, question: str, candidates: list[dict]) -> dict:
    import requests  # runtime dependency only for live judging

    headers = {
        "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
        "Content-Type": "application/json",
    }
    blocks = [
        f"[{c['paper_id']}] ({c.get('pubdate', '')}) {c.get('title', '')}\n"
        f"{(c.get('abstract') or '')[:1500]}"
        for c in candidates
    ]
    body = {
        "model": model,
        "response_format": {"type": "json_object"},
        "temperature": 0,
        "messages": [
            {"role": "system", "content": JUDGE_PROMPT},
            {"role": "user", "content":
                f"Question (generated from pre-cutoff evidence): {question}\n\n"
                "Candidate post-cutoff abstracts:\n\n" + "\n\n".join(blocks)},
        ],
    }
    for attempt in range(4):
        resp = requests.post(API_URL, headers=headers, json=body, timeout=180)
        if resp.status_code == 429 or resp.status_code >= 500:
            time.sleep(2 ** (attempt + 1))
            continue
        resp.raise_for_status()
        return json.loads(resp.json()["choices"][0]["message"]["content"])
    resp.raise_for_status()
    return {}


def constrain(judged: dict, allowed_bibcodes: set[str], question_id: str) -> dict:
    """Validate a raw judge response against the benchmark constraints."""
    outcome = judged.get("outcome")
    premise = judged.get("premise_status")
    flagged = False
    if outcome not in OUTCOME_LABELS:
        outcome, flagged = "not_addressed", True
    if premise not in PREMISE_LABELS:
        premise, flagged = "not_applicable", True
    evidence = judged.get("evidence") or []
    stray = [e.get("bibcode") for e in evidence if e.get("bibcode") not in allowed_bibcodes]
    if stray:
        raise CitationError(f"{question_id}: judge cited non-candidate bibcodes {stray}")
    if outcome == "not_addressed" and evidence:
        # A judge that cites evidence while declaring non-engagement is
        # contradicting itself. Resolve conservatively: keep the weaker
        # outcome, drop the citations, and force human review.
        evidence, flagged = [], True
    return {
        "question_id": question_id,
        "outcome": outcome,
        "premise_status": premise,
        "supporting_bibcodes": [e["bibcode"] for e in evidence],
        "evidence": evidence,
        "rationale": judged.get("rationale", ""),
        "adjudication_status": "needs_review" if flagged else "unreviewed",
    }


def judge_all(questions_file: str | Path, retrieval_file: str | Path,
              corpus_file: str | Path, out_file: str | Path,
              *, model: str = "gpt-4.1") -> list[dict]:
    questions = {q["question_id"]: q for q in load_jsonl(questions_file)}
    papers = {p["paper_id"]: p for p in load_jsonl(corpus_file)}
    records = []
    for r in load_jsonl(retrieval_file):
        qid = r["question_id"]
        candidates = [papers[d["bibcode"]] for d in r["documents"] if d["bibcode"] in papers]
        raw = _call_judge(model, questions[qid]["question"], candidates)
        record = constrain(raw, {d["bibcode"] for d in r["documents"]}, qid)
        record.update({
            "retrieval_top_similarity": r.get("top1_similarity"),
            "judge_model": model,
            "judge_protocol": JUDGE_PROTOCOL,
        })
        records.append(record)
        time.sleep(0.4)
    write_jsonl(out_file, records)
    return records
