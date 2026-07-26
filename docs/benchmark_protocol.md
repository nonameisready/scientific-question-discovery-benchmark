# The Historical Backtesting Protocol (v1.0)

A model-agnostic protocol for evaluating scientific question discovery:
**a scientific question is valuable if future science actually invests in
answering it.** The protocol turns that idea into a reproducible
measurement by rewinding the clock.

```
Past Literature (≤ cutoff)
        │
Generate Scientific Questions        ← any system
        │
Freeze Questions                     ← immutable before future access
        │
Future Literature (after cutoff)     ← temporally isolated corpus
        │
Retrieve Evidence                    ← fixed embedding retrieval, top-k
        │
Historical Outcome Assessment        ← constrained judge + human adjudication
        │
Benchmark Metrics
```

There is no question generator, evidence graph, or particular LLM in the
protocol: any system that emits frozen questions can be evaluated.

## Steps

### 1. Choose a cutoff
A historical date `T` (astronomy v1: **2020-12-31**). Everything at or
before `T` is "the past"; everything after is "the future".

### 2. Generate questions
Any method — an evidence-graph pipeline, a prompted LLM, a heuristic
baseline, a human. The system may consume **only** past-corpus evidence.
Each question records its `source_evidence_ids`; any source postdating
the cutoff invalidates the submission (`scripts/validate_cutoff.py`).

### 3. Freeze
Questions are serialized in the [submission format](submission_format.md)
with `frozen: true` **before any future-corpus access**, and are never
edited afterwards. Rewording a question after seeing the future corpus is
the benchmark's cardinal sin; frozen files are append-only in the
repository and guarded by CI.

### 4. Define the future window
A bounded window after the cutoff (astronomy v1: **2021–2026**), realized
as an isolated future corpus built from frozen queries
(`data/corpus_metadata/corpus_b_manifest.json`). Isolation rules are in
[leakage_prevention.md](leakage_prevention.md).

### 5. Retrieve future evidence
For each frozen question, embed the question text and every future-corpus
`title + abstract`; rank by cosine similarity; keep the top-k (default 8,
`text-embedding-3-small`). Retrieval is deliberately fixed so systems are
compared on their questions, not their retrievers. Retrieval records are
released so reviewers can see exactly which documents the judge saw.

### 6. Assess outcomes
A constrained judge assigns **two independent labels** per question
([outcome_taxonomy.md](outcome_taxonomy.md)):

| Dimension | Labels |
|---|---|
| `outcome` | answered · partially_addressed · posed_but_open · not_addressed |
| `premise_status` | supported · refuted · weakened · still_plausible · not_applicable |

The judge may cite only retrieved candidates (violations are hard
errors), and every label requires human adjudication before release
([annotation_guidelines.md](annotation_guidelines.md)).

### 7. Compute metrics
`python -m benchmark.run --config configs/<instance>.yaml` produces
`metrics.json`, `per_question_results.csv`, and `report.md`. Definitions
live in `benchmark/metrics.py` and the paper.

## Versioning

Protocol, dataset, annotations, and retrieval runs are versioned
independently (`protocol v1.0`, `astronomy dataset v1.0`,
`annotations v1.0`, `retrieval run v1.0`). Changing a judge, retriever,
or label definition mints a **new** versioned run; released results are
never overwritten.

Astronomy v1 is the first benchmark *instance*, not the definition of
the benchmark itself.
