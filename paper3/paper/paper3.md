# What Makes a Scientific Question Succeed? Predicting Future Attention, Resolution, and Premise Revision from Question Structure and Evidence Context

**Paper 3 — temporally grounded predictor discovery for scientific questions**

## Abstract

Large language models are increasingly asked to propose "important open
questions", and are typically evaluated by asking another model how good
those questions feel. We replace taste with history. We construct a
temporally grounded dataset of astronomy research questions frozen at five
historical cutoffs (2012–2020), spanning eight subfields and four distinct
generation sources — evidence-tension mining, direct LLM elicitation,
author-stated future work, and weak/negative controls — on top of the
complete arXiv astro-ph metadata record (2005–2025). Each question carries
a six-group cutoff-time feature record (text structure, evidence context,
novelty, falsifiability, tractability, field environment) and a tiered
outcome label derived from the five years of literature that actually
followed: whether the community substantively engaged the question, how far
it was resolved, and how quickly. Using only out-of-time and out-of-domain
evaluation, we identify which question properties robustly predict future
scientific attention, test six pre-stated hypotheses about the mechanism of
question value, and show that the resulting models produce interpretable
prediction cards rather than opaque scores. [RESULTS-SUMMARY-PLACEHOLDER]

## 1. Introduction

A scientific question is an instrument for allocating future effort. Yet
the standard way of evaluating machine-generated research questions — LLM
or expert panels scoring "importance" and "novelty" at generation time —
measures how a question *sounds*, not what it *does*. Paper 2 of this
series introduced historical backtesting as the alternative: freeze
questions using only pre-cutoff literature, then observe what the
scientific community actually did afterwards. Its pilot instance, however,
contained ten questions from a single subfield and cutoff — enough for a
case study, not for learning what distinguishes questions that succeed.

This paper turns the backtesting protocol into a supervised-learning
problem at scale. Three design decisions matter:

1. **The unit of data is (question, cutoff, subfield, source), not the
   question alone.** We generate questions at five rolling cutoffs
   (2012–2020) in eight astronomy subfields, so that one study contains
   what would otherwise be thirty historical experiments, and era- or
   field-specific accidents can be detected rather than absorbed.
2. **No single generator.** Predictors learned from one generation system
   risk being that system's stylistic fingerprint. We use four sources —
   our evidence-tension system, a direct-LLM baseline, questions extracted
   from the authors' own future-work statements, and deliberately weak
   controls (random claim pairings, vague, untestable, and
   evidence-free-contrarian questions). Without negative controls a model
   can only learn that "question-shaped sentences succeed".
3. **Prediction is out-of-time or out-of-domain, always.** Random splits
   would place near-duplicate questions from the same era and topic on
   both sides. We train on 2012–2016 cutoffs, validate on 2018, test on
   2020, and additionally hold out entire subfields.

The contribution is deliberately not a leaderboard number. It is a
temporally grounded dataset of scientific questions with subsequent
outcomes, and an analysis of *which properties of a question and its
evidence context* predicted future scientific attention, resolution, and
premise revision — with controls for field popularity, instrument eras,
and generation method, and with stability checks across cutoffs,
subfields, and sources.

## 2. Related framing

Paper 1 built an evidence-graph system that generates questions from
cross-paper observational tensions. Paper 2 defined the backtesting
benchmark and showed, on ten frozen exoplanet-atmosphere questions, that
future literature substantively engaged all ten (one premise later
refuted). Both left open the question this paper addresses: *what,
measurably, makes a question one the community will take up?* Related
work on predicting scientific impact operates at the paper or grant level
(citation prediction, idea novelty metrics); to our knowledge no prior
dataset attaches future-outcome labels to *questions* frozen at multiple
historical cutoffs with controlled generation sources.

## 3. Dataset construction

### 3.1 Corpus

