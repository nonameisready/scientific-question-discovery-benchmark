# Historical Backtesting Report — astronomy_v1

Protocol v1.0 | cutoff 2020-12-31 | 10 frozen questions

## Headline metrics

| Metric | Value |
|---|---|
| Future attention rate (coverage) | 70% |
| Answered | 0% |
| Partially addressed | 70% |
| Posed but open | 0% |
| Not addressed | 30% |
| Premise refutation rate | 0% |
| Mean supporting papers per engaged question | 2.57 |
| Multi-source evidence rate | 60% |

## Per-question outcomes

### rank 1 — q_001: not_addressed (premise: still_plausible)

**Is the main result reported in "Optical Properties of Sulfuric Acid" robust to independent reanalysis with different modeling assumptions?**

- rationale: None of the provided abstracts report an independent reanalysis of the main result from 'Optical Properties of Sulfuric Acid' or directly address the robustness of its findings under different modeling assumptions. While several works discuss sulfur chemistry, photochemical hazes, or optical properties of related compounds, none engage with the specific question of reanalyzing sulfuric acid's optical properties or testing the robustness of the original result. The premise remains plausible but untested in the post-cutoff literature provided.

### rank 2 — q_002: partially_addressed (premise: still_plausible)

**Is the main result reported in "Mass-loss rate and local thermodynamic state of the KELT-9 b thermosphere from the hydrogen Balmer series" robust to independent reanalysis with different modeling assumptions?**

- rationale: Post-cutoff literature (2023AJ....165..101L) confirms the presence of Hα excess absorption and ongoing mass loss in KELT-9b, and explores alternative modeling scenarios for the observed transit shape, but does not provide a direct independent reanalysis of the original mass-loss rate using different modeling assumptions. Thus, the robustness of the main result is not fully resolved, but there is substantial directly-relevant progress in confirming the phenomenon and discussing modeling uncertainties.
- [2023AJ....165..101L] This work presents multiepoch Hα observations of KELT-9b, confirming excess absorption and mass loss, and discusses the modeling of the Hα transit with a 'cometary tail' scenario, but does not directly reanalyze the original mass-loss rate with different modeling assumptions.

### rank 3 — q_003: not_addressed (premise: still_plausible)

**Is the main result reported in "Saturn as a Transiting Exoplanet" robust to independent reanalysis with different modeling assumptions?**

- rationale: None of the provided abstracts report an independent reanalysis of the specific result from 'Saturn as a Transiting Exoplanet' or directly address the robustness of its findings under different modeling assumptions. While several works discuss general issues of robustness, reanalysis, and modeling in exoplanet transit studies, none engage with the main result or premise of the referenced study on Saturn as a transiting exoplanet.

### rank 4 — q_004: not_addressed (premise: still_plausible)

**Is the main result reported in "Testing the Detectability of Extraterrestrial O<SUB>2</SUB> with the Extremely Large Telescopes Using Real Data with Real Noise" robust to independent reanalysis with different modeling assumptions?**

- rationale: None of the provided abstracts report an independent reanalysis of the main result from 'Testing the Detectability of Extraterrestrial O2 with the Extremely Large Telescopes Using Real Data with Real Noise' using different modeling assumptions. While some works discuss general robustness and methodological issues in exoplanet atmospheric retrievals, they do not directly engage with or test the specific result or its modeling choices.

### rank 5 — q_005: partially_addressed (premise: supported)

**Is the main result reported in "Constraining Stellar Photospheres as an Essential Step for Transmission Spectroscopy of Small Exoplanets" robust to independent reanalysis with different modeling assumptions?**

- rationale: Multiple post-cutoff studies have independently reanalyzed the impact of stellar photosphere modeling assumptions on exoplanet transmission spectroscopy, confirming that the main result—stellar contamination is a major limiting factor—remains robust, but also showing that the degree of bias and noise depends strongly on the fidelity and assumptions of the stellar models used. While these works make substantial progress in quantifying and mitigating the effects, they do not fully resolve the issue, as significant model discrepancies and challenges in accurately characterizing stellar heterogeneity persist.
- [2024AJ....168...82R] This work directly investigates the robustness of transmission spectroscopy corrections to different stellar models, finding that discrepancies between models can significantly affect the noise budget and advocating for improved stellar modeling.
- [2024ApJ...960..107T] This study uses two independent stellar models to test the impact of stellar contamination on transmission spectra retrievals, confirming that including stellar activity parameters reduces bias, but some limitations remain under high activity.
- [2025ApJ...980L..42P] This paper demonstrates that including additional stellar components (chromospheres/coronae) in modeling can significantly alter retrieved exoplanet atmospheric properties, highlighting sensitivity to modeling assumptions.
- [2024eas..conf.2078C] This abstract presents a new tool for modeling and removing stellar activity effects in transmission spectra, emphasizing the importance of accurate stellar contamination models and their impact on atmospheric inference.

### rank 6 — q_006: partially_addressed (premise: still_plausible)

**Is the main result reported in "On the Temperature Profiles and Emission Spectra of Mini-Neptune Atmospheres" robust to independent reanalysis with different modeling assumptions?**

