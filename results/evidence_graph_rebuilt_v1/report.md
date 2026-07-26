# Historical Backtesting Report — astronomy_v1

Protocol v1.0 | cutoff 2020-12-31 | 10 frozen questions

## Headline metrics

| Metric | Value |
|---|---|
| Future attention rate (coverage) | 90% |
| Answered | 10% |
| Partially addressed | 80% |
| Posed but open | 0% |
| Not addressed | 10% |
| Premise refutation rate | 10% |
| Mean supporting papers per engaged question | 2.78 |
| Multi-source evidence rate | 70% |

## Per-question outcomes

### rank 1 — q_002: not_addressed (premise: still_plausible)

**How does terminator heterogeneity affect the statistical evidence for water and the inferred water abundance and C/O ratio in WASP-12 b?**

- rationale: None of the provided post-cutoff abstracts directly engage with the impact of terminator heterogeneity on the statistical evidence for water or the inferred water abundance and C/O ratio in WASP-12b. The premise that terminator heterogeneity could affect these inferences remains plausible but untested in the cited literature.

### rank 2 — q_001: partially_addressed (premise: supported)

**What causes the roughly factor-of-five discrepancy between the ~8 km/s wind inferred from optical sodium and the ~1.7 km/s wind inferred from near-infrared CO/H2O in HD 189733 b: vertical wind shear between the probed atmospheric layers, temporal variability, line-formation differences, or instrumental and analysis systematics?**

- rationale: Post-cutoff literature has made substantial progress by modeling wind structures in HD 189733 b and confirming the presence of vertical wind shear, which supports one of the proposed explanations for the wind speed discrepancy. However, the literature does not fully resolve the factor-of-five discrepancy between optical sodium and near-infrared wind measurements, leaving the core question open.
- [2021PhDT.........4S] This thesis directly models winds in HD 189733 b, finding evidence for zonal winds in the lower and vertical winds in the intermediate atmosphere, supporting the presence of vertical wind shear as a cause for differing wind measurements.
- [2024AJ....167..179B] This paper reanalyzes high-resolution near-infrared data for HD 189733 b and finds a significant blueshift in absorption features, but does not directly compare optical sodium and near-infrared wind measurements or resolve the discrepancy.
- [2021MNRAS.502.4392L] This study confirms sodium detection and blueshift in HD 189733 b, and discusses the impact of telluric and instrumental systematics, but does not directly resolve the wind speed discrepancy between different tracers.

### rank 3 — q_004: partially_addressed (premise: supported)

**Under what atmospheric conditions does HD 189733 b exhibit subsolar water abundances alongside robust carbon monoxide detection in high-dispersion transmission spectra?**

- rationale: Post-cutoff literature (2021AJ....162..233B) directly detects subsolar water vapor in HD 189733 b and discusses its context alongside previous super-solar CO detections, supporting the premise that such atmospheric conditions exist. However, while the study constrains water abundance and references CO, it does not fully resolve the atmospheric conditions (e.g., temperature, cloud properties, C/O ratio) that specifically lead to this combination, leaving the core question open but making substantial progress.
- [2021AJ....162..233B] This study directly detects water vapor in HD 189733 b's atmosphere using high-resolution transmission spectroscopy, finding a slightly subsolar water abundance and referencing previous super-solar CO detections, thus engaging the question of atmospheric conditions for subsolar H2O and robust CO.

### rank 4 — q_008: answered (premise: refuted)

**Is the strongly subsolar terminator water abundance retrieved for HD 209458 b a property of the atmosphere or an artifact of retrieval assumptions, as tested by comparing independent retrieval frameworks on the same and on independent datasets?**

- rationale: Multiple post-cutoff studies directly address the question by applying independent retrieval frameworks to both new and archival data for HD 209458 b, including HST, JWST, and ground-based spectra. These works consistently find that the previously reported strongly subsolar terminator water abundance is not robust to improved data and retrieval assumptions, and that the true water abundance is consistent with solar, refuting the premise that the subsolar value is a real atmospheric property.
- [2025A&A...700A.105B] This study reanalyzes HST and JWST spectra of HD 209458 b with improved systematics treatment and multiple retrieval assumptions, finding a water abundance consistent with solar, not strongly subsolar, and robust to retrieval framework choices.
- [2025AJ....170...69V] This work applies an independent retrieval framework (SANSAR) to HST and JWST data, showing that the retrieved water abundance and metallicity depend on retrieval assumptions, but that solar or near-solar values are favored with modern data and methods.
- [2025AJ....170..223F] High-resolution ground-based spectroscopy and retrievals independently constrain the water abundance in HD 209458 b to be at least solar, consistent with recent JWST results and inconsistent with a strongly subsolar value.

