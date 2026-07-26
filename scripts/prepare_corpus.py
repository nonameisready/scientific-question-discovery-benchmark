#!/usr/bin/env python3
"""Rebuild a benchmark corpus from its manifest via the NASA ADS API.

    python scripts/prepare_corpus.py \
        --manifest data/corpus_metadata/corpus_b_manifest.json \
        --out data/corpus/future_corpus.jsonl

Requires ADS_API_TOKEN (https://ui.adsabs.harvard.edu/user/settings/token).
Records are deduplicated by bibcode; records without abstracts are
dropped, matching the frozen corpus construction. The corpus data itself
is not committed to the repository — the manifest (queries, window,
counts) is the source of truth, per the reproducibility policy in
docs/reproducibility.md.
"""

import argparse
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from benchmark.schemas import write_jsonl  # noqa: E402

ADS_URL = "https://api.adsabs.harvard.edu/v1/search/query"
FIELDS = "bibcode,title,abstract,pubdate,citation_count"
PAGE = 200


def search(query: str, year_min: int, year_max: int, max_records: int) -> list[dict]:
    import requests

    headers = {"Authorization": f"Bearer {os.environ['ADS_API_TOKEN']}"}
    docs, start = [], 0
    while start < max_records:
        params = {
            "q": f"{query} AND year:{year_min}-{year_max}",
            "fl": FIELDS,
            "rows": min(PAGE, max_records - start),
            "start": start,
            "sort": "date asc",
        }
        resp = requests.get(ADS_URL, headers=headers, params=params, timeout=60)
        resp.raise_for_status()
        page = resp.json()["response"]["docs"]
        if not page:
            break
        docs.extend(page)
        start += len(page)
        time.sleep(0.3)
    return docs


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--max-per-query", type=int, default=700)
    args = parser.parse_args()
    manifest = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    window = manifest.get("validation_window") or manifest["publication_year"]
    rows, seen = [], set()
    for query in manifest["ads_queries"]:
        for doc in search(query, window["min"], window["max"], args.max_per_query):
            bibcode = doc.get("bibcode")
            if not bibcode or bibcode in seen or not doc.get("abstract"):
                continue
            seen.add(bibcode)
            title = doc.get("title")
            rows.append({
                "paper_id": bibcode,
                "title": title[0] if isinstance(title, list) else title,
                "abstract": doc["abstract"],
                "pubdate": doc.get("pubdate"),
                # As reported by ADS at rebuild time (includes post-cutoff
                # citations); see baselines/citation_leader.py for how this
                # biases the citation-leader baseline upward.
                "citation_count": doc.get("citation_count", 0),
                "corpus_id": manifest["corpus_id"],
            })
        print(f"  {query!r}: cumulative {len(rows)} unique records")
    write_jsonl(args.out, rows)
    print(f"OK: {len(rows)} records -> {args.out} "
          f"(manifest count: {manifest.get('n_papers', 'n/a')})")


if __name__ == "__main__":
    main()