- rationale: Post-cutoff literature has engaged in independent re-analyses of mini-Neptune and Neptune-size exoplanet atmospheres, using different modeling assumptions and data pipelines to test the robustness of previous results. While these studies have made substantial progress and sometimes broadened the range of plausible models, they have not fully resolved whether the main result of the original study is robust under all alternative modeling frameworks, leaving the core question partially open.
- [2023AAS...24115106B] This work presents a re-analysis of Neptune-size exoplanet atmospheric spectra, directly engaging with the robustness of previously identified trends and modeling assumptions.
- [2024MNRAS.530.3100D] This study re-analyzes GJ 3470 b with a custom pipeline and Bayesian framework, comparing results to previous models and highlighting a broader range of compatible atmospheric models.

### rank 7 — q_007: partially_addressed (premise: still_plausible)

**Is the main result reported in "Atmospheric escape from rocky M-dwarf planets orbiting within the habitable zone" robust to independent reanalysis with different modeling assumptions?**

- rationale: Several post-cutoff studies have directly engaged with the robustness of atmospheric escape predictions for rocky M-dwarf planets, employing new modeling frameworks and considering additional physical processes such as radiative cooling and interior-atmosphere interactions. While these works have advanced the field and tested the sensitivity of escape rates to different assumptions, they have not fully resolved the question of robustness, leaving some core uncertainties open.
- [2022ApJ...934..137Y] This work presents new hydrodynamic escape simulations for terrestrial planets around M dwarfs, showing that escape rates are sensitive to atmospheric composition and radiative cooling, which directly tests and refines the modeling assumptions underlying atmospheric escape predictions.
- [2024AGUFMU13C...01K] This abstract discusses the implications of JWST observations and modeling for atmospheric retention on rocky M-dwarf planets, specifically addressing the robustness of atmospheric escape predictions in the habitable zone.
- [2026absc.conf22103L] This study uses a novel integrated modeling framework to simulate atmospheric stability and escape for rocky planets in M-dwarf habitable zones, directly engaging with the robustness of previous escape models under different assumptions.

### rank 8 — q_008: partially_addressed (premise: still_plausible)

**Is the main result reported in "Planets are Shaped by their Past: Reconstructing the Early XUV Emission of Exoplanet Host Stars" robust to independent reanalysis with different modeling assumptions?**

- rationale: Post-cutoff literature has made substantial progress in identifying and quantifying uncertainties in reconstructing the XUV emission histories of exoplanet host stars, including the effects of stellar rotation, variability, and the timescales of high-energy emission. However, there is no evidence of a direct, independent reanalysis of the specific main result from 'Planets are Shaped by their Past' using alternative modeling assumptions, so the robustness of that particular result remains only partially addressed and the premise is still plausible.
- [2022AN....34310077K] This work explores the impact of diverse stellar XUV histories on exoplanet atmospheric evolution, highlighting uncertainties in reconstructing past XUV emission and its effects on planetary outcomes.
- [2021MNRAS.501L..28K] This study challenges common modeling assumptions about the timescale and evolution of stellar EUV emission, suggesting that previous models may oversimplify the irradiation history relevant to exoplanet atmospheres.
- [2024HEAD...2110734B] This abstract discusses the variability and unpredictability of stellar X-ray emission, which is a key input for reconstructing the high-energy environment of exoplanet host stars.

### rank 9 — q_009: partially_addressed (premise: supported)

**Is the main result reported in "Atmosphere Models of Brown Dwarfs Irradiated by White Dwarfs: Analogs for Hot and Ultrahot Jupiters" robust to independent reanalysis with different modeling assumptions?**

- rationale: Post-cutoff literature has engaged the question by applying independent retrieval frameworks and new data to irradiated brown dwarfs and hot Jupiter analogs, directly testing the predictions and assumptions of atmosphere models. While these studies provide substantial progress in evaluating model robustness and highlight both agreements and limitations, they do not fully resolve all uncertainties, leaving the core question partially addressed and the premise supported.
- [2023AAS...24132402L] This work performs atmospheric retrievals on the same class of irradiated brown dwarfs as the original study, using independent retrieval methods and phase-resolved spectra, and directly compares empirical results to theoretical models, thus testing the robustness of model predictions.
- [2022ApJ...933...79W] This study systematically explores the impact of different modeling assumptions (1D vs. 2D) on atmospheric retrievals for irradiated exoplanets, addressing the robustness of results to modeling choices.

### rank 10 — q_010: partially_addressed (premise: supported)

**Is the main result reported in "Information in the Reflected-light Spectra of Widely Separated Giant Exoplanets" robust to independent reanalysis with different modeling assumptions?**

- rationale: Post-cutoff literature has made substantial progress in independently assessing the robustness of reflected-light spectral retrievals for giant exoplanets to different modeling assumptions, particularly regarding cloud parameterizations and radiative transfer methods. However, while these studies demonstrate that modeling choices can significantly affect inferred properties and identify sources of systematic discrepancies, they do not fully resolve whether the specific main result of the original paper is robust to all plausible independent reanalyses, leaving the core question open but substantially advanced.
- [2021ApJ...910..158M] This study directly investigates how different cloud parameterizations in reflected light retrievals of cool giant exoplanets affect the inferred atmospheric properties, showing that modeling assumptions can significantly alter results.
- [2026asi..confP..21J] This work presents a generalized reflected-light spectra model and systematically compares methodological choices, identifying consistencies and discrepancies with existing models, thus probing the robustness of reflected-light spectral interpretations.
- [2023A&A...678A..41N] This paper examines how data processing algorithms and their parameters impact the accuracy of atmospheric retrievals from reflected-light spectra, highlighting systematic biases and the importance of accounting for correlated noise.
