# Annotation brief — 30 minutes to read, ~1 hour to do
# 标注说明书 —— 3 分钟读完，约 1 小时完成

---

## 1. What you are doing / 你要做什么

You will see **23 research questions**. Each question was written from
literature published **before 2021**. Below each question are **up to 8
abstracts of papers published after it**.

你会看到 **23 个科研问题**。每个问题都是根据 **2021 年以前**的文献写出来的。
每个问题下面是 **最多 8 篇在那之后发表的论文摘要**。

**Your job: decide what the later literature did to that question.**
Two labels per item. About 2–3 minutes each.

**你的任务：判断后来的文献对这个问题做了什么。** 每题两个标签，每题约 2–3 分钟。

---

## 2. Why it matters / 为什么这件事重要

We built a benchmark that scores AI systems on the research questions they
generate. The labels currently come from an LLM. In a first blinded pass, a
non-expert annotator agreed with the LLM **at chance level** (κ = 0.04).

我们做了一个基准，用来评价 AI 提出的科研问题好不好。目前的标签是 LLM 打的。
第一轮盲测中，一位非专业标注者与 LLM 的一致度**处于随机水平**（κ = 0.04）。

We do not know whether the LLM is wrong, that reader was, or our label
definitions are too vague for anyone to apply consistently. **Your independent
pass is the experiment that tells us which.** Please label what you actually
see — a disagreement with the LLM is just as useful to us as an agreement.

我们不知道是 LLM 判错了、那位读者判错了，还是我们的标签定义本身太模糊、
换谁来都统一不了。**你这一遍独立标注，就是能区分这三者的实验。**
请按你真实看到的判断——**你和 LLM 不一致，对我们同样有价值。**

---

## 3. The one rule that matters most / 最重要的一条规则

> ### Same topic is NOT engagement.
> ### 同话题 ≠ 有人研究了这个问题。

An abstract about the same planet, the same molecule, or the same instrument
**does not count** — unless it bears on **the specific thing this question asks
you to test**, or on **the assumption the question rests on**.

一篇摘要讲的是同一颗行星、同一个分子、同一台望远镜，**都不算**。
必须真的碰到**这个问题要检验的那件具体的事**，或者碰到**这个问题所依赖的假设**。

*Example / 例子:* the question asks about CO on **Proxima Centauri b**; an
abstract reports no thick CO₂ atmosphere on **TRAPPIST-1 c**. Same field, same
kind of measurement — but a different planet, so it says nothing about this
question. → `not_addressed`

*问题问的是 **Proxima Centauri b** 上的 CO；摘要报告的是 **TRAPPIST-1 c** 没有
厚 CO₂ 大气。同一领域、同类测量，但不同的行星，对这个问题什么也没说。→ `not_addressed`*

---

## 4. Label 1 — `outcome`: what happened to the question?
## 标签一 —— `outcome`：这个**问题**后来怎么样了？

**Ask these four questions in order. Stop at the first one you can answer.**
**按顺序问自己这四个问题，第一个能回答的就是答案。**

**Q1. Does any abstract bear on this question's actual test, or on its
assumption?**
**问 1：有没有任何一篇摘要，真的碰到了这个问题要检验的事，或它依赖的假设？**

→ **No** ⇒ **`not_addressed`** — stop here. / **没有** ⇒ **`not_addressed`**，到此为止。

**Q2. Could you now state an answer to the question, citing these abstracts?**
**问 2：读完这些摘要，你现在能说出这个问题的答案吗？**

→ **Yes** ⇒ **`answered`** / **能** ⇒ **`answered`**

**Q3. Do the abstracts explicitly raise the same question, without settling it?**
**问 3：这些摘要是不是也提出了同一个问题，但没有解决它？**

→ **Yes** ⇒ **`posed_but_open`** / **是** ⇒ **`posed_but_open`**

**Q4. Otherwise** ⇒ **`partially_addressed`** — real relevant progress, core
question still open.
**问 4：以上都不是** ⇒ **`partially_addressed`** —— 有实质的相关进展，
但核心问题仍未解决。

---

## 5. Label 2 — `premise_status`: what happened to its underlying assumption?
## 标签二 —— `premise_status`：它**依赖的那个假设**怎么样了？

Many questions quietly assume something that could turn out to be false.

很多问题里悄悄埋了一个"可能其实是错的"的前提。

> *"Is the strongly subsolar water abundance of HD 209458 b real, or an
> artifact of retrieval assumptions?"*
> — assumes that a strongly subsolar abundance **was in fact reported**.
> —— 它假设了"确实有人报告过极低含水量"这件事。

**Ask in order / 按顺序问：**

**Q1. Does the question rest on an assumption that could be wrong at all?**
**问 1：这个问题依赖任何一个「可能是错的」假设吗？**

→ **No** ⇒ **`not_applicable`** / **不依赖** ⇒ **`not_applicable`**

**Q2. Do the abstracts actually test that assumption?**
**问 2：这些摘要真的检验了那个假设吗？**

→ **No** ⇒ **`still_plausible`** (untested, not "true") / **没有** ⇒ **`still_plausible`**（是"没被检验"，不是"成立"）

**Q3. If tested — what happened? / 检验了的话，结果是：**

| Result | Label |
|---|---|
| Confirmed / 被证实 | `supported` |
| Falsified / 被证伪 | `refuted` |
| Seriously undermined, not settled / 被严重削弱但未定论 | `weakened` |

**Important / 重要：** a question can be `answered` **because** its assumption
was `refuted`. That combination is expected, not a contradiction.

一个问题可以**正因为**它的假设被推翻而得到解决。`answered` + `refuted`
是合理组合，不是自相矛盾。

