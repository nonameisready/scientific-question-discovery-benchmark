# Recruiting a second annotator — email templates

## Before you send

**Send individually, not as a BCC blast.** Exoplanet atmospheres is a small
community; a message that looks automated reads as spam and costs more
goodwill than it gains. Five to ten personalised emails, sent one at a time
with the recipient's own paper named in the first line, will do better than
fifty identical ones. Batch of 8, wait a week, send the next batch.

**Emails are not in the candidate list, and should not be guessed.** Take the
corresponding-author address from the front page of the person's most recent
paper (linked in `recruitment_candidates.csv`) or from their group page.

**Be specific about what co-authorship means.** Offering authorship for one
hour of labelling is generous but standard for benchmark papers, provided the
contribution is real and the person can vouch for the work. Say plainly what
you expect of them: label the items, read the section that describes the
annotation, and approve the final text. Anyone who declines authorship should
still be offered an acknowledgement and, if they prefer, payment.

---

## Template A — the main ask (~160 words)

> **Subject:** 1 hour, co-authorship: does an LLM judge match expert judgement
> on exoplanet-atmosphere literature?
>
> Dear Dr <Surname>,
>
> I read <PAPER TITLE> (<YEAR>) — <ONE SPECIFIC SENTENCE ABOUT IT, NOT
> FLATTERY: what you did and why it is relevant to this request>.
>
> I am building a benchmark that scores AI systems on the research questions
> they generate, by checking whether later literature actually engaged those
> questions. The labels currently come from an LLM judge. In a first blinded
> pass, a non-expert annotator agreed with that judge at chance
> (κ = 0.04, n = 23). I do not yet know whether the judge is wrong, the
> annotator was, or the label scheme is underdetermined — and only a second
> independent annotator can tell me.
>
> The ask is one hour: 23 questions, each with eight post-2021 abstracts,
> labelled in a self-contained web page (no install, works offline). Everything
> is blinded — you will not see which system produced which question, or what
> the LLM answered.
>
> In return I would like to offer co-authorship on the resulting paper:
> concretely, labelling the items, reviewing the section that reports the
> annotation, and approving the final text. If you would rather not be an
> author, an acknowledgement or an honorarium is equally fine.
>
> Data, code and the full protocol are public: <REPO URL>.
>
> Happy to send the page, or to answer anything first.
>
> Best regards,
> <NAME>
> <AFFILIATION / ROLE>

---

## Template B — shorter cold version (~90 words)

> **Subject:** 1-hour blinded annotation task (co-authorship offered) —
> exoplanet atmosphere literature
>
> Dear Dr <Surname>,
>
> I am testing whether an LLM can reproduce expert judgement about what the
> post-2021 exoplanet-atmosphere literature did or did not settle. A first
> non-expert pass agreed with the model at chance, so I need one domain expert
> to label the same 23 items independently.
>
> One hour, self-contained web page, fully blinded. Co-authorship on the
> resulting benchmark paper, or an acknowledgement/honorarium if you prefer.
> Code and data are public: <REPO URL>.
>
> May I send you the page?
>
> Best regards,
> <NAME>

---

## Template C — reply to send once someone agrees

> Thank you — here is everything.
>
> **Attached:** `annotator_2_form_subset.html`. Open it in any browser; it runs
> offline and saves your progress locally as you go. When you have finished all
> 23 items, click **Export CSV** and send me the file.
>
> **Three things that matter for the comparison:**
>
> 1. Judge only from the abstracts shown. Please do not look the papers up —
> the LLM saw exactly these abstracts, so any extra knowledge breaks the
> comparison. If you happen to know the later history, set it aside.
> 2. Same topic is not engagement. An abstract on the same planet or the same
> molecule does not count unless it bears on the question's actual test, or on
> the assumption the question rests on.
> 3. Please do not discuss the items with anyone else beforehand — inter-rater
> agreement is only meaningful if the two passes are independent.
>
> The two labels per item, and worked examples, are in the page's built-in
> codebook (top of the page). Confidence 1–3, and a free-text note wherever you
> hesitated — the notes are genuinely useful when we adjudicate disagreements.
>
> One item corresponds to a case study already described in the paper draft, so
> you may recognise it; label it as you see it. We report agreement both with
> and without that item.
>
> Roughly 2–3 minutes per item. Thank you again.

---

## If nobody replies

Two fallbacks, in order:

1. **Any careful independent reader.** The decisive number is human–human
   agreement, and it does not require domain expertise: if two careful readers
   also fail to converge, that indicts the label scheme, which is a finding in
   its own right. A colleague or graduate student in any quantitative field can
   supply it in an hour.
2. **Paid domain experts.** Kolabtree and Upwork both list astrophysics PhDs;
   USD 50–150 is a fair rate for an hour of expert labelling. Say up front that
   the labels will be published.
