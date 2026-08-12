"""Deterministic specificity (anchoring) scoring for frozen questions.

Broad questions ("How can we better understand exoplanet atmospheres?")
are engaged by future literature almost for free; specific, falsifiable
questions are the ones whose engagement carries information. This module
scores each question 0-3 with a released, auditable rubric — no LLM in
the loop, so the score cannot drift and cannot be lobbied:

  S_object    names at least one specific catalogued object
              (HD 209458 b, WASP-121 b, TRAPPIST-1, ...)
  S_quantity  names a specific measurable claim: a chemical species, a
              quantity with units, or an abundance comparative
              (subsolar / solar / ppm / upper limit ...)
  S_test      contains an explicit discriminative construction
              ("... or an artifact of ...", "as tested by",
              "under what conditions", "hold under", "reconciled")

Template baselines inherit S_test from their template by construction;
the content-anchoring components (S_object, S_quantity) are inherited
only when the underlying source content provides them. The paper reports
component distributions per system for exactly this reason.

Specificity-adjusted foresight (SAF) combines anchoring with outcome:

  SAF = mean_q( outcome_weight(q) * specificity(q) / 3 )

with outcome weights answered=1.0, partially_addressed=0.5,
posed_but_open=0.25, not_addressed=0. A refuted premise does not add
weight (it is reported separately). The novelty term of a full foresight
metric requires community first-posed dates and is deferred with lead
time (see docs and paper roadmap).
"""

from __future__ import annotations

import re

OBJECT_PATTERNS = [
    r"\bHD\s?\d{4,6}\s?[A-Gb-g]?\b",
    r"\bWASP-\d+\s?[A-Gb-g]?\b",
    r"\bHAT-P-\d+\s?[A-Gb-g]?\b",
    r"\bKELT-\d+\s?[A-Gb-g]?\b",
    r"\bK2-\d+\s?[A-Gb-g]?\b",
    r"\bKepler-\d+\s?[A-Gb-g]?\b",
    r"\bGJ\s?\d{2,4}\s?[A-Gb-g]?\b",
    r"\bLHS\s?\d{3,4}\s?[A-Gb-g]?\b",
    r"\bTOI-?\d+\s?[A-Gb-g]?\b",
    r"\bTRAPPIST-1\s?[b-h]?\b",
    r"\bCoRoT-\d+\s?[A-Gb-g]?\b",
    r"\bTrES-\d+\s?[A-Gb-g]?\b",
    r"\bXO-\d+\s?[A-Gb-g]?\b",
    r"\b55\s?Cnc\s?e?\b",
    r"\b51\s?Peg(asi)?\s?b?\b",
    r"\bGl\s?\d{2,4}\s?[A-Gb-g]?\b",
    r"\bNGTS-\d+\s?[A-Gb-g]?\b",
    r"\bLTT\s?\d{3,4}\s?[A-Gb-g]?\b",
    r"\bL\s?98-59\s?[b-d]?\b",
    r"\bV1298\s?Tau\b",
    r"\bAU\s?Mic\s?[b-c]?\b",
    r"\bbeta\s?Pic(toris)?\s?[b-c]?\b",
    r"\bProxima\s?(Cen(tauri)?)?\s?[b-d]\b",
]
OBJECT_RE = re.compile("|".join(OBJECT_PATTERNS), re.IGNORECASE)

SPECIES = [
    "H2O", "water", "CH4", "methane", "CO2", "carbon dioxide", "CO",
    "carbon monoxide", "TiO", "titanium oxide", "VO", "vanadium oxide",
    "NH3", "ammonia", "HCN", "Na ", "sodium", "K I", "potassium", "FeH",
    "SiO", "H-", "helium", "He I", "10830", "hydrogen", "Lyman",
    "H-alpha", "Balmer", "SO2", "sulfur", "PH3", "phosphine", "C/O",
    "metallicity", "haze", "cloud", "aerosol",
]
QUANTITY_RE = re.compile(
    r"\bsub-?solar\b|\bsuper-?solar\b|\bsolar\b|\bppm\b|\bupper limits?\b"
    r"|\bnon-?detections?\b|\b\d+(\.\d+)?\s?(K|bar|mbar|ppm|um|micron|A|nm|%)\b"
    r"|\b\d+(\.\d+)?\s?(x|times)\s?solar\b|\bscale heights?\b",
    re.IGNORECASE)

TEST_RE = re.compile(
    r"\bor an? artifact\b|\bas tested by\b|\bunder what (observational, )?"
    r"(observational or )?(methodological )?conditions\b|\bhold under\b"
    r"|\brobust to\b|\breconcil\w+\b|\bconfirmed? by independent\b"
    r"|\bindependent(ly)? (of|confirm|reproduc|retriev|datasets?|analys)\w*\b"
    r"|\bproperty of the atmosphere or\b|\brule[sd]? out\b"
    r"|\bdistinguish(es|ed)? between\b|\bwhich (currently )?untested assumption\b",
    re.IGNORECASE)

OUTCOME_WEIGHTS = {
    "answered": 1.0,
    "partially_addressed": 0.5,
    "posed_but_open": 0.25,
    "not_addressed": 0.0,
}


def score_question(text: str) -> dict:
    """Score one question text. Deterministic; returns components + total."""
    s_object = 1 if OBJECT_RE.search(text) else 0
    lowered = text.lower()
    s_quantity = 1 if (any(sp.lower() in lowered for sp in SPECIES)
                       or QUANTITY_RE.search(text)) else 0
    s_test = 1 if TEST_RE.search(text) else 0
    return {
        "s_object": s_object,
        "s_quantity": s_quantity,
        "s_test": s_test,
        "specificity": s_object + s_quantity + s_test,
    }


def saf(questions: list[dict], outcomes: list[dict]) -> dict:
    """Specificity-adjusted foresight over aligned question/outcome records."""
    omap = {o["question_id"]: o for o in outcomes}
    per_question, total = [], 0.0
    for q in questions:
        s = score_question(q["question"])
        o = omap[q["question_id"]]
        w = OUTCOME_WEIGHTS[o["outcome"]]
        contribution = w * s["specificity"] / 3
        total += contribution
        per_question.append({
            "question_id": q["question_id"], **s,
            "outcome": o["outcome"], "outcome_weight": w,
            "saf_contribution": round(contribution, 4),
        })
    n = len(per_question) or 1
    mean_spec = sum(p["specificity"] for p in per_question) / n
    return {
        "n": len(per_question),
        "mean_specificity": round(mean_spec, 3),
        "component_rates": {
            c: round(sum(p[c] for p in per_question) / n, 3)
            for c in ("s_object", "s_quantity", "s_test")
        },
        "saf": round(total / n, 4),
        "per_question": per_question,
    }