---

## 6. Three worked examples / 三个完整例子

**A.**
*Question:* Is HD 209458 b's strongly subsolar water abundance real, or an
artifact of retrieval assumptions?
*Abstracts:* three independent reanalyses, all converging on a solar abundance.
→ **`answered` + `refuted`** — settled, and settled by overturning the
assumption the question challenged.
→ 问题解决了，而且是靠推翻它质疑的那个假设解决的。

**B.**
*Same question.*
*Abstracts:* several papers measuring water in **other** hot Jupiters.
→ **`not_addressed` + `still_plausible`** — same topic, different object;
nothing here bears on this test.
→ 同话题、不同天体，对这个检验没有任何贡献。

**C.**
*Question:* How do inhomogeneous terminators bias retrieved abundances?
*Abstracts:* papers showing the bias exists in general, none resolving the
specific case asked about.
→ **`partially_addressed` + `still_plausible`** — real progress, core question
open, and the assumption was never directly tested.
→ 有实质进展，核心问题未决，假设也没被直接检验。

---

## 7. Four rules / 四条规则

1. **Judge only from the abstracts shown. Do not look the papers up.**
   The LLM saw exactly these abstracts; if you use outside knowledge, the
   comparison is no longer valid. If you happen to know the later history,
   set it aside.
   **只根据显示的摘要判断，不要上网查。** LLM 当时看到的就是这几篇；
   你用了外部知识，这个对比就不成立了。就算你知道后来发生了什么，也请放到一边。

2. **Do not discuss the items with anyone before you finish.**
   Inter-rater agreement only means something if the two passes are independent.
   **标完之前不要和任何人讨论。** 两遍标注必须独立，一致度才有意义。

3. **Use confidence honestly: 1 = unsure, 2 = medium, 3 = confident.**
   Low-confidence items are analysed separately — they are information, not
   failure. Please do use 1 when you mean it.
   **信心度请如实填：1 没把握 / 2 一般 / 3 很有把握。** 低信心的条目会单独分析，
   它们是有用信息，不是失败。该填 1 就填 1。

4. **Write a note wherever you hesitated.** One line on what made it hard is
   genuinely valuable when we adjudicate disagreements.
   **犹豫的地方请写一句备注。** 说明你卡在哪里——在后面仲裁分歧时非常有用。

---

## 8. How to do it / 怎么操作

1. Open **`annotator_2_form_subset.html`** in any browser. It runs **offline**;
   nothing is uploaded.
   用浏览器打开 **`annotator_2_form_subset.html`**，**完全离线**，不上传任何内容。
2. For each item: read the question, read the abstracts, click two labels, set
   confidence, add a note if you hesitated. Chinese translations are shown
   under each English original — **the English is authoritative**.
   每题：读问题 → 读摘要 → 点两个标签 → 选信心度 → 犹豫就写备注。
   中文译文在英文原文下方，**以英文原文为准**。
3. Progress **saves automatically** in your browser. You can close and come back.
   进度**自动保存**在浏览器里，可以关掉再回来。
4. When all 23 are done, click **Export CSV** and send the file back.
   全部完成后点 **Export CSV**，把文件发回。

**What you will NOT see, by design:** which AI system produced which question,
and what the LLM judge answered. That is deliberate — it keeps your pass
independent.

**你看不到（这是刻意的）：** 每个问题是哪个 AI 系统生成的，以及 LLM 裁判怎么判的。
这样才能保证你这一遍是独立的。

---

## 9. One thing to expect / 一个提醒

One of the 23 items corresponds to a case study already described in our paper
draft, so you may recognise it. **Label it as you see it.** We report agreement
both with and without that item.

23 题里有一题对应我们论文草稿中已描述的一个案例，你可能会认出来。
**照你看到的标就行。** 我们会同时报告包含和剔除这一题的结果。

---

## 10. Scope, and how your labels will be used
## 10. 工作范围与你的标注将被如何使用

**Scope:** all **90 items**, in the order given. Roughly 2–3 minutes each, so
about 3.5–4 hours in total. You can stop and resume freely; progress is saved
in your browser. If you can only finish part of it, **stop at a whole item**
and send what you have — partial sheets are usable, and we report exactly how
many items were labelled.

**范围：** 全部 **90 题**，按给定顺序。每题约 2–3 分钟，合计约 3.5–4 小时。
可随时中断续做，进度存在浏览器里。如果只能做一部分，**请在一整题结束处停下**
并把已完成的发回——部分标注同样可用，我们会如实报告标注了多少题。

**How the labels are used:** they are the human reference against which we
measure an LLM judge. They will be **published** with the paper and the public
repository, attributed to you or anonymised — **your choice, tell us which**.
Your individual labels, including any that disagree with the model, will appear
in the released data.

**标注的用途：** 它们是用来检验 LLM 裁判的人类参照。这些标注会随论文和公开仓库
**一并发布**，署你的名字或匿名——**由你决定，请告诉我们**。你的每一条标注，
包括与模型不一致的那些，都会出现在公开数据中。

**What we will not do:** we will not adjust, filter, or re-label your entries to
improve agreement with the model. If your labels disagree with the LLM, that is
the result, and it gets reported as the result.

**我们不会做的事：** 我们不会为了提高与模型的一致度而修改、筛选或重标你的条目。
如果你的标注与 LLM 不一致，那就是结果，我们就照结果报告。

---

*Questions about the task are welcome at any point — but please ask before you
start rather than midway, so your pass stays uniform.*

*任何关于任务本身的疑问随时欢迎——但请在开始之前问，不要标到一半再问，
以保证你这一遍的标准前后一致。*
