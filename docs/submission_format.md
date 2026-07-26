# Submission Format (v1.0)

Any question-discovery system is evaluated by submitting **frozen
questions**; the benchmark does the rest (isolation checks → retrieval →
judging → adjudication → metrics → report).

## Directory layout

```
submissions/<system_name>/
├── questions.jsonl     # one frozen question per line
└── metadata.json       # system description
```

## questions.jsonl — one record per line

```json
{
  "question_id": "q_001",
  "question": "Is the reported low water abundance of planet X robust to retrieval assumptions?",
  "domain": "exoplanet_atmospheres",
  "cutoff_date": "2020-12-31",
  "generated_at": "2026-01-15",
  "generation_system": "my_system_v1",
  "source_evidence_ids": ["2019MNRAS.482.1485P"],
  "rank": 1,
  "frozen": true
}
```

| Field | Required | Notes |
|---|---|---|
| `question_id` | yes | unique within the submission |
| `question` | yes | one interrogative sentence, ends with `?` |
| `domain` | yes | must match the benchmark instance |
| `cutoff_date` | yes | must equal the instance cutoff |
| `generated_at` | yes | ISO date the question was produced |
| `generation_system` | yes | versioned system identifier |
| `source_evidence_ids` | yes | pre-cutoff bibcodes the question is grounded in |
| `rank` | yes | the system's own priority order (1 = best) |
| `frozen` | yes | must be `true`; questions are immutable after submission |
| `sub_questions`, `objects`, `signal_type` | no | optional structure |

## metadata.json

```json
{
  "system_name": "my_system_v1",
  "description": "one paragraph",
  "repository": "https://github.com/...",
  "cutoff_date": "2020-12-31",
  "domain": "exoplanet_atmospheres",
  "n_questions": 10,
  "frozen": true,
  "llm_components": {"generation": "model name + version"}
}
```

`llm_components` is required whenever an LLM touched generation: the
weights-contamination surface must be declared (see
[leakage_prevention.md](leakage_prevention.md)).

## Validation before evaluation

```bash
python scripts/validate_cutoff.py \
    --questions submissions/my_system_v1/questions.jsonl \
    --cutoff 2020-12-31
```

Submissions that fail schema or cutoff validation are not evaluated.
Number of questions: match the instance's question budget (astronomy v1:
10 ranked questions) so rates are comparable across systems.
