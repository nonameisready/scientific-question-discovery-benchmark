# Historical Backtesting Report — astronomy_v1

Protocol v1.0 | cutoff 2020-12-31 | 10 frozen questions

## Headline metrics

| Metric | Value |
|---|---|
| Future attention rate (coverage) | 100% |
| Answered | 30% |
| Partially addressed | 70% |
| Posed but open | 0% |
| Not addressed | 0% |
| Premise refutation rate | 0% |
| Mean supporting papers per engaged question | 2.9 |
| Multi-source evidence rate | 80% |

## Per-question outcomes

### rank 1 — q_001: answered (premise: supported)

**Does the central conclusion of the highly cited study "Seven temperate terrestrial planets around the nearby ultracool dwarf star TRAPPIST-1" hold under independent datasets and alternative analysis assumptions?**

- rationale: Multiple independent studies and reviews, using new datasets (Spitzer, HST, K2, JWST) and alternative analysis methods, have confirmed the central conclusion of the original TRAPPIST-1 discovery: seven temperate, Earth-sized, rocky planets orbit the ultracool dwarf star in a compact, resonant system. The premise of the original study is strongly supported by these subsequent investigations, which have refined but not overturned its core findings.
- [2021PSJ.....2....1A] This study uses an expanded and independent dataset (Spitzer, HST, K2) and alternative analysis (N-body, photodynamical) to confirm the existence, masses, radii, densities, and orbital architecture of all seven TRAPPIST-1 planets, supporting the original study's central claims.
- [2024arXiv240111815G] This review summarizes multiple independent follow-up studies, confirming the seven Earth-sized, rocky planets in compact orbits, their mass-radius relation, and the lack of extended primary atmospheres, all consistent with the original discovery.
- [2021AstHe.114..617H] This review reiterates the existence of seven temperate terrestrial planets around TRAPPIST-1, their near-resonant orbits, and rocky nature, based on accumulated evidence since the original discovery.

### rank 2 — q_002: partially_addressed (premise: supported)

**Does the central conclusion of the highly cited study "A Framework for Prioritizing the TESS Planetary Candidates Most Amenable to Atmospheric Characterization" hold under independent datasets and alternative analysis assumptions?**

- rationale: Post-cutoff literature has independently applied, validated, and extended the prioritization framework for TESS planetary candidates using new datasets and alternative analysis methods, confirming its core utility and approach. However, while these studies support and refine the framework, they do not fully close the question of its universal validity under all possible datasets and assumptions, leaving some aspects open for further investigation.
- [2024AJ....167..233H] This study independently identifies and validates top TESS planetary candidates for atmospheric characterization using updated datasets and analysis, directly engaging with the prioritization framework's core conclusions.
- [2023AAS...24115203H] This work validates TESS planet candidates for atmospheric characterization using independent vetting and statistical validation, applying similar metrics as the original framework and confirming the utility of such prioritization.
- [2021PhDT........15W] This thesis investigates the robustness of model assumptions in atmospheric retrievals, directly addressing the reliability of frameworks for prioritizing exoplanet targets.

### rank 3 — q_003: partially_addressed (premise: supported)

**Does the central conclusion of the highly cited study "petitRADTRANS. A Python radiative transfer package for exoplanet characterization and retrieval" hold under independent datasets and alternative analysis assumptions?**

- rationale: Post-cutoff literature demonstrates that petitRADTRANS has been independently benchmarked against other radiative transfer codes, and its outputs are consistent with those from alternative frameworks, supporting the reliability of its central conclusions. However, while these works show substantial validation and widespread adoption, they do not explicitly test the code's conclusions under a wide variety of independent datasets and alternative analysis assumptions, leaving the core question only partially addressed.
- [2021MNRAS.505.2675C] This work benchmarks the PYRAT BAY framework by reproducing spectra consistent with PETITRADTRANS models, indicating independent validation of the code's outputs.
- [2024JOSS....9.5875N] This abstract notes that petitRADTRANS has been benchmarked against numerous similar tools and is widely used for atmospheric retrievals on a range of exoplanet data.

### rank 4 — q_004: partially_addressed (premise: supported)

**Does the central conclusion of the highly cited study "The ExoMol database: Molecular line lists for exoplanet and other hot atmospheres" hold under independent datasets and alternative analysis assumptions?**

