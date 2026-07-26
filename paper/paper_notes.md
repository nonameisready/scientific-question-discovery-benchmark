# Paper 2 — working notes

## Positioning

Paper 2 does not validate our framework; it defines how the field should
evaluate scientific question discovery. The generation system (Paper 1)
appears only as submission `evidence_graph_v1`.

Three-tier claim structure (deliberate, keep it):

1. **Strong** — we formalize historical backtesting as an evaluation
   protocol for scientific question discovery.
2. **Medium** — we release a reproducible astronomy benchmark instance
   with temporally isolated past and future corpora.
3. **Cautious** — in an initial set of ten questions, all were
   substantively engaged by later literature, including one whose
   underlying premise was subsequently refuted.

Never claim: "AI can reliably identify the most valuable future
scientific questions" (no support for "reliably", "most valuable", or
cross-domain generalization at n=10).

## Numbers (all derived from released data; CI reproduces them)

| Quantity | Value |
|---|---|
| Cutoff | 2020-12-31 |
| Corpus A | 2,512 papers (2015–2020), 500 full-text core |
| Corpus B | 1,891 papers (2021–2026) |
| Questions | 10 frozen |
| Coverage | 10/10 (Clopper–Pearson 95%: [0.69, 1.0]) |
| Answered / partial / open / not addressed | 2 / 7 / 1 / 0 |
| Premise refuted | 1 (q_008) |
| Mean supporting papers | 2.4; multi-source 60% |
| Mean top-1 retrieval similarity | 0.6664 |
| First-engagement lag | mean 2.9 y, range 1–5 (lower bound; NOT lead time) |
| Lead time | null in v1 (no community first-posed dates yet) |

## Figures

- Fig 1 (protocol): system-agnostic pipeline; no Evidence Graph, no
  Question Generator, no LLM in the loop.
- Fig 2 (q_008 timeline): 2017 subsolar retrieval → 2020 frozen question
  → 2025 three independent refutations. TikZ, inline.

## Venue notes

- Emphasize benchmark-paper checklist: protocol + frozen data +
  reproducible pipeline + baselines (defined & shipped; runs on
  roadmap) + human adjudication + one-command metrics + CI.
- Threats section is load-bearing for review; keep contamination
  discussion prominent (weights channel vs retrieval channel;
  prospective instances as the clean endgame).
- Leaderboard table intentionally shows empty baseline rows — honesty
  beats a rushed fill; the harness ships in the repo.

## TODO before submission

- [ ] Author list / affiliations
- [ ] Compile check (no LaTeX toolchain in dev container)
- [ ] Populate at least B2/B3 baseline rows if budget allows
- [ ] Bib entries for post-2021 evidence papers if a venue requires
      formal citations for them (currently referenced by ADS bibcode in
      released data records)