### rank 5 — q_007: partially_addressed (premise: weakened)

**Do patchy-cloud, solar-composition models remain the preferred explanation of the HST/WFC3 transmission spectra of HD 189733 b and HAT-P-11 b when tested with independent retrieval frameworks and broader-wavelength or independent observations?**

- rationale: Recent literature has made substantial progress in testing the robustness of atmospheric retrievals for exoplanets like HD 189733 b and HAT-P-11 b, particularly by highlighting the impact of stellar heterogeneity and parameter degeneracies, and by applying multiple retrieval frameworks to similar systems. However, while these studies cast doubt on the unambiguous preference for patchy-cloud, solar-composition models and stress the need for broader-wavelength and multi-code analyses, they do not definitively resolve whether such models remain preferred for the specific planets in question, leaving the core question open but weakened.
- [2024MNRAS.528.3354F] This study applies three independent retrieval codes to HAT-P-18 b (a similar Saturn-mass planet) using HST/WFC3, JWST, and Spitzer data, finding agreement on sub-solar H2O and a cloud deck, but also highlights the impact of stellar heterogeneity and the need for further investigation into CO2 abundance.
- [2024AJ....167..107N] This work demonstrates that stellar heterogeneity (unocculted spots) on HD 189733 A can mimic or mask planetary atmospheric features, complicating the interpretation of transmission spectra and challenging the robustness of previous cloud/haze inferences.
- [2025MNRAS.538.2521N] This paper discusses parameter degeneracies in HST/WFC3 retrievals, emphasizing the need for broader wavelength coverage and multiple retrieval codes to resolve ambiguities, though it does not directly reanalyze HD 189733 b or HAT-P-11 b.

### rank 6 — q_010: partially_addressed (premise: supported)

**How sensitive is the reported WASP-121 b water detection to cloud opacity, stellar contamination, baseline offsets, retrieval priors, and the selected null model?**

- rationale: Post-cutoff literature (2022MNRAS.512.4618G) directly engages with the sensitivity of WASP-121b atmospheric retrievals to data-processing choices, which relate to baseline offsets and stellar contamination, and demonstrates reliable constraints on atmospheric abundances. However, the abstract does not explicitly address all aspects of the original question, such as the effects of cloud opacity, retrieval priors, or null model selection, leaving the core question only partially addressed while supporting the premise that such sensitivities are important.
- [2022MNRAS.512.4618G] This work presents retrievals on WASP-121b transmission spectra, addressing the impact of data-processing methods (which can be analogous to baseline offsets and stellar contamination) on atmospheric abundance constraints, including water.

### rank 7 — q_005: partially_addressed (premise: supported)

**Do the HST transmission data independently support NH3 or HCN in HD 209458 b, and how does the evidence for each species change under cloud-free, patchy-cloud, and fully cloudy retrieval scenarios?**

- rationale: Post-cutoff literature places strong upper limits on NH3 and HCN in HD 209458 b and reconciles previous conflicting reports, supporting the premise that HST transmission data can constrain these species. However, while these studies address the detectability and abundance of NH3 and HCN, they do not systematically resolve how evidence for each species changes under different cloud scenarios, leaving the core question partially addressed.
- [2025AJ....170..223F] This study provides strong upper limits on NH3 and HCN abundances in HD 209458 b using high-resolution spectroscopy, consistent with recent JWST transmission results, but does not explicitly test different cloud scenarios.
- [2024A&A...690A..63B] This work reports a non-detection of HCN in HD 209458 b from high-resolution ground-based transmission spectra, noting that recent space-based observations also do not detect HCN.
- [2022BAAS...54e.209M] This abstract describes a joint analysis of HD 209458 b's atmosphere, reconciling previous discrepant molecular detections and placing tighter constraints on its chemical composition, including HCN and NH3.
- [2022eas..conf.1751M] This is a duplicate of the previous entry, also describing a joint analysis that addresses the authenticity of HCN and NH3 detections in HD 209458 b.

### rank 8 — q_009: partially_addressed (premise: supported)