- rationale: Post-cutoff literature has directly engaged with the reliability and completeness of the ExoMol database by comparing its line lists to alternatives and quantifying the impact of line list choice on atmospheric retrievals and model outputs. While these studies support the utility and central role of ExoMol, they also reveal that systematic uncertainties due to line list differences remain significant, so the core question of ExoMol's definitive accuracy under all conditions is not fully resolved.
- [2026ApJ...997..118Y] This study explicitly tests the robustness of atmospheric retrievals against different CO line lists (including ExoMol), finding that line list systematics are the dominant source of uncertainty, thus directly engaging with the reliability of ExoMol's central conclusions under alternative assumptions.
- [2021ApJS..254...34G] This work compares absorption cross sections calculated from different line lists (including ExoMol) and reports significant variations in theoretical spectra, highlighting the impact of line list choice on atmospheric modeling.
- [2021isms.confEWF04G] This abstract discusses the existence of multiple cross-section datasets (including ExoMol) and the resulting biases and inaccuracies in atmospheric interpretation, directly addressing the reliability and completeness of such databases.

### rank 5 — q_005: partially_addressed (premise: supported)

**Does the central conclusion of the highly cited study "The Transit Light Source Effect: False Spectral Features and Incorrect Densities for M-dwarf Transiting Planets" hold under independent datasets and alternative analysis assumptions?**

- rationale: Multiple post-cutoff studies independently confirm that the transit light source effect and stellar contamination can induce spurious features and biases in exoplanet transmission spectra, especially for M-dwarf hosts, supporting the central premise of the original study. However, while these works provide substantial progress in quantifying, modeling, and mitigating the effect, they do not fully resolve the issue across all datasets and analysis assumptions, leaving the core question partially open.
- [2022AJ....163..231G] This study models the impact of stellar activity on transit spectroscopy for M-dwarfs, confirming that stellar contamination can induce planetary-like features and offsets in measured planet radii, supporting the original study's premise.
- [2023AAS...24231205W] This work quantifies the Transit Light Source Effect for an active M-dwarf, independently constraining spot parameters and discussing their bias on transmission spectra, directly engaging with the core issue.
- [2026A&A...706A.281S] This paper tests the limitations of simplified stellar contamination models (including the Rackham-TLSE prescription) and finds significant differences in corrections for M-dwarfs, confirming the importance of the effect and the need for more sophisticated modeling.
- [2024AAS...24440705D] This abstract discusses the need to account for stellar activity and photospheric complexity in M-dwarf hosts to avoid biases in transmission spectra, extending the original study's concerns to future ELT observations.

### rank 6 — q_006: partially_addressed (premise: supported)

**Does the central conclusion of the highly cited study "Characterizing Transiting Exoplanet Atmospheres with JWST" hold under independent datasets and alternative analysis assumptions?**

- rationale: Multiple post-cutoff studies directly engage with the robustness of JWST-based exoplanet atmospheric characterizations to independent datasets and alternative analysis assumptions, including pipeline and model choices. These works show that while some atmospheric parameters and conclusions are robust, others are sensitive to analysis details, indicating substantial progress but not a full resolution of the question.
- [2025A&A...704A.223S] This study directly tests the robustness of JWST-based exoplanet atmospheric retrievals to different data reduction pipelines and spectral perturbations, finding some parameters are stable while others are sensitive to analysis choices.
- [2025epsc.conf.1005R] This work compares exoplanet transmission spectra and atmospheric retrievals derived from the same JWST dataset processed through multiple pipelines, highlighting the impact of analysis assumptions.
- [2023nova.pres10547C] This abstract discusses how different data reduction and retrieval pipelines can lead to different conclusions about exoplanet atmospheres from JWST data, emphasizing the importance of analysis assumptions.
- [2024ESS.....562704N] This study demonstrates that model uncertainty can significantly affect atmospheric property inferences, showing that conclusions from JWST and HST data depend on the ensemble of models considered.
- [2024AAS...24331403D] This work finds that for WASP-39 b, the main atmospheric properties inferred from JWST spectra are robust to current opacity model uncertainties, supporting the reliability of some key conclusions.

### rank 7 — q_007: answered (premise: supported)

**Does the central conclusion of the highly cited study "Stellar Flares from the First TESS Data Release: Exploring a New Sample of M Dwarfs" hold under independent datasets and alternative analysis assumptions?**

