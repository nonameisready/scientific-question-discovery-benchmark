# Release: astronomy historical backtesting benchmark v1.0.0

Frozen bundle for the astronomy v1 instance.

| Artifact | Version | File |
|---|---|---|
| Benchmark protocol | v1.0 | `docs/benchmark_protocol.md` |
| Astronomy dataset | v1.0 | `data/questions/astronomy_questions_v1.jsonl` |
| Retrieval run | v1.0 | `data/retrieval/astronomy_top8_v1.jsonl` |
| Annotations | v1.0 | `data/annotations/outcomes_v1.jsonl` (+ adjudication) |
| Results | v1.0 | `results/astronomy_v1/` |

Provenance: questions, verdicts, and corpus manifests derive from the
`hv-p1` historical-validation run of
[scientific-question-discovery](https://github.com/nonameisready/scientific-question-discovery)
(cutoff 2020-12-31, validation window 2021–2026, judge gpt-4.1,
retrieval text-embedding-3-small top-8).

Planned for v1.1: full top-8 retrieval lists with per-document scores;
baseline submissions and leaderboard runs.