We harvested the complete arXiv astro-ph metadata record — titles,
abstracts, submission dates, and categories — from 2005-01 through
2025-12 via the public arXiv API ([N-CORPUS-PLACEHOLDER] papers after
deduplication; `paper3/pipeline/harvest.py`). Papers are assigned to
eight subfields by transparent weighted keyword rules over title+abstract
(multi-membership allowed): exoplanet atmospheres, protoplanetary disks,
stellar activity, fast radio bursts, gravitational waves, galaxy
evolution, cosmology tensions, and compact objects. The classifier is
identical at every cutoff, so subfield corpora are time-sliced views of a
fixed rule, not retrofitted topic models.

Each cutoff year c ∈ {2012, 2014, 2016, 2018, 2020} defines a **past
window** [c−7, c] used for generation and features and a **future
window** (c, c+5] used only for labels. The five future windows all close
by 2025-12-31, giving every cutoff the same 5-year outcome horizon.

### 3.2 Question generation (40 cells × quota 25)

For every (cutoff, subfield) cell:

- **Evidence-tension (10).** We mine the cell's past-window abstracts for
  tension statements (contradiction, discrepancy, unexplained-result
  markers), cluster them so that each cluster spans ≥ 2 distinct papers,
  and have an LLM phrase each cluster as one precise question grounded
  only in the mined sentences. Provenance (exact sentences, arXiv ids,
  dates) is stored with the question.
- **Direct LLM (5).** The baseline the field implicitly uses: the model
  sees a year-stratified sample of pre-cutoff titles and is asked for the
  most important unanswered questions, with an explicit
  knowledge-freeze instruction.
- **Future-work (5).** Sentences in which pre-cutoff authors themselves
  flag an open problem ("remains poorly constrained", "further
  observations are needed"), selected for topic diversity and converted
  faithfully into interrogative form. These are real scientists'
  questions.
- **Controls (5).** Two random claim-pairings across unrelated papers,
  one vague question, one untestable question, one evidence-free
  consensus challenge — all phrased by the same LLM so that surface style
  cannot separate controls from real candidates.

Near-duplicates within a cell are removed (TF-IDF cosine ≥ 0.75). The ten
frozen Paper 1 evidence-graph questions join the dataset as a small
additional source (cutoff 2020, exoplanet atmospheres), linking this
study to the original system. Realized totals: [N-QUESTIONS-PLACEHOLDER].

Temporal isolation is enforced by construction — every mined sentence and
every title shown to a generator predates the cutoff — and verified by an
automated validator over the frozen records.

### 3.3 Feature record (six groups, all cutoff-time)

**A. Text structure** — length, named entities, numbers, causal /
comparative / mechanistic language, measurable quantities, explicit
alternatives ("real or artifact"), falsification wording, yes/no form,
and a composite specificity score.

**B. Evidence context** — retrieval of the top-20 pre-cutoff subfield
papers for each question: similarity mass (top-1, mean top-5, count above
threshold), instrument diversity among retrieved papers, density of
tension markers in the retrieved evidence, and the age profile of that
evidence; plus native evidence-record features (paper count, year spread)
for tension-sourced questions.

**C. Novelty** — nearest-neighbour semantic distance to the pre-cutoff
corpus, mean top-10 similarity, concept-pair novelty (do the question's
two most distinctive terms co-occur in any pre-cutoff paper?), and
overlap with pre-cutoff review articles (was the question already posed
in reviews?).

**D. Falsifiability / answerability** — rule-based markers plus a blinded
LLM structured coding of {observable, competing_hypotheses,
quantitative_test, falsification_path} for every question.

**E. Tractability** — facilities named in the question checked against a
lexicon of ~50 astronomical facilities with operational epochs: counts of
already-operational vs. future instruments, archival-data markers,
longitudinal / theory / large-sample requirements.

**F. Field environment (controls)** — subfield publication volume and
growth at the cutoff, review activity, share of all astro-ph output, and
proximity of the subfield's next major facility launch. These are
confounders to control for, not virtues of the question: without them a
model mistakes hot fields for good questions.

### 3.4 Tiered outcome labels

**Tier 1 (automatic candidates).** For each question we retrieve future
papers from its subfield's future window: relevant-paper count (cosine ≥
0.18), weak-relevance count, first-follow-up date, lead time in months,
and review recognition.

