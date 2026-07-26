# data/ — released benchmark data

Everything a reviewer needs to audit astronomy v1, and everything a new
system needs to be evaluated. Released files are **frozen**: changing a
judge, retriever, or label definition mints a new versioned file; nothing
is overwritten (CI enforces this).

| Path | Contents |
|---|---|
| `questions/astronomy_questions_v1.jsonl` | 10 frozen questions (cutoff 2020-12-31) with source evidence and ranks |
| `questions/example_submission.jsonl` | minimal valid submission record |
| `corpus_metadata/corpus_a_manifest.json` | past corpus: 2,512 papers, 2015–2020, frozen ADS queries |
| `corpus_metadata/corpus_b_manifest.json` | future corpus: 1,891 papers, 2021–2026, isolation rules |
| `retrieval/astronomy_top8_v1.jsonl` | retrieval run v1.0: model, window, top-k, judge-cited documents, top-1 similarity |
| `annotations/outcomes_v1.jsonl` | annotations v1.0: two-dimensional outcome labels, evidence, rationales |
| `annotations/adjudication_v1.jsonl` | human adjudication decisions per question |
| `releases/benchmark_v1/` | release notes for the frozen v1 bundle |

Bulk corpus text is **not** committed (size + licensing): the manifests
are the source of truth, and `scripts/prepare_corpus.py` rebuilds a
corpus from its manifest via the ADS API
(see [docs/reproducibility.md](../docs/reproducibility.md)).
