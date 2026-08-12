#!/usr/bin/env python3
"""Temporal contamination stress test.

Runs the same four generators (direct_llm, random_claim, tension_llm,
tension_template) at four historical cutoffs with uniform 4-year future
windows (the 2024 window is censored at 2026-06 and flagged), then
evaluates every submission through the standard pipeline. If a modern
LLM's backtest performance comes from memorized future literature, its
margin over the weight-free generators should collapse for the cutoff
that postdates its training data; a generator that only verbalizes
pre-cutoff evidence structure should degrade far less.

    python scripts/stress_test.py            # run everything (resumable)
    python scripts/stress_test.py --summary  # just print the summary table

Every stage skips work whose output file already exists, so the script
is safe to re-run after interruptions. Requires OPENAI_API_KEY for
generation (direct/tension_llm), retrieval, and judging.
"""

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark.judging import judge_all  # noqa: E402
from benchmark.retrieval import retrieve  # noqa: E402
from benchmark.schemas import load_jsonl  # noqa: E402
from benchmark.specificity import saf  # noqa: E402

CUTOFFS = {
    "c2010": {"cutoff": "2010-12-31", "window": ("2011-01-01", "2014-12-31")},
    "c2015": {"cutoff": "2015-12-31", "window": ("2016-01-01", "2019-12-31")},
    "c2020": {"cutoff": "2020-12-31", "window": ("2021-01-01", "2024-12-31")},
    "c2024": {"cutoff": "2024-12-31", "window": ("2025-01-01", "2026-06-30"),
              "censored": True},
}
GENERATORS = ["direct_llm", "random_claim", "tension_llm", "tension_template"]
N = 50
DOMAIN = "exoplanet_atmospheres"
ROOT = Path(__file__).resolve().parents[1]


def generate(tag: str, gen: str) -> Path:
    out_dir = ROOT / "submissions" / "stress" / f"{tag}_{gen}"
    questions = out_dir / "questions.jsonl"
    if questions.exists():
        return questions
    corpus = ROOT / "data" / "corpus" / f"stress_{tag}_past.jsonl"
    cutoff = CUTOFFS[tag]["cutoff"]
    base = ["--corpus", str(corpus), "--cutoff", cutoff,
            "--domain", DOMAIN, "--n", str(N), "--out", str(out_dir)]
    if gen == "direct_llm":
        cmd = ["direct_llm.py", "--batches", "2", "--seed", "0",
               "--model", "gpt-4.1"] + base
    elif gen == "random_claim":
        cmd = ["random_claim.py", "--seed", "0"] + base
    elif gen == "tension_llm":
        cmd = ["tension_pair.py", "--mode", "llm", "--model", "gpt-4.1"] + base
    else:
        cmd = ["tension_pair.py", "--mode", "template"] + base
    subprocess.run([sys.executable, cmd[0], *cmd[1:]],
                   cwd=ROOT / "baselines", check=True)
    return questions


def evaluate(tag: str, gen: str, questions: Path) -> dict:
    window = CUTOFFS[tag]["window"]
    future = ROOT / "data" / "corpus" / f"stress_{tag}_future.jsonl"
    retrieval_file = ROOT / "data" / "retrieval" / "stress" / f"{tag}_{gen}_top8.jsonl"
    annotations = ROOT / "data" / "annotations" / "stress" / f"{tag}_{gen}.jsonl"
    retrieval_file.parent.mkdir(parents=True, exist_ok=True)
    annotations.parent.mkdir(parents=True, exist_ok=True)
    if not retrieval_file.exists():
        retrieve(questions, future, retrieval_file, corpus_id=f"stress_{tag}_future",
                 corpus_start=window[0], corpus_end=window[1])
    if not annotations.exists():
        judge_all(questions, retrieval_file, future, annotations)
    qs, outs = load_jsonl(questions), load_jsonl(annotations)
    n = len(outs)
    engaged = sum(1 for o in outs if o["outcome"] != "not_addressed")
    answered = sum(1 for o in outs if o["outcome"] == "answered")
    refuted = sum(1 for o in outs if o["premise_status"] == "refuted")
    sims = [r["top1_similarity"] for r in load_jsonl(retrieval_file)]
    spec = saf(qs, outs)
    return {
        "n": n, "engaged": engaged, "answered": answered, "refuted": refuted,
        "engaged_rate": round(engaged / n, 4), "answered_rate": round(answered / n, 4),
        "mean_top1_similarity": round(sum(sims) / len(sims), 4),
        "mean_specificity": spec["mean_specificity"],
        "saf": spec["saf"],
        "censored_window": CUTOFFS[tag].get("censored", False),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--summary", action="store_true",
                        help="print existing summary without running anything")
    parser.add_argument("--only", choices=list(CUTOFFS), default=None,
                        help="run a single cutoff (writes summary_<tag>.json); "
                             "a later full run merges the per-tag files")
    parser.add_argument("--out", default="results/stress/summary.json")
    args = parser.parse_args()
    out_path = ROOT / args.out
    if args.summary:
        summary = json.loads(out_path.read_text(encoding="utf-8"))
    else:
        tags = [args.only] if args.only else list(CUTOFFS)
        summary = {}
        for tag in tags:
            per_tag = out_path.parent / f"summary_{tag}.json"
            if not args.only and per_tag.exists():
                summary[tag] = json.loads(per_tag.read_text(encoding="utf-8"))
                continue
            summary[tag] = {"cutoff": CUTOFFS[tag]["cutoff"],
                            "window": CUTOFFS[tag]["window"]}
            for gen in GENERATORS:
                print(f"== {tag} / {gen}")
                questions = generate(tag, gen)
                summary[tag][gen] = evaluate(tag, gen, questions)
                print(f"   {summary[tag][gen]}")
            per_tag.parent.mkdir(parents=True, exist_ok=True)
            per_tag.write_text(json.dumps(summary[tag], indent=2,
                                          ensure_ascii=False), encoding="utf-8")
        if not args.only:
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(json.dumps(summary, indent=2, ensure_ascii=False),
                                encoding="utf-8")
            print(f"OK -> {out_path}")
    header = f"{'cutoff':8s} {'generator':18s} {'n':>4} {'eng':>6} {'ans':>6} {'ref':>4} {'sim':>7} {'spec':>5} {'saf':>6}"
    print(header)
    for tag, row in summary.items():
        for gen in GENERATORS:
            if gen not in row:
                continue
            g = row[gen]
            print(f"{tag:8s} {gen:18s} {g['n']:>4} {g['engaged_rate']:>6.0%} "
                  f"{g['answered_rate']:>6.0%} {g['refuted']:>4} "
                  f"{g['mean_top1_similarity']:>7.3f} {g['mean_specificity']:>5.2f} "
                  f"{g['saf']:>6.3f}")


if __name__ == "__main__":
    main()
