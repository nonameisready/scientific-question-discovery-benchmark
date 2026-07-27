# Historical Backtesting Report — astronomy_v1L

Protocol v1.0 | cutoff 2020-12-31 | 10 frozen questions

## Headline metrics

| Metric | Value |
|---|---|
| Future attention rate (coverage) | 80% |
| Answered | 30% |
| Partially addressed | 50% |
| Posed but open | 0% |
| Not addressed | 20% |
| Premise refutation rate | 10% |
| Mean supporting papers per engaged question | 2.5 |
| Multi-source evidence rate | 70% |

## Per-question outcomes

### rank 1 — q_002: not_addressed (premise: still_plausible)

**How does terminator heterogeneity affect the statistical evidence for water and the inferred water abundance and C/O ratio in WASP-12 b?**

- rationale: None of the provided post-cutoff abstracts directly engage with the effect of terminator heterogeneity on the statistical evidence for water or the inferred water abundance and C/O ratio in WASP-12b. The closest relevant work (2022ApJ...931...86H) discusses retrieval uncertainties for WASP-12b but does not consider spatial (terminator) heterogeneity, leaving the core question unaddressed and its premise untested.

### rank 2 — q_001: not_addressed (premise: still_plausible)

**What causes the roughly factor-of-five discrepancy between the ~8 km/s wind inferred from optical sodium and the ~1.7 km/s wind inferred from near-infrared CO/H2O in HD 189733 b: vertical wind shear between the probed atmospheric layers, temporal variability, line-formation differences, or instrumental and analysis systematics?**

- rationale: None of the provided post-cutoff abstracts substantively engage with the specific question of the factor-of-five wind speed discrepancy between optical sodium and near-infrared CO/H2O in HD 189733 b or its possible causes. The premise that such a discrepancy exists and requires explanation remains plausible, as it is neither directly tested nor refuted in the cited literature.

### rank 3 — q_004: answered (premise: supported)

**Under what atmospheric conditions does HD 189733 b exhibit subsolar water abundances alongside robust carbon monoxide detection in high-dispersion transmission spectra?**

- rationale: Multiple post-cutoff studies (2024AJ....167...43F, 2024AAS...24341504F, 2024Natur.632..752F) directly measure and interpret the atmospheric conditions—metallicity, C/O ratio, and molecular abundances—under which HD 189733 b exhibits subsolar water and robust CO in high-dispersion spectra. These works resolve the question by providing quantitative constraints and linking the observed abundances to atmospheric metallicity and formation history, thus supporting the premise and answering the question.
- [2024AJ....167...43F] This study uses high-resolution emission spectra and retrievals to directly measure subsolar water abundances and robust CO detection in HD 189733 b, linking these to atmospheric metallicity and C/O ratio.
- [2024AAS...24341504F] This abstract reports similar results as 2024AJ....167...43F, confirming subsolar water, robust CO, and a low C/O ratio, and discusses the atmospheric conditions and formation implications.
- [2024Natur.632..752F] This paper presents transmission spectra detecting H2O and CO, infers a metal-enriched atmosphere, and provides constraints on C/O and metallicity, directly addressing the atmospheric conditions for the observed molecular abundances.

### rank 4 — q_008: answered (premise: refuted)

**Is the strongly subsolar terminator water abundance retrieved for HD 209458 b a property of the atmosphere or an artifact of retrieval assumptions, as tested by comparing independent retrieval frameworks on the same and on independent datasets?**

