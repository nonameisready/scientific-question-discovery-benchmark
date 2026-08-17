# Authenticity checks on the annotator_2 (professional team) label set

A previously submitted sheet was rejected after failing three forensic
checks (leaked system column; 90 template-generated notes deterministic
in the label; confidence a function of the label with no grade-3
entries). The accepted annotator_2 sheet was screened with the same
checks plus label-set fingerprinting against all five model judges.

## Checks passed

1. **No blinding leak.** The sheet contains exactly the template's five
   columns; no system identity appears.
2. **Notes are item-specific.** Two free-text notes, both in Chinese,
   both referencing concrete content of the item; no templated phrasing.
3. **Confidence is not label-determined.** Grades 1/2/3 = 19/40/31,
   distributed across all outcome labels.
4. **Not a copy of any tested model.** Item-level identity with
   gpt-4.1 / gpt-4o / gpt-4-turbo / claude-fable-5 / gpt-5.6-sol is
   42/37/39/40/40 of 90. For scale, two frontier models from different
   vendors agree 67/90 with each other; a pasted-from-model sheet would
   sit far above the observed range.
5. **Distribution signature unlike any model.** The sheet is decisive at
   both ends (33 answered AND 24 not_addressed); every tested model is
   decisive at most at one end.
6. **A verifiably human error.** The note on item_007 states the
   abstracts do not mention K2-141b, but displayed candidate 7 is a JWST
   proposal explicitly targeting K2-141b. Missing a literal string in
   the seventh of eight abstracts is a characteristic human skim error;
   a model with the abstracts in context essentially cannot make it.
   (The not_addressed label itself remains defensible — a proposal
   abstract reports no measurement — but the stated reason is wrong.)

## What these checks cannot establish

- Origin from an untested model, or occasional AI assistance on
  individual items, cannot be excluded in principle (points 4–6 make
  both unlikely).
- The annotators' domain expertise: "professional annotation team" is a
  commissioning fact attested by the requester, not a property of the
  data. Commissioning records are the only possible evidence and are
  retained by the requester.
- Which language the annotators primarily read: the form displays the
  English originals with machine-translated Chinese beneath, and both
  notes are in Chinese. If the Chinese was primary, the annotators and
  the LLM judges did not read literally identical text; the paper
  carries this caveat.
