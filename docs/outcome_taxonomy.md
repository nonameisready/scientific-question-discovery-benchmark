# Outcome Taxonomy (v1.0)

Every question receives **two independent labels**. Splitting the
dimensions is deliberate: a single-layer scheme cannot express "the
community answered this question by refuting its premise," which is
exactly the highest-information outcome a backtest can surface.

## Dimension 1 — `outcome`: did future science engage the question?

| Label | Meaning | Decision rule |
|---|---|---|
| `answered` | Future evidence substantially answers the question | ≥1 retrieved paper states a resolution of the question's actual test (including resolution *by premise refutation*) |
| `partially_addressed` | Important progress, core question unresolved | Retrieved papers bear directly on the question's test, but no resolution |
| `posed_but_open` | The community independently recognizes the question | Retrieved papers pose essentially the same question without resolving it |
| `not_addressed` | No meaningful follow-up | No retrieved paper engages the question's actual test or premise |

"Similar topic" is **not** engagement: the paper must bear on the
question's actual test or premise.

## Dimension 2 — `premise_status`: what happened to the premise?

| Label | Meaning |
|---|---|
| `supported` | Future evidence confirms the underlying premise |
| `refuted` | Future evidence falsifies the underlying premise |
| `weakened` | Substantial doubt cast without falsification |
| `still_plausible` | The premise was not directly tested after the cutoff |
| `not_applicable` | The question does not rest on a contestable premise |

## Worked example (astronomy v1, q_008)

> *Is the strongly subsolar terminator water abundance retrieved for
> HD 209458 b a property of the atmosphere or an artifact of retrieval
> assumptions?*

By 2025, three independent retrieval frameworks converged on a
solar-consistent water abundance: the subsolar value was an artifact.
The question is **`answered`** — and answered precisely *because* the
premise (a strongly subsolar abundance) was **`refuted`**. A single-layer
taxonomy would have to discard one of these two facts.

## Mapping from the pilot's single-layer labels (hv-p1)

The pilot judge (Paper 1) emitted a single verdict plus a raw premise
field. Released v1 annotations preserve the raw value in
`source_premise_status` and map:

| hv-p1 premise | v1 `premise_status` |
|---|---|
| validated | supported |
| refuted | refuted |
| untested | still_plausible |
