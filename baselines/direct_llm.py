#!/usr/bin/env python3
"""Baseline 2 — direct LLM prompting.

Give an LLM a sample of pre-cutoff abstracts and ask it to propose the
most valuable open research questions. No structured evidence
representation, no tension detection — the strongest "just ask the model"
comparison. Requires OPENAI_API_KEY.

CONTAMINATION NOTE: a modern LLM's training data includes the future
corpus. Direct-LLM baselines therefore measure an *upper* bound that
mixes generation ability with memorized hindsight; the paper's
threats-to-validity section discusses how to read this comparison.

    python baselines/direct_llm.py --corpus data/corpus/past_corpus.jsonl \
        --cutoff 2020-12-31 --domain exoplanet_atmospheres \
        --n 10 --model gpt-4.1 --out submissions/direct_llm_v1
"""

import argparse
import json
import os
import random

from common import load_past_corpus, submission_record, write_submission

API_URL = "https://api.openai.com/v1/chat/completions"

PROMPT = """\
You are given abstracts of scientific papers, all published on or before {cutoff}.
Using ONLY this evidence (do not use knowledge of anything published after
{cutoff}), propose the {n} most valuable open research questions in the domain
"{domain}". Prefer precise, falsifiable questions grounded in specific tensions
or untested assumptions in the provided abstracts.

Return JSON: {{"questions": [{{"question": str, "source_bibcodes": [str]}}]}}
Cite source_bibcodes only from the provided abstracts.
"""


def main() -> None:
    import requests

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", required=True)
    parser.add_argument("--cutoff", required=True)
    parser.add_argument("--domain", required=True)
    parser.add_argument("--n", type=int, default=10)
    parser.add_argument("--sample", type=int, default=60,
                        help="abstracts shown to the model per batch")
    parser.add_argument("--seed", type=int, default=0)
    parser.add_argument("--batches", type=int, default=1,
                        help="split generation into this many calls, each over a "
                             "fresh abstract sample (seed+batch); duplicate "
                             "question texts are dropped")
    parser.add_argument("--model", default="gpt-4.1")
    parser.add_argument("--system-name", default=None,
                        help="override the generation_system string")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    papers = load_past_corpus(args.corpus, args.cutoff)
    system = args.system_name or f"baseline_direct_llm_{args.model}_v1"
    per_batch = -(-args.n // args.batches)  # ceil
    records, seen_questions = [], set()
    for batch in range(args.batches):
        sample = random.Random(args.seed + batch).sample(
            papers, min(args.sample, len(papers)))
        blocks = [f"[{p['paper_id']}] {p['title']}\n{p['abstract'][:1200]}"
                  for p in sample]
        body = {
            "model": args.model,
            "response_format": {"type": "json_object"},
            "temperature": 0,
            "messages": [
                {"role": "system",
                 "content": PROMPT.format(cutoff=args.cutoff, n=per_batch,
                                          domain=args.domain)},
                {"role": "user", "content": "\n\n".join(blocks)},
            ],
        }
        resp = requests.post(
            API_URL, json=body, timeout=300,
            headers={"Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"})
        resp.raise_for_status()
        proposed = json.loads(
            resp.json()["choices"][0]["message"]["content"])["questions"]
        allowed = {p["paper_id"] for p in sample}
        for q in proposed[:per_batch]:
            text = q["question"].strip()
            if text.lower() in seen_questions or len(records) >= args.n:
                continue
            seen_questions.add(text.lower())
            sources = [b for b in q.get("source_bibcodes", []) if b in allowed]
            records.append(submission_record(
                len(records) + 1, text, system, args.cutoff, args.domain, sources))
        if len(records) >= args.n:
            break
    write_submission(args.out, records, system)


if __name__ == "__main__":
    main()
