# Scientific Question Backtesting Benchmark

A model-agnostic benchmark for evaluating whether AI-generated
scientific questions anticipate future scientific progress.

The benchmark freezes questions using literature available before a
historical cutoff and evaluates them against an isolated future corpus.

## Core idea

```
Past literature → Generated questions → Frozen evaluation →
Future evidence → Outcome labels → Benchmark metrics
```

A scientific question is valuable if future science actually invests in
answering it. Historical backtesting turns that idea into a reproducible
measurement: any system generates questions from a pre-cutoff corpus,
freezes them, and is scored against what the scientific community
actually did afterwards — no expert panels, no self-grading LLM scores.

## Astronomy v1

- Historical cutoff: **2020-12-31**
- Past corpus: **2,512 papers** (2015–2020, NASA ADS; 500 full-text core)
- Future corpus: **1,891 papers** (2021–2026, temporally isolated)
- Questions: **10** (frozen, from the [evidence-graph system](https://github.com/nonameisready/scientific-question-discovery))
- Addressed by future literature: **10/10**
- Answered: **2** · Partially addressed: **7** · Posed but still open: **1**
- Premise refuted: **1** (HD 209458 b subsolar water — see the paper's case study)

> Astronomy v1 is the first benchmark instance, not the definition of
> the benchmark itself.

## Quickstart (offline, no API keys)

```bash
pip install -e .
pytest                                                   # 24 offline tests
python -m benchmark.run --config configs/astronomy_2020.yaml
```

This validates schemas and temporal isolation, recomputes
`results/astronomy_v1/{metrics.json, per_question_results.csv, report.md}`,
and refreshes `results/leaderboard.json` — bit-identical to the committed
files (CI enforces it).

Step by step instead:

```bash
python scripts/validate_cutoff.py \
  --questions data/questions/astronomy_questions_v1.jsonl --cutoff 2020-12-31
python scripts/compute_metrics.py \
  --annotations data/annotations/outcomes_v1.jsonl
```

Live stages (rebuilding corpora, retrieval, judging) need API keys — see
`.env.example` and [docs/reproducibility.md](docs/reproducibility.md).

## Evaluate your own system

The benchmark does not generate questions; it evaluates frozen question
lists from **any** system:

1. Generate questions from pre-cutoff evidence only.
2. Freeze them in the [submission format](docs/submission_format.md)
   under `submissions/<your_system>/`.
3. `python scripts/validate_cutoff.py --questions ... --cutoff 2020-12-31`
4. Run retrieval + judging (`scripts/retrieve_future_evidence.py`,
   `scripts/judge_outcomes.py`), get labels adjudicated, compute metrics.

Reference baselines (random claims, direct LLM, review future-work,
citation leaders) live in [baselines/](baselines/).

## Repository map

| Path | Contents |
|---|---|
| `benchmark/` | protocol implementation: schemas, leakage checks, retrieval, judging, metrics, reporting |
| `configs/` | benchmark instance definitions (`astronomy_2020.yaml`), outcome taxonomy |
| `data/` | frozen questions, corpus manifests, retrieval records, adjudicated annotations |
| `docs/` | [protocol](docs/benchmark_protocol.md) · [taxonomy](docs/outcome_taxonomy.md) · [annotation](docs/annotation_guidelines.md) · [leakage](docs/leakage_prevention.md) · [submissions](docs/submission_format.md) · [reproducibility](docs/reproducibility.md) |
| `baselines/` | four reference question generators |
| `scripts/` | CLI: validate → prepare corpus → retrieve → judge → metrics → report |
| `submissions/` | evaluated systems (`evidence_graph_v1` = Paper 1's system) |
| `results/` | released metrics, per-question results, reports, leaderboard |
| `tests/` + `.github/workflows/` | offline tests, data validation, reproducibility smoke test |
| `paper/` | the benchmark paper (Paper 2) |
| `paper3/` | **Paper 3**: ~1,000-question temporally grounded dataset (5 cutoffs × 8 subfields × 4 sources) + predictor-discovery study — see [paper3/README.md](paper3/README.md) |

## Relationship to the question-generation repo (Paper 1)

[`scientific-question-discovery`](https://github.com/nonameisready/scientific-question-discovery)
is **how to generate** questions (evidence graph, tension detection,
ranking). This repository is **how to evaluate** them. The generation
system appears here only as one submission, `submissions/evidence_graph_v1`
— like any future system.

## Roadmap

- Public leaderboard with baseline runs (random claims, direct LLM,
  review future-work, citation leaders) on astronomy v1
- Full top-8 retrieval lists with per-document scores (v1.1 data release)
- Additional domain instances and cutoffs; lead-time estimation from
  community first-posed dates

## Citation

See [CITATION.cff](CITATION.cff). License: [Apache-2.0](LICENSE).
