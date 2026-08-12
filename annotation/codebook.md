# Annotation codebook — historical backtesting outcomes

You will see a research question written **before 2021**, and up to eight
abstracts of papers published **after** it. Judge only from these abstracts.
You do not need to know the field's later history; if an abstract does not
show it, it did not happen for our purposes.

Assign **two independent labels** per item.

## Label 1 — outcome: what happened to the question?

| Code | Meaning | Test to apply |
|---|---|---|
| `answered` | The literature substantially resolved it | Could you now state the answer, citing these abstracts? |
| `partially_addressed` | Substantial directly-relevant progress, core question still open | Real progress on *this* question, but no resolution |
| `posed_but_open` | Later work independently raises the same question without resolving it | The abstracts ask it too, and leave it open |
| `not_addressed` | No abstract engages it substantively | Same topic is **not** engagement |

**The single most common error is confusing topic overlap with engagement.**
An abstract about the same planet, or the same molecule, does not count
unless it bears on the question's actual test or its premise.

## Label 2 — premise_status: what happened to the assumption the question rests on?

| Code | Meaning |
|---|---|
| `supported` | Later evidence confirms the premise |
| `refuted` | Later evidence falsifies it |
| `weakened` | Later evidence seriously undermines it without falsifying |
| `still_plausible` | The premise was never directly tested |
| `not_applicable` | The question rests on no contestable premise |

A question can be `answered` **because** its premise was `refuted` — that
combination is expected, not a contradiction.

## Worked examples

*Question:* "Is the strongly subsolar terminator water abundance retrieved for
HD 209458 b a property of the atmosphere, or an artifact of retrieval
assumptions?"
*Abstracts:* three independent reanalyses converging on a solar abundance.
→ `answered` + `refuted` (the question is settled, and settled by overturning
the premise it challenged).

*Question:* the same question.
*Abstracts:* several papers measuring water in *other* hot Jupiters.
→ `not_addressed` (same topic, different object — no bearing on this test).

*Question:* "How do inhomogeneous terminators bias retrieved abundances?"
*Abstracts:* papers demonstrating the bias exists in general, none resolving
the specific case asked about.
→ `partially_addressed` + `still_plausible`.

## Procedure

1. Work through items **in the order given**; do not skip ahead.
2. Do **not** discuss items with the other annotator until both sheets are done.
3. Do **not** look up the papers online — abstracts only. The LLM judge saw
   exactly these abstracts, so any extra knowledge you use breaks the
   comparison.
4. Enter `confidence` as 1 (low) / 2 (medium) / 3 (high). Low-confidence items
   are analysed separately — they are informative, not failures.
5. Use `notes` freely, especially where you hesitated.

Budget roughly 2–3 minutes per item.
