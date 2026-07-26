# submissions/ — evaluated systems

One directory per system, in the [submission format](../docs/submission_format.md):
`questions.jsonl` (frozen questions) + `metadata.json` (system
description, including any LLM components used in generation).

| System | Description | Status |
|---|---|---|
| `evidence_graph_v1` | Paper 1's evidence-based question discovery (claims → tensions → ranked questions) | evaluated on astronomy v1 |
| `example_system` | template for new submissions | template only |

The benchmark treats every submission identically — the evidence-graph
system gets no special interface. To submit: copy `example_system/`,
replace the questions with your frozen output, validate with
`scripts/validate_cutoff.py`, and open a PR.
