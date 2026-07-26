# Leakage Prevention (v1.0)

The protocol's validity rests on one invariant: **nothing from after the
cutoff influences what is generated or frozen, and everything used to
judge comes from strictly after the cutoff.**

## Rules

1. **Past-corpus purity.** Nothing dated after the cutoff enters the past
   corpus — including catalog rows whose `rowupdate` postdates the cutoff
   and metadata fields (citation counts are as-of collection and are
   therefore excluded from generation inputs in strict mode).
2. **Question freezing.** Questions are serialized with `frozen: true`
   before any future-corpus access and never edited afterwards. Frozen
   files are append-only; edits require a new versioned instance.
3. **Source-evidence audit.** Every `source_evidence_ids` bibcode must
   predate or equal the cutoff year (`scripts/validate_cutoff.py`, CI).
4. **Future-corpus isolation.** The future corpus is collected under its
   own manifest, stored separately, and filtered by corpus identifier;
   its records must never enter the past-corpus pipeline. Its window
   must start strictly after the cutoff.
5. **Retrieval containment.** Only future-corpus documents may be
   retrieved; every retrieved bibcode's year must postdate the cutoff.
6. **Citation containment.** The judge may cite only retrieved
   candidates; violations are hard errors, never silently dropped.
7. **Recorded contamination surface.** Retrieval dates, embedding model,
   judge model, and (where known) model training cutoffs are recorded in
   the released records so residual contamination can be audited.

## What the protocol cannot prevent (declared, not hidden)

- **Model-weight contamination.** A modern LLM used for generation or
  judging has training data that postdates the cutoff. The protocol
  controls the *retrieval* channel, not the *weights* channel. This is
  measured and discussed in the paper's threats-to-validity section, and
  is why generation-system metadata must disclose the models used.
- **Question-selection hindsight by human curators.** Curators who know
  the post-cutoff literature could bias curation; the astronomy v1
  curation log is released so this can be audited.

## Enforcement

`python scripts/validate_data.py --config configs/<instance>.yaml`
runs rules 1–6 plus metrics reproducibility, and runs in CI on every
change to `data/`, `results/`, `configs/`, or `benchmark/`.
