# Annotation & Adjudication Guidelines (v1.0)

Judge labels are drafts. No outcome enters a released benchmark instance
until a human adjudicator has reviewed it. This file defines that review.

## Inputs per question

1. The frozen question text (and sub-questions, if any).
2. The top-k retrieved future abstracts (the judge saw nothing else).
3. The judge's proposed `outcome`, `premise_status`, cited evidence
   (bibcode + one-sentence relevance), and rationale.

## Adjudication procedure

For each question, the adjudicator must:

1. **Check citation validity** — every cited bibcode is among the
   retrieved candidates and its relevance sentence accurately reflects
   the abstract. A fabricated or misused citation rejects the record.
2. **Check the engagement bar** — "similar topic" is not engagement.
   The cited paper must bear on the question's actual test or premise
   (e.g. a terminator-heterogeneity paper about *another planet* does not
   answer a WASP-12 b question; it supports at most `posed_but_open` /
   `partially_addressed`).
3. **Check the outcome/premise split** — if the premise was refuted,
   verify the outcome reflects what happened to the *question* (a
   refuted premise can still mean `answered`).
4. **Record a decision** — `accept`, `revise` (with corrected labels),
   or `reject` (send back for re-judging), plus a short note, in
   `data/annotations/adjudication_<version>.jsonl`:

```json
{"question_id": "q_008", "decision": "accept", "adjudicator": "human_reviewer_1",
 "notes": "Refutation supported by three independent frameworks and datasets."}
```

5. **Flip the status** — accepted records get
   `adjudication_status: "reviewed"` in the outcomes file. CI rejects
   released instances containing unreviewed records.

## Conservatism rules

- When torn between two outcome labels, choose the weaker engagement.
- `answered` requires the resolution to be stated in the cited abstracts,
  not inferred by the adjudicator.
- Evidence from a single paper cannot support `answered` unless the
  paper itself reports convergence across independent analyses.
- Do not consult literature outside the retrieved candidates while
  labeling; a retrieval miss is measured, not silently patched (it goes
  to the error analysis instead).
