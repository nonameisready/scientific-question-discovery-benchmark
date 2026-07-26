# Reproducibility (v1.0)

## Three tiers

**Tier 1 — offline, no keys, CI-enforced.** The released instance ships
frozen questions, retrieval records, adjudicated annotations, and
results. Anyone can re-run validation → metrics → report and must get
bit-identical results:

```bash
pip install -e .
python -m benchmark.run --config configs/astronomy_2020.yaml
git diff --exit-code results/    # CI does exactly this
```

**Tier 2 — re-judging (OPENAI_API_KEY).** Rebuild the future corpus from
its manifest, re-run retrieval and judging, and compare against the
released annotations. LLM outputs are not bit-stable; agreement is
evaluated at the label level and disagreements go to adjudication. New
runs get new version suffixes; released runs are never overwritten.

**Tier 3 — full corpus rebuild (ADS_API_TOKEN).** Corpus data is not
committed (licensing + size); the manifests are the source of truth:

```bash
python scripts/prepare_corpus.py \
    --manifest data/corpus_metadata/corpus_b_manifest.json \
    --out data/corpus/future_corpus.jsonl
```

ADS is a living index, so a rebuild today can differ slightly from the
frozen count (1,891). The manifest records the frozen count and query
set; drift is reported, not hidden.

## Pinned components (astronomy v1)

| Component | Value |
|---|---|
| Cutoff | 2020-12-31 |
| Future window | 2021-01-01 … 2026-07-01 |
| Embedding model | text-embedding-3-small |
| Similarity / k | cosine / top-8 |
| Judge model | gpt-4.1 (temperature 0), protocol hv-p1 |
| Questions | 10, frozen 2026-07-25 |

## Never overwrite

Changing the judge, retriever, or label definitions mints a new versioned
run (`outcomes_v2.jsonl`, `astronomy_top8_v2.jsonl`, …). Released results
are append-only; CI (`repro-smoke.yml`, `data-validation.yml`) rejects
in-place changes to released files.