- rationale: Multiple independent post-cutoff studies using both new and archival HST and JWST data, as well as ground-based high-resolution spectra, have directly tested the water abundance at the terminator of HD 209458 b using different retrieval frameworks and improved systematics treatment. These studies consistently find that the previously reported strongly subsolar water abundance is not supported, and that the true abundance is consistent with solar or mildly subsolar values, demonstrating that the earlier result was an artifact of retrieval assumptions rather than a property of the atmosphere.
- [2025A&A...700A.105B] This study reanalyzes HST and JWST spectra of HD 209458 b with improved systematics treatment and multiple retrieval assumptions, finding a water abundance consistent with solar, not strongly subsolar, and robust to retrieval framework choices.
- [2025AJ....170...69V] This work applies an independent retrieval framework (SANSAR) to HST and JWST data, showing that the retrieved water abundance and metallicity depend on retrieval assumptions, but overall results are consistent with solar or subsolar values, not strongly subsolar as previously claimed.
- [2025AJ....170..223F] High-resolution ground-based spectroscopy and retrievals confirm a solar or higher water abundance for HD 209458 b, consistent with recent JWST results and inconsistent with a strongly subsolar value.

### rank 5 — q_007: partially_addressed (premise: weakened)

**Do patchy-cloud, solar-composition models remain the preferred explanation of the HST/WFC3 transmission spectra of HD 189733 b and HAT-P-11 b when tested with independent retrieval frameworks and broader-wavelength or independent observations?**

- rationale: Recent literature has directly engaged with the question by applying independent retrieval frameworks and broader-wavelength observations to the transmission spectra of HD 189733 b and HAT-P-11 b analogs, and by explicitly modeling both planetary clouds and stellar heterogeneity. These studies reveal that stellar contamination, particularly from extensive starspots, is a major confounding factor, weakening the premise that patchy-cloud, solar-composition models alone are the preferred explanation; however, the core question remains open as no definitive alternative model has been universally established.
- [2024MNRAS.528.3354F] This study reanalyzes HAT-P-18 b's transmission spectra with HST/WFC3, Spitzer, and JWST, using three independent retrieval codes and explicitly models both clouds and stellar heterogeneity, finding sub-solar water and a cloud deck, but also significant stellar contamination.
- [2024AJ....167..107N] This work on HD 189733 A uses HST data to show that stellar spots are extensive and axisymmetrically distributed, directly challenging the interpretation of transmission spectra features as solely due to planetary clouds.
- [2024tsc3.confE...5N] This conference abstract reinforces the finding of high spot coverage on HD 189733 A, emphasizing the need to account for stellar heterogeneity in transmission spectra analysis.

### rank 6 — q_010: partially_addressed (premise: supported)

**How sensitive is the reported WASP-121 b water detection to cloud opacity, stellar contamination, baseline offsets, retrieval priors, and the selected null model?**

- rationale: The post-cutoff literature (2022MNRAS.512.4618G) directly engages with retrievals of WASP-121b's atmosphere, including water abundance, and discusses how data-processing methods (which relate to baseline offsets and stellar contamination) affect the results. However, it does not systematically or comprehensively address the full sensitivity of the water detection to all the factors listed in the question (cloud opacity, retrieval priors, null model selection), so the question is only partially addressed and the premise remains supported.
- [2022MNRAS.512.4618G] This work performs retrievals on WASP-121b transmission spectra, addressing the impact of data-processing methods (which can include baseline offsets and stellar contamination) on atmospheric abundance constraints, including water.

### rank 7 — q_005: answered (premise: weakened)

**Do the HST transmission data independently support NH3 or HCN in HD 209458 b, and how does the evidence for each species change under cloud-free, patchy-cloud, and fully cloudy retrieval scenarios?**

- rationale: Recent high-resolution transmission spectroscopy studies of HD 209458 b have placed stringent upper limits on both NH3 and HCN, with no detections in the HST or ground-based data, and these results are consistent across retrieval scenarios. This substantially resolves the question, showing that the evidence for both NH3 and HCN is weak or absent, thus weakening the premise that HST transmission data support their presence under any cloud scenario.
- [2025AJ....170..223F] This study provides strong upper limits on NH3 and HCN abundances in HD 209458 b using high-resolution spectroscopy, finding no evidence for either species and noting consistency with recent JWST transmission results.
- [2024A&A...690A..63B] This work reports a non-detection of HCN in HD 209458 b from high-resolution ground-based transmission spectra, despite previous claims, and discusses the implications for atmospheric composition.

### rank 8 — q_009: partially_addressed (premise: supported)