**Under what atmospheric conditions do patchy cloud models with solar composition provide robust fits to HST/WFC3 spectra of hot Neptunes and hot Jupiters, without invoking high mean molecular weight or globally uniform clouds?**

- rationale: Post-cutoff literature has made substantial progress in modeling and constraining the effects of patchy clouds with solar composition on the spectra of hot Neptunes and hot Jupiters, including direct application to HST/WFC3 data. However, while patchy cloud models are shown to be plausible and sometimes compatible with observations, the literature does not yet robustly resolve under exactly which atmospheric conditions these models provide the best fits without invoking high mean molecular weight or globally uniform clouds, leaving the core question open.
- [2024MNRAS.530.3100D] This study directly analyzes HST/WFC3 and high-resolution spectra of a warm Neptune, finding that solar-abundance models with a high cloud deck (i.e., patchy or non-uniform clouds) are among the family of models compatible with the data, alongside high-metallicity and globally uniform cloud scenarios.
- [2022ApJ...934...79K] This work uses GCMs to show that patchy cloud distributions are a natural outcome in hot Jupiter atmospheres and discusses their radiative effects, supporting the plausibility of patchy cloud models for fitting spectra.
- [2021ApJ...909...85H] This paper demonstrates that temperature-dependent, spatially inhomogeneous clouds in GCMs significantly affect the emission spectra of hot Jupiters, highlighting the importance of patchy clouds in spectral modeling.

### rank 9 — q_006: partially_addressed (premise: still_plausible)

**Does the >3-sigma exclusion of a carbon-rich (C/O > 1) atmosphere for WASP-12 b survive relaxing the equilibrium-chemistry assumption in retrievals of the same HST/WFC3 transmission spectrum?**

- rationale: Post-cutoff literature directly engages the question by examining the robustness of C/O constraints for WASP-12b from HST/WFC3 spectra, including the effects of model assumptions and parameter degeneracies. However, while these works highlight the challenges and some robustness, they do not definitively resolve whether the >3-sigma exclusion of a carbon-rich atmosphere survives all disequilibrium scenarios, leaving the core question open but substantially advanced.
- [2025MNRAS.538.2521N] This study specifically investigates retrieval degeneracies in HST/WFC3 transmission spectra for WASP-12b, highlighting the challenges in robustly constraining atmospheric parameters such as C/O, especially when relaxing model assumptions.
- [2022ApJ...931...86H] This paper discusses the sensitivity of WASP-12b atmospheric retrievals to model inputs and assumptions, including the impact of adding species relevant to disequilibrium chemistry, but finds that results are mostly data-driven and robust to these changes.

### rank 10 — q_011: partially_addressed (premise: weakened)

**To what extent have actual JWST observations validated pre-launch predictions that aerosol-free TRAPPIST-1 CO2 atmospheres would be detectable within ten NIRSpec Prism transits?**

- rationale: Post-cutoff JWST NIRSpec Prism observations of TRAPPIST-1e and c have directly engaged the question by attempting to detect or constrain CO2 atmospheres, but stellar contamination has so far prevented a definitive detection or exclusion of aerosol-free CO2 atmospheres within the number of transits observed. The premise that such atmospheres would be readily detectable within ten transits is weakened, as the limiting factor is not photon noise but unanticipated stellar heterogeneity, leaving the core question open but with substantial progress and new challenges identified.
- [2024ESS.....562518R] Reports that stellar contamination challenges the precision needed to probe TRAPPIST-1c's atmosphere with NIRSpec Prism, and that substantial CO2-dominated atmospheres are unlikely for TRAPPIST-1c.
- [2025AAS...24521501G] Describes four NIRSpec Prism transits of TRAPPIST-1e, noting significant stellar contamination and laying groundwork for further observations to constrain atmospheric properties.
- [2025ApJ...990L..52E] Presents four NIRSpec Prism spectra of TRAPPIST-1e, rules out H2-dominated atmospheres, and discusses the challenge of stellar contamination, with constraints on secondary atmospheres in a companion paper.
- [2026ASTCS..1160070G] Analyzes NIRSpec Prism spectra of TRAPPIST-1e, finding no strong evidence for or against an atmosphere and only weakly disfavors CO2-rich atmospheres at 2σ, with stellar contamination limiting conclusions.
- [2026AJ....171..105A] Describes a program aiming to detect a CO2 atmosphere on TRAPPIST-1e using NIRSpec Prism, but notes that stellar contamination and flares inhibit confident correction and detection.