- rationale: The 2026ApJ...998..173C paper directly tests the flare frequency distributions of M dwarfs using new TESS data and alternative analysis methods, finding results that are consistent with the central conclusion of the original study. This constitutes an independent confirmation, supporting the premise and resolving the question.
- [2026ApJ...998..173C] This study uses independent TESS datasets and alternative analysis assumptions to measure flare frequency distributions in M dwarfs, finding power-law exponents consistent with those reported in the original highly cited study, thus confirming its central conclusion.

### rank 8 — q_008: partially_addressed (premise: weakened)

**Does the central conclusion of the highly cited study "Exoplanetary Atmospheres: Key Insights, Challenges, and Prospects" hold under independent datasets and alternative analysis assumptions?**

- rationale: Post-cutoff literature has made substantial progress in testing the robustness of exoplanet atmospheric inferences under new datasets (notably JWST) and alternative modeling assumptions, revealing that conclusions can be highly sensitive to these factors. While this work has not fully resolved the question—since the field now recognizes fundamental limitations and the need for new frameworks—it has weakened the premise that previous central conclusions are robust, and has advanced understanding of the challenges involved.
- [2026AAS...24715209W] This abstract directly questions the robustness of atmospheric inferences in exoplanet science, showing that independent datasets (e.g., JWST for K2-18 b) and alternative model assumptions can lead to irreconcilably different conclusions, thus challenging the central conclusion of earlier studies.
- [2021PhDT........15W] This thesis investigates the robustness of model assumptions in exoplanet atmospheric retrievals, systematically exploring how different assumptions and degeneracies affect inferred properties, directly engaging with the question of whether previous conclusions hold under alternative analyses.
- [2021RNAAS...5..265W] This note discusses pitfalls and statistical interpretation issues in exoplanet atmosphere analyses, highlighting the importance of careful model comparison and the potential for misleading conclusions under different assumptions.
- [2022BAAS...54e.400E] This abstract reviews population studies of exoplanet atmospheres, noting both key findings and significant limitations and biases in current analysis methods, thus addressing the reliability of central conclusions from earlier work.

### rank 9 — q_009: partially_addressed (premise: supported)

**Does the central conclusion of the highly cited study "Helium in the eroding atmosphere of an exoplanet" hold under independent datasets and alternative analysis assumptions?**

- rationale: Post-cutoff literature has engaged the question by applying independent datasets and alternative analysis frameworks to helium detections in exoplanet atmospheres, confirming some results, finding contradictions, and highlighting the need for improved models. While these studies support the premise that helium is a robust tracer of atmospheric escape, they also reveal complexities and uncertainties, so the central conclusion is not fully resolved but is substantially advanced.
- [2023A&A...677A.164A] This study conducts a homogeneous search for helium in the atmospheres of 11 gas giant exoplanets, confirming some previous detections and noting contradictions with earlier results, thus directly engaging with the reproducibility and robustness of helium detections in exoplanet atmospheres.
- [2025AJ....169..204Z] This work uses independent JWST and Keck/NIRSPEC datasets to constrain helium in exoplanet atmospheres, demonstrating the diagnostic power and sensitivity of helium observations to atmospheric properties, and thus tests the central premise of helium-based atmospheric escape studies.
- [2026ApJ...996L..23D] This paper reanalyzes JWST data for HD 209458 b, showing that helium-rich atmospheres may be misinterpreted under standard analysis frameworks, and calls for alternative modeling approaches, directly addressing the robustness of helium detection and interpretation.

### rank 10 — q_010: answered (premise: supported)

**Does the central conclusion of the highly cited study "2018 Census of Interstellar, Circumstellar, Extragalactic, Protoplanetary Disk, and Exoplanetary Molecules" hold under independent datasets and alternative analysis assumptions?**

- rationale: The 2022 census (2022ApJS..259...30M) independently updates and extends the molecular inventory using new data and analysis, confirming the central conclusion of the 2018 study regarding the diversity and detection of molecules in these environments. The premise that such a census is robust and reproducible is supported by the new, consistent results from an independent dataset and analysis.
- [2022ApJS..259...30M] This work presents an updated, independent census of interstellar, circumstellar, extragalactic, protoplanetary disk, and exoplanetary molecules, directly replicating and extending the methodology of the 2018 study.
