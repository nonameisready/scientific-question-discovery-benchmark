#!/usr/bin/env python3
"""Build a small, information-dense annotation subset with known weights.

    python scripts/make_subset.py --n 24

Ninety items is more than a single annotator can reasonably absorb. Rather
than thinning at random — which spends most of the budget on items where
the judges already agree and therefore answers nothing — we stratify by
the one thing the human labels have to settle:

    stratum D  gpt-4.1 and gpt-4o assign DIFFERENT outcomes (42 of 90)
    stratum A  they assign the SAME outcome (48 of 90)

Half the budget goes to each. Stratum D arbitrates the cross-model
disagreement reported in the judge-validation section; stratum A checks
that agreement between two models is not agreement on a shared error.
Because the stratum sizes in the full sample are known, population
estimates are recovered by post-stratification: each stratum's statistic
is weighted by its share of the 90, so the subset yields an unbiased
population estimate with an honest (wider) interval rather than a
disagreement-enriched number quoted as if it were a population rate.

Within each stratum items are drawn round-robin across systems, so no
system dominates the subset.
"""

import argparse
import json
import random
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark.schemas import load_jsonl  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "judge_validation"
SAMPLE = OUT / "sample.json"
SEED = 24081201


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=24)
    parser.add_argument("--seed", type=int, default=SEED)
    args = parser.parse_args()

    sample = json.loads(SAMPLE.read_text(encoding="utf-8"))
    strata: dict[str, list[tuple[str, str]]] = {"D": [], "A": []}
    for name, spec in sample.items():
        base = {r["question_id"]: r
                for r in load_jsonl(ROOT / spec["annotations_file"])}
        alt = {r["question_id"]: r
               for r in load_jsonl(OUT / f"e2_gpt4o_{name}.jsonl")}
        for qid in spec["question_ids"]:
            if qid in base and qid in alt:
                key = "A" if base[qid]["outcome"] == alt[qid]["outcome"] else "D"
                strata[key].append((name, qid))

    rng = random.Random(args.seed)
    picked: dict[str, list[tuple[str, str]]] = {}
    per_stratum = args.n // 2
    for key, pool in strata.items():
        by_system: dict[str, list] = defaultdict(list)
        for name, qid in sorted(pool):
            by_system[name].append((name, qid))
        for items in by_system.values():
            rng.shuffle(items)
        chosen, systems = [], sorted(by_system)
        while len(chosen) < min(per_stratum, len(pool)):      # round-robin
            for name in systems:
                if by_system[name] and len(chosen) < per_stratum:
                    chosen.append(by_system[name].pop())
        picked[key] = chosen

    subset = {"n": sum(len(v) for v in picked.values()), "seed": args.seed,
              "strata": {}, "items": []}
    for key, chosen in picked.items():
        subset["strata"][key] = {
            "description": ("gpt-4.1 and gpt-4o disagree on outcome" if key == "D"
                            else "gpt-4.1 and gpt-4o agree on outcome"),
            "population_size": len(strata[key]),
            "sampled": len(chosen),
            "weight": round(len(strata[key]) / sum(len(v) for v in strata.values()), 4),
        }
        for name, qid in chosen:
            subset["items"].append({"system": name, "question_id": qid,
                                    "stratum": key})
    (OUT / "subset.json").write_text(json.dumps(subset, indent=2, ensure_ascii=False),
                                     encoding="utf-8")
    print(f"OK: {subset['n']} items -> {OUT/'subset.json'}")
    for key, meta in subset["strata"].items():
        print(f"  stratum {key}: {meta['sampled']} sampled of "
              f"{meta['population_size']} (weight {meta['weight']}) — "
              f"{meta['description']}")


if __name__ == "__main__":
    main()