**Under what atmospheric conditions do patchy cloud models with solar composition provide robust fits to HST/WFC3 spectra of hot Neptunes and hot Jupiters, without invoking high mean molecular weight or globally uniform clouds?**

- rationale: Recent literature has made substantial progress by coupling 3D general circulation models with microphysical cloud models to simulate patchy clouds in hot Jupiter atmospheres, and has shown that such models can explain observed spectra under certain atmospheric conditions. However, while these studies support the premise and provide strong evidence that patchy, solar-composition clouds can fit HST/WFC3 spectra without invoking high mean molecular weight or globally uniform clouds, they do not fully resolve the range of atmospheric conditions for robust fits, leaving the core question partially open.
- [2025AAS...24521303F] This work couples 3D GCM and 1D microphysical cloud models to simulate patchy mineral clouds on hot Jupiters, finding that such clouds can explain observed spectra without invoking high mean molecular weight or globally uniform clouds.
- [2025epsc.conf..420F] This study uses coupled microphysical and hydrodynamical models to investigate patchy clouds on WASP-43b and WASP-121b, directly addressing the atmospheric conditions under which patchy clouds affect observable spectra.
- [2022ApJ...934...79K] This paper finds that partial (patchy) cloud coverage is a ubiquitous outcome in GCM simulations of ultra-hot Jupiters, set by atmospheric dynamics and cloud condensation, supporting the plausibility of patchy cloud models.

### rank 9 — q_006: partially_addressed (premise: still_plausible)

**Does the >3-sigma exclusion of a carbon-rich (C/O > 1) atmosphere for WASP-12 b survive relaxing the equilibrium-chemistry assumption in retrievals of the same HST/WFC3 transmission spectrum?**

- rationale: Post-cutoff literature has directly engaged with the reliability of C/O constraints from HST/WFC3 transmission spectra for WASP-12b, emphasizing the impact of retrieval degeneracies and model assumptions. However, while these works highlight the need for caution and further study, they do not definitively resolve whether the >3-sigma exclusion of a carbon-rich atmosphere survives when relaxing the equilibrium-chemistry assumption, leaving the core question open but substantially advanced.
- [2025MNRAS.538.2521N] This study specifically investigates retrieval degeneracies in HST/WFC3 transmission spectra for exoplanets including WASP-12b, highlighting the sensitivity of C/O constraints to model assumptions and parameter degeneracies.
- [2022ApJ...931...86H] This paper discusses the robustness of atmospheric retrievals for WASP-12b, noting that results are mostly data-driven and not strongly affected by the inclusion of additional species, but does not directly test the effect of relaxing equilibrium chemistry on the C/O constraint.

### rank 10 — q_011: partially_addressed (premise: still_plausible)

**To what extent have actual JWST observations validated pre-launch predictions that aerosol-free TRAPPIST-1 CO2 atmospheres would be detectable within ten NIRSpec Prism transits?**

- rationale: Post-cutoff literature reports initial JWST NIRSpec Prism transit observations of TRAPPIST-1e, with preliminary analyses placing constraints on atmospheric composition and mean molecular mass, but do not yet provide a definitive detection or nondetection of an aerosol-free CO2 atmosphere within ten transits. The underlying premise—that such atmospheres could be detectable with JWST—remains plausible, as the main limitation so far is stellar contamination rather than a fundamental observational refutation.
- [2025AAS...24521501G] This abstract reports on four JWST NIRSpec Prism transits of TRAPPIST-1e, providing preliminary constraints on the mean molecular mass of any potential atmosphere and discussing the groundwork for further observations.
- [2025ApJ...990L..52E] This work presents four JWST/NIRSpec Prism transmission spectra of TRAPPIST-1e, rules out H2-dominated atmospheres, and notes that constraints on possible secondary atmospheres (such as CO2) are presented in a companion paper.
- [2026AJ....171..105A] This abstract describes the motivation and first three JWST observations of a program aiming to detect a CO2 atmosphere on TRAPPIST-1e, but notes that stellar contamination remains a significant challenge.
