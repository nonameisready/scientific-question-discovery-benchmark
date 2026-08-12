#!/usr/bin/env python3
"""Translate the annotation packet's questions and abstracts into Chinese.

    python scripts/translate_packet.py

The English originals are never replaced — the form shows both, because
the LLM judge read the English text and the human annotator must be
looking at the same material for the comparison to mean anything. The
Chinese is a reading aid.

Translations are cached in annotation/translations.json keyed by a stable
id (question text hash / bibcode), so re-runs cost nothing and the packet
can be rebuilt reproducibly. Requires OPENAI_API_KEY.
"""

import argparse
import hashlib
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark.schemas import load_jsonl  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
PACK = ROOT / "annotation"
SAMPLE = ROOT / "results" / "judge_validation" / "sample.json"
CORPUS = ROOT / "data" / "corpus" / "future_corpus_large_frozen_window.jsonl"
CACHE = PACK / "translations.json"
API_URL = "https://api.openai.com/v1/chat/completions"

PROMPT = """\
You translate astronomy paper abstracts and research questions from English
into simplified Chinese for a domain expert who is annotating them.

Rules:
- Translate faithfully and completely; do not summarise, omit, or add.
- Keep object names, instrument names, molecular formulae, numbers, units and
  statistical terms in their original form (HD 209458 b, JWST, H2O, C/O, 3.5
  sigma, ppm). Do not transliterate them.
- Standard field terms: transmission spectroscopy 透射光谱, emission
  spectroscopy 发射光谱, retrieval 检索/反演, terminator 晨昏线, hot Jupiter
  热木星, atmospheric escape 大气逃逸, phase curve 相位曲线, upper limit 上限,
  non-detection 未探测到, abundance 丰度, metallicity 金属丰度.
- Keep it readable: plain scientific Chinese, no flowery language.

You receive a JSON array of {id, text}. Return JSON:
{"items": [{"id": <same id>, "zh": "<translation>"}]}
Translate every item you are given.
"""


def _sid(text: str) -> str:
    return "q_" + hashlib.sha1(text.encode("utf-8")).hexdigest()[:12]


def collect() -> dict[str, str]:
    """id -> English text, for every question and unique abstract."""
    sample = json.loads(SAMPLE.read_text(encoding="utf-8"))
    papers = {p["paper_id"]: p for p in load_jsonl(CORPUS)}
    todo: dict[str, str] = {}
    for name, spec in sample.items():
        questions = {q["question_id"]: q["question"]
                     for q in load_jsonl(ROOT / spec["questions_file"])}
        retrieval = {r["question_id"]: r["documents"]
                     for r in load_jsonl(ROOT / spec["retrieval_file"])}
        for qid in spec["question_ids"]:
            todo[_sid(questions[qid])] = questions[qid]
            for d in retrieval[qid]:
                paper = papers.get(d["bibcode"])
                if not paper:
                    continue
                todo[f"t:{d['bibcode']}"] = paper.get("title") or ""
                todo[f"a:{d['bibcode']}"] = paper.get("abstract") or ""
    return {k: v for k, v in todo.items() if v.strip()}


def translate(batch: list[tuple[str, str]], model: str) -> dict[str, str]:
    import requests

    payload = [{"id": i, "text": t} for i, t in batch]
    body = {
        "model": model,
        "response_format": {"type": "json_object"},
        "temperature": 0,
        "messages": [{"role": "system", "content": PROMPT},
                     {"role": "user", "content": json.dumps(payload, ensure_ascii=False)}],
    }
    headers = {"Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
               "Content-Type": "application/json"}
    for attempt in range(4):
        resp = requests.post(API_URL, headers=headers, json=body, timeout=300)
        if resp.status_code == 429 or resp.status_code >= 500:
            time.sleep(2 ** (attempt + 1))
            continue
        resp.raise_for_status()
        items = json.loads(resp.json()["choices"][0]["message"]["content"])["items"]
        return {it["id"]: it["zh"] for it in items if it.get("zh")}
    resp.raise_for_status()
    return {}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", default="gpt-4.1")
    parser.add_argument("--batch-chars", type=int, default=9000,
                        help="approximate English characters per API call")
    args = parser.parse_args()

    todo = collect()
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    pending = [(k, v) for k, v in sorted(todo.items()) if k not in cache]
    print(f"{len(todo)} strings total, {len(cache)} cached, {len(pending)} to translate")

    batch: list[tuple[str, str]] = []
    size = 0
    done = 0
    for key, text in pending:
        batch.append((key, text))
        size += len(text)
        if size >= args.batch_chars:
            cache.update(translate(batch, args.model))
            done += len(batch)
            CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1),
                             encoding="utf-8")
            print(f"  {done}/{len(pending)} translated")
            batch, size = [], 0
    if batch:
        cache.update(translate(batch, args.model))
        done += len(batch)
    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")
    missing = [k for k in todo if k not in cache]
    print(f"OK: {len(cache)} translations cached -> {CACHE}"
          + (f" ({len(missing)} still missing)" if missing else ""))


if __name__ == "__main__":
    main()