**Tier 2 (blinded LLM judge).** For every question with any plausible
future evidence, a judge sees the question and its top-8 retrieved future
records — never the generation source — and outputs `addressed`,
`answer_status` ∈ {answered, partially_addressed, posed_but_open,
premise_refuted, not_addressed}, `premise_status`, supporting arXiv ids,
a rationale, and a confidence. Questions whose best future similarity
falls below a floor are auto-labeled not_addressed without a judge call.

**Tier 3 (independent verification).** A second, stronger model
re-judges all premise_refuted cases plus a 20% random sample of judged
questions; we report raw agreement and Cohen's κ for both the binary
label and the five-way status. [AGREEMENT-PLACEHOLDER]

The label record mirrors the design's outcome dimensions: attention,
resolution status, premise status, community investment (paper counts),
and speed (lead time).

## 4. Models and evaluation protocol

Baselines before models, interpretable models before ensembles: majority
class; field-popularity-only; question-text-only (bag of words); then L2
and L1 logistic regression, random forest, and gradient boosting on the
structured features; multinomial GBM for the five-way status; a Cox
proportional-hazards model for time-to-first-follow-up; and within-cell
ranking concordance between model scores and future paper counts.

All headline numbers use the **temporal split** (train 2012–2016,
validate 2018, test 2020). Generalization is probed with
**leave-one-subfield-out** and a fixed **cross-domain split** (train:
exoplanet atmospheres, disks, stellar activity, galaxy evolution → test:
FRBs, gravitational waves, cosmology tensions, compact objects). Random
splits are not reported anywhere in this paper.

Predictor identification goes beyond feature importance: (i) univariate
associations; (ii) controlled logistic effects with subfield, cutoff,
source, and environment covariates; (iii) feature-group ablations; (iv)
sign-stability of controlled effects across cutoffs, subfields, and
generation sources. A predictor is called robust only if it survives all
four.

### Pre-stated hypotheses

- **H1** Cross-source evidence tension predicts future attention better
  than semantic novelty.
- **H2** Observation availability predicts short-term attention but not
  premise refutation.
- **H3** Explicit competing hypotheses raise the probability of being
  answered, given attention.
- **H4** Novelty shows an inverted-U: very high novelty reduces
  short-term attention.
- **H5** Field popularity inflates future paper counts without raising
  answer rates.
- **H6** High-tension × high-tractability questions succeed most.

## 5. Results

[RESULTS-PLACEHOLDER]

## 6. Discussion

[DISCUSSION-PLACEHOLDER]

## 7. Limitations

- **Abstract-level corpus.** Full texts are not used; tension and
  future-work mining see only abstracts, and citation-weighted attention
  is unavailable without a second data provider. Paper counts, lead
  times, and review recognition stand in for citation impact.
- **LLM judges, not humans.** Label reliability is estimated with an
  independent second model rather than human adjudication; the annotation
  protocol is written so human passes can be added, and all judge
  rationales and supporting ids are released for audit.
- **Parametric-knowledge leakage.** The direct-LLM source (and, weakly,
  LLM phrasing of mined material) could import post-cutoff knowledge from
  the model's training data despite freeze instructions. Mined sources
  are constructed from pre-cutoff text; the direct-LLM source should be
  read as an upper-bounded baseline, and source is controlled for in all
  regressions.
- **Retrieval-bounded labels.** A question can be engaged by literature
  our TF-IDF retrieval misses; not_addressed is therefore a lower bound
  on engagement, uniformly across sources.
- **One domain.** Astronomy only; the cross-subfield transfers here are
  necessary but not sufficient evidence of cross-science generality.

## 8. Conclusion

[CONCLUSION-PLACEHOLDER]

## Reproducibility

All code, the frozen dataset, labels, and results are in `paper3/` of the
repository; every pipeline stage is a single script, all LLM calls are
cached and pinned to temperature 0, and the offline test suite plus a
temporal-isolation validator run in CI. See `paper3/README.md`.
