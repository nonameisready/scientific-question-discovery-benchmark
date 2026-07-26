# Baselines

Four reference question-generation baselines. Each writes a frozen
submission (`questions.jsonl` in the [submission format](../docs/submission_format.md))
that the benchmark evaluates exactly like any other system — the
benchmark itself never generates questions.

| Baseline | Idea |
|---|---|
| `random_claim.py` | Sample claims from the past corpus, template them into questions |
| `direct_llm.py` | Prompt an LLM with pre-cutoff abstracts: "what should be investigated next?" |
| `review_future_work.py` | Extract future-work questions verbatim from pre-cutoff review papers |
| `citation_leader.py` | Generate questions from the most-cited pre-cutoff papers |

All four consume **only pre-cutoff corpus records** and freeze their
output before any future-corpus access; `scripts/validate_cutoff.py`
enforces this. Baseline runs on astronomy v1 are part of the public
leaderboard roadmap (see README); the pilot release ships the harness
and the `evidence_graph_v1` submission.
