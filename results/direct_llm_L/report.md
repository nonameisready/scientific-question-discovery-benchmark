# Historical Backtesting Report — astronomy_v1L

Protocol v1.0 | cutoff 2020-12-31 | 125 frozen questions

## Headline metrics

| Metric | Value |
|---|---|
| Future attention rate (coverage) | 96% |
| Answered | 15% |
| Partially addressed | 79% |
| Posed but open | 2% |
| Not addressed | 4% |
| Premise refutation rate | 0% |
| Mean supporting papers per engaged question | 3.92 |
| Multi-source evidence rate | 94% |

## Per-question outcomes

### rank 1 — q_001: partially_addressed (premise: supported)

**How do photochemical hazes and clouds in exoplanet atmospheres, especially those around M dwarfs and ultra-hot Jupiters, affect the interpretation of transmission and emission spectra, and what are the dominant microphysical processes governing their formation and vertical distribution?**

- rationale: Post-cutoff literature has made substantial progress in quantifying how photochemical hazes and clouds affect the interpretation of exoplanet spectra, especially for hot Jupiters, and has advanced understanding of the microphysical processes (e.g., formation, transport, sedimentation) that govern their vertical distribution. However, while these studies have clarified many aspects and demonstrated the importance of including haze/cloud physics in models, the dominant microphysical processes and their parameterization remain incompletely resolved, and the question is not fully answered for all exoplanet classes (e.g., M dwarfs, ultra-hot Jupiters).
- [2021MNRAS.502.5643L] Directly investigates the impact of photochemical hazes on the thermal structure and spectra of hot Jupiters, showing their significant effect on transmission and emission spectra.
- [2023ApJ...951..117S] Presents 3D GCM simulations including photochemical hazes, demonstrating their dramatic influence on temperature structure, circulation, and spectral features.
- [2021MNRAS.504.2783S] Explores the 3D transport and vertical distribution of photochemical hazes in a hot Jupiter, linking microphysical processes (settling, transport) to spectral signatures.
- [2022BAAS...54e5302Y] Uses laboratory experiments and data analysis to constrain haze formation and removal rates in temperate exoplanet atmospheres, addressing microphysical processes.
- [2021ApJ...909...85H] Models the effect of clouds on emission spectra and shows how cloud vertical extent and thickness alter spectral features, relevant to the interpretation of spectra.

### rank 2 — q_002: answered (premise: supported)

**What is the efficiency of atmospheric escape driven by XUV irradiation for young, close-in exoplanets, and how does this efficiency depend on planet mass, composition, and stellar activity history?**

- rationale: Multiple post-cutoff studies directly quantify and model the efficiency of XUV/EUV-driven atmospheric escape for young, close-in exoplanets, explicitly addressing its dependence on planet mass, composition, and stellar activity. These works provide analytic, simulation, and observational frameworks that substantially resolve the question, confirming the premise that escape efficiency is not constant but varies systematically with planetary and stellar properties.
- [2022A&A...663A.122C] This study quantitatively investigates the dependence of atmospheric escape efficiency on planet mass (via gravitational potential), composition, and stellar XUV irradiation, providing analytic and simulation-based results for a wide range of exoplanet types.
- [2025A&A...695A.153M] Presents a physically motivated analytic model for EUV-driven escape efficiency, validated against hydrodynamic simulations, and explores how efficiency varies with planetary and stellar parameters.
- [2024EPSC...17..198M] Derives analytic formulae for mass-loss rate and efficiency driven by EUV photoionization, showing dependence on planetary mass, composition, and irradiation, and connects theory to observations.
- [2023IAUS..370..155M] Classifies hydrodynamic escape regimes for close-in planets based on physical conditions, linking escape efficiency to planetary and stellar properties.
- [2024eas..conf.1848M] Provides a theoretical framework for classifying escape regimes and efficiency based on the ratio of characteristic to equilibrium temperature, directly addressing the dependence on planetary and stellar parameters.

### rank 3 — q_003: partially_addressed (premise: supported)

**To what extent do magma-atmosphere interactions and magma ocean crystallization timescales set the volatile inventory and atmospheric composition of super-Earths and sub-Neptunes, and how does this process contribute to the observed radius gap?**

- rationale: Post-cutoff literature has made substantial progress in modeling and quantifying the effects of magma-atmosphere interactions and magma ocean crystallization on volatile inventories and atmospheric compositions of super-Earths and sub-Neptunes. However, while these studies clarify mechanisms and their demographic consequences, the core question of how these processes quantitatively set the observed radius gap remains open, as no single work fully resolves the causal link between interior processes and the radius distribution.
- [2026arXiv260614646T] This work presents a unified evolution model that self-consistently couples magma ocean crystallization, volatile partitioning, and atmospheric loss, directly addressing how these processes affect radius evolution and the volatile inventory of super-Earths and sub-Neptunes.
- [2024ApJ...975...14S] This study models atmosphere-magma chemical equilibrium and shows how magma ocean properties and volatile interactions set atmospheric composition in sub-Neptunes, relevant to the radius gap.
- [2026ApJ...999..178W] This paper extends chemical equilibrium models to include non-ideal mixing in magma oceans and atmospheres, quantifying how volatile partitioning is affected in super-Earths and sub-Neptunes.
- [2021EPSC...15..157F] This abstract proposes a model for the mass-radius relation of sub-Neptunes that includes the effect of gas dissolution in magma oceans, linking magma-atmosphere interactions to the observed radius gap.
- [2024AAS...24313305M] This work discusses the importance of magma-atmosphere interactions for interpreting the radius valley and atmospheric composition of sub-Neptunes, highlighting the need to include these processes in models.

### rank 4 — q_004: partially_addressed (premise: supported)

**How do stellar magnetic activity and unocculted star spots impact the accuracy of exoplanet transmission and emission spectra, particularly for small planets orbiting active M dwarfs, and what are the best methods to correct for these effects?**

- rationale: Post-cutoff literature has made substantial progress in quantifying and mitigating the impact of stellar magnetic activity and unocculted star spots on exoplanet transmission spectra, especially for M dwarfs. Several studies propose and test new correction methods (e.g., mid-IR observations, advanced retrieval frameworks, and spectral libraries), but the problem is not fully resolved, as the effectiveness of these methods can depend on stellar activity levels and spot coverage, leaving the core challenge open.
- [2024ApJ...970..155S] Directly investigates how stellar magnetic activity (spots and faculae) contaminates exoplanet transmission spectra for M dwarfs and demonstrates that mid-infrared observations can partially mitigate these effects.
- [2024ApJ...960..107T] Presents and tests retrieval frameworks that explicitly model and correct for stellar activity (spots and faculae) in exoplanet transmission spectra, showing that including stellar parameters reduces bias.
- [2024eas..conf.2078C] Describes a new tool (SAGE) for modeling and removing time-dependent stellar activity contamination in transmission spectra, accounting for spot position, limb-darkening, and rotational broadening.
- [2023jwst.prop.3593S] Proposes the creation of a spectral library for star spots and faculae on M and K stars to improve modeling and correction of magnetic contamination in exoplanet transmission spectra.

### rank 5 — q_005: partially_addressed (premise: supported)

**What are the dominant mechanisms and timescales for atmospheric loss on terrestrial exoplanets in the habitable zones of M dwarfs, and how do stellar wind and magnetic field interactions influence their long-term habitability?**

- rationale: Post-cutoff literature has made substantial progress in modeling and quantifying the mechanisms and timescales of atmospheric loss for terrestrial exoplanets in M dwarf habitable zones, particularly through advanced MHD simulations and analytic frameworks that directly address the roles of stellar wind and magnetic field interactions. However, while these studies provide predictive insights and analytic relations, the core question of dominant mechanisms and their precise impact on long-term habitability remains open, as the field continues to grapple with uncertainties in volatile inventories and the diversity of exoplanetary and stellar properties.
- [2025ApJ...994L..50L] Directly models atmospheric ion escape from terrestrial exoplanets around an M dwarf, quantifying timescales and showing the influence of stellar wind and magnetic field interactions on atmospheric retention and potential habitability.
- [2023ApJ...953...70G] Performs 3D MHD simulations to quantify how stellar and planetary magnetic field strengths affect atmospheric mass loss, providing analytic relations and mechanisms relevant to M dwarf habitable zone planets.
- [2022AGUFM.P45B..05D] Discusses atmospheric escape processes and the impact of stellar winds and magnetic activity on exoplanetary atmospheric losses, drawing on solar system analogs and extending to M dwarf systems.
- [2021BAAS...53c1015H] Presents 3D MHD simulations of stellar wind interactions with escaping atmospheres of magnetized planets in M dwarf habitable zones, showing timescales and variability of atmospheric loss.

### rank 6 — q_006: partially_addressed (premise: supported)

**How can we robustly distinguish between rocky exoplanets with and without atmospheres using secondary eclipse photometry, and what are the observational limits for this method with current and upcoming facilities?**

- rationale: Post-cutoff literature has made substantial progress in quantifying the challenges and observational limits of distinguishing rocky exoplanets with and without atmospheres using secondary eclipse photometry, including new analysis frameworks, real JWST data, and improved noise modeling. However, the core question remains open, as these works consistently find that current methods are often degenerate and do not yet provide robust, unambiguous atmospheric detections, though they do support the premise that secondary eclipse photometry is a viable—if currently limited—approach.
- [2025ApJ...978L..40H] This work directly simulates and compares secondary eclipse and phase curve photometry for rocky exoplanets, finding that secondary eclipse alone is often degenerate between bare rock and atmospheric models, and discusses observational limits with JWST.
- [2026AJ....171..319M] This paper introduces a framework to account for stellar and orbital uncertainties in interpreting rocky exoplanet secondary eclipse data, quantifying how these uncertainties limit robust atmospheric detection.
- [2025A&A...701A..25F] This study presents new secondary eclipse observations of a rocky exoplanet, develops improved noise modeling, and demonstrates the challenge of distinguishing bare rock from atmospheric cases with current photometric precision.
- [2026arXiv260514997W] This work develops a Bayesian inference method for secondary eclipse spectra, applies it to real JWST data, and quantifies upper limits on atmospheric pressures, showing the method's current sensitivity.
- [2026SSRv..222...40L] This review summarizes the state and future prospects of distinguishing atmospheres on rocky exoplanets using secondary eclipse and other methods, outlining current and upcoming observational capabilities.

### rank 7 — q_007: partially_addressed (premise: supported)

**What are the key uncertainties in radiative transfer modeling of exoplanet atmospheres, especially regarding the treatment of gas mixtures, pressure broadening, and line-mixing, and how do these affect the retrieval of atmospheric properties?**

- rationale: Post-cutoff literature has made substantial progress in identifying and quantifying the impact of uncertainties in radiative transfer modeling, particularly regarding pressure broadening and line list choices, and has begun to address these gaps through new data and modeling efforts. However, the core challenge remains open, as the literature calls for further laboratory measurements and inter-model comparisons to fully resolve these uncertainties and their effects on atmospheric retrievals.
- [2022BAAS...54e.270G] This abstract directly identifies a critical lack of pressure-broadening data for high-metallicity exoplanet atmospheres and describes efforts to compute relevant broadening coefficients, highlighting the impact of these uncertainties on radiative transfer and spectral modeling.
- [2022SPIE12180E..3LA] This work quantifies the impact of differences in line list provenance, broadening coefficients, and line wing cut-offs on atmospheric retrievals, showing that these factors can bias the estimation of atmospheric properties and calling for more laboratory and modeling efforts.

### rank 8 — q_008: partially_addressed (premise: supported)

**How do the properties of exoplanetary atmospheres (e.g., metallicity, internal heat flux, cloud/haze content) influence the radiative-convective boundary and the observable emission spectra of mini-Neptunes and warm Neptunes?**

- rationale: Multiple post-cutoff studies directly model or observationally constrain how metallicity, internal heat flux, and clouds/hazes influence the radiative-convective boundary and emission spectra of mini-Neptunes and warm Neptunes, providing substantial progress. However, while these works advance understanding and provide new constraints, the core question remains open as no single study fully resolves the complex interplay of all these properties across the population.
- [2021AAS...23711107P] Directly models how metallicity, internal heat flux, and clouds/hazes affect the radiative-convective boundary and emission spectra of mini-Neptunes.
- [2024Natur.630..836W] Observationally constrains metallicity, internal temperature, and vertical mixing in a warm Neptune, linking these to atmospheric structure and emission features.
- [2025AAS...24531401M] Explores how metallicity, internal heat flux, and vertical mixing affect atmospheric chemistry and observable spectra in sub-Neptunes and gas giants.
- [2024ApJ...961L..23B] Analyzes trends in cloud/haze properties and metallicity in Neptune-size exoplanets, relating these to observable transmission spectra.
- [2022ExA....53..279M] Models how temperature and composition (including metallicity and chemistry) affect emission spectra and atmospheric structure in exo-Neptunes.

### rank 9 — q_009: partially_addressed (premise: supported)

**What is the role of atmospheric metallicity and anomalous heating in the inflation of hot Jupiters, and how can population-level Bayesian models constrain the mechanisms responsible for radius inflation?**

- rationale: Post-cutoff literature has made substantial progress in constraining the mechanisms responsible for hot Jupiter radius inflation, particularly through population-level Bayesian modeling that distinguishes between shallow and deep heating processes and quantifies the role of atmospheric metallicity and Ohmic dissipation. However, while these studies have advanced our understanding and provided strong evidence for the importance of shallow heating and atmospheric properties, the core question of the dominant inflation mechanism remains open, with multiple mechanisms still under consideration.
- [2026ApJ..1001...35S] This study uses hierarchical Bayesian modeling of a population of hot Jupiters to constrain the depth and nature of anomalous heating, finding strong evidence for shallow heating as the primary inflation mechanism.
- [2025A&A...701A...8V] This work quantitatively investigates Ohmic dissipation as a mechanism for radius inflation, modeling atmospheric metallicity and wind-driven currents in a population of hot Jupiters.
- [2022BAAS...54e.416W] This abstract describes the use of Bayesian parameter estimation and self-consistent radiative-convective models to infer metallicities and heat redistribution in a population of hot Jupiters.

### rank 10 — q_010: partially_addressed (premise: supported)

**How do atmospheric escape rates and mechanisms differ between planets with hydrogen-dominated envelopes and those with high mean molecular weight atmospheres, especially in the context of the sub-Jovian desert and radius gap?**

- rationale: Post-cutoff literature has made substantial progress in modeling and comparing atmospheric escape mechanisms and rates between hydrogen-dominated and high mean molecular weight atmospheres, including their roles in shaping the sub-Jovian desert and radius gap. However, while models and some observations support the premise and clarify qualitative differences, the core question of quantitatively distinguishing escape mechanisms and rates across the full parameter space remains open.
- [2025epsc.conf..376T] This abstract presents full-atmosphere models comparing escape from hydrogen-dominated hot Jupiters and water-rich (high mean molecular weight) sub-Neptunes, finding distinct thermal structures and suppressed mass loss in water-dominated atmospheres.
- [2026ASTCS..1160086F] This work extends hydrodynamic escape modeling to both hydrogen-rich and steam-dominated (high mean molecular weight) atmospheres, highlighting differences in cooling and mass loss mechanisms.
- [2022BAAS...54e2805O] This abstract discusses the evolution of atmospheric composition during escape, including the fate of hydrogen and heavier elements, and implications for the radius gap.
- [2022eas..conf.2490O] This abstract reviews how atmospheric escape shapes the sub-Jovian desert and radius gap, and discusses the competing roles of photoevaporation and core-powered escape for different atmospheric compositions.
- [2026ASTCS..1130201M] This review notes that atmospheric composition substantially affects escape rates and that fractionation during loss alters atmospheric composition, with recent models addressing high-mean-molecular-weight atmospheres.

### rank 11 — q_011: partially_addressed (premise: supported)

**What are the observational signatures and detectability limits of biosignature gases (e.g., O2, CH4) in terrestrial exoplanet atmospheres, considering the effects of refraction, clouds, and haze on transmission spectra?**

- rationale: Post-cutoff literature has made substantial progress in modeling and simulating the detectability of biosignature gases (O2, CH4, CO2, N2O) in terrestrial exoplanet atmospheres, including the effects of clouds, haze, and observational parameters such as spectral resolution. However, while these studies advance our understanding of detection limits and strategies, the core question regarding the comprehensive observational signatures and detectability limits—especially considering all atmospheric effects like refraction, clouds, and haze in transmission spectra—remains open and is not fully resolved.
- [2025PSJ.....6...96C] This study simulates the detectability of biosignature gases (O2, CH4, CO2) in terrestrial exoplanet atmospheres, considering observational configurations and atmospheric types, and discusses the impact of clouds and false positives.
- [2026arXiv260426925G] This work assesses the detectability of key biosignature gases (O2, O3, CH4, CO2) in Earth-like atmospheres through time, focusing on the effects of spectral resolution and noise, and discusses indirect detection strategies.
- [2024AJ....168..292T] This paper models the detectability of CH4, CO2, CO, and N2O in Archean and Proterozoic Earth analogs, quantifying detection limits for these gases in reflected light spectra.
- [2024EGUGA..2617748T] This abstract discusses the detectability of biosignature spectral features in modeled Earth-like atmospheres using transmission and emission spectra, with attention to future missions.
- [2025PSJ.....6...96C] This study specifically simulates the impact of clouds and atmospheric composition on biosignature detectability for nontransiting terrestrial exoplanets.

### rank 12 — q_012: partially_addressed (premise: supported)

**How do the properties of exoplanet host stars, particularly their XUV emission histories, affect the atmospheric evolution and current state of close-in exoplanets, and can we reconstruct these histories to test photoevaporation models?**

- rationale: Multiple post-cutoff works directly address how host star XUV emission histories affect exoplanet atmospheric evolution, using both observational and modeling approaches. However, while substantial progress has been made in characterizing these effects and reconstructing stellar histories, the question remains open as to whether these reconstructions are sufficient to fully test and constrain photoevaporation models across the exoplanet population.
- [2024AAS...24321904F] This abstract summarizes observational and theoretical work on the effect of XUV emission from host stars on exoplanet atmospheres and discusses the need to reconstruct stellar XUV histories for atmospheric modeling.
- [2024eas..conf.1699M] This work presents time-dependent modeling of exoplanet atmospheric evolution under varying stellar XUV irradiation, directly addressing the impact of host star emission histories on photoevaporation.
- [2022csss.confE.160M] This study presents observational and modeling results for the XUV irradiation of young exoplanetary atmospheres, including the effects of stellar activity on atmospheric evolution.
- [2022AN....34310077K] This abstract explores how the diversity of stellar rotation and XUV emission histories affects atmospheric escape and the resulting diversity in exoplanet densities.
- [2021xmm..prop..112Z] This proposal aims to measure X-ray spectra of young, active exoplanet host stars to reduce uncertainties in modeling atmospheric escape, directly engaging with reconstructing XUV histories.

### rank 13 — q_013: partially_addressed (premise: supported)

**What are the dominant sources of correlated noise in multi-wavelength exoplanet transit observations, and how can unsupervised machine learning methods improve the precision and reliability of atmospheric retrievals?**

- rationale: Post-cutoff literature has made substantial progress in characterizing the sources and properties of correlated noise in exoplanet transit observations (2024jwst.prop.6388T) and has demonstrated the utility of unsupervised machine learning for exploring and reducing the dimensionality of correlated spectral data (2022PSJ.....3..205M). However, while these works advance understanding and methodology, they do not fully resolve the identification of dominant noise sources across all instruments nor provide a comprehensive demonstration that unsupervised machine learning methods have definitively improved the precision and reliability of atmospheric retrievals in practice, leaving the core question partially addressed.
- [2024jwst.prop.6388T] This work directly investigates the sources and properties of correlated noise in multi-wavelength exoplanet transit observations, applying both parametric and non-parametric models to real JWST data.
- [2022PSJ.....3..205M] This paper explores unsupervised machine learning techniques for analyzing exoplanet transmission spectra, focusing on dimensionality reduction and correlation structure in the data.

### rank 14 — q_014: partially_addressed (premise: supported)

**How do the microphysical properties (size, composition, spatial distribution) of aerosols and clouds in exoplanet atmospheres affect their phase curves and albedo, and can these properties be constrained with current observations?**

- rationale: Post-cutoff literature has made substantial progress in linking aerosol and cloud microphysical properties to exoplanet phase curves and albedo, with both modeling and observational studies demonstrating sensitivity to particle size, composition, and spatial distribution. However, while these works show that current observations can probe these properties to some extent, they also highlight significant remaining uncertainties and limitations in fully constraining them, leaving the core question open but advanced.
- [2021JGRE..12606655G] This review summarizes how aerosol microphysical properties (size, composition, spatial distribution) affect exoplanet phase curves and albedo, and discusses the extent to which current observations can constrain these properties.
- [2021DPS....5330503H] This study presents laboratory phase curve measurements for specific aerosol species and particle sizes relevant to exoplanet atmospheres, directly linking microphysical properties to observable phase curve signatures.
- [2024ESS.....562431D] This work uses phase curve observations to infer cloud condensation and evaporation events, suggesting that microphysical cloud processes can be probed with current data.

### rank 15 — q_015: partially_addressed (premise: supported)

**What are the limitations of current high-resolution spectrographs in detecting key atmospheric species (e.g., O2, He, Fe I) in exoplanet atmospheres, and how can instrumental advances improve sensitivity to biomarkers and escape tracers?**

- rationale: Multiple recent works explicitly discuss the limitations of current high-resolution spectrographs for detecting key atmospheric species in exoplanet atmospheres, such as telluric contamination, instrument size, and the need for advanced data processing. Several studies also propose and simulate instrumental advances, including space-based spectrographs and optimal resolution strategies, but the core challenge of reliably detecting biomarkers and escape tracers in terrestrial exoplanets remains only partially resolved.
- [2024NatSR..1427356R] This review discusses recent developments in high-resolution spectrographs for exoplanet atmospheres, including their current limitations and the potential for future instrumental advances to improve sensitivity to key species such as O2 and biomarkers.
- [2024asi..confP.245M] This feasibility study directly addresses the limitations of ground-based high-resolution spectrographs, particularly telluric contamination, and explores the potential benefits and challenges of deploying such instruments in space.
- [2026ASTCS..1120004R] This work simulates the detection of biosignature molecules (e.g., O2, H2O) with high-resolution spectroscopy, discusses optimal instrument parameters, and highlights progress in measuring refractory and volatile species in exoplanet atmospheres.
- [2025epsc.conf..644M] This abstract discusses the challenges and capabilities of current high-resolution transit spectroscopy for exoplanet atmospheres, including the need for advanced data reduction to overcome limitations such as telluric contamination.

### rank 16 — q_016: answered (premise: supported)

**How do planetary magnetic fields influence atmospheric escape rates in close-in exoplanets, and under what conditions can magnetic fields significantly reduce or enhance mass loss?**

- rationale: Multiple post-cutoff studies directly address how planetary magnetic fields influence atmospheric escape rates in close-in exoplanets, using advanced simulations and analytic models to show that magnetic fields can both enhance and reduce mass loss depending on their strength and configuration. The literature establishes that the effect is not universally protective and is highly dependent on the interplay between stellar and planetary magnetic fields, thus substantially resolving the question and supporting its premise.
- [2023ApJ...953...70G] This study uses 3D MHD simulations to directly quantify how varying stellar and planetary magnetic field strengths affect atmospheric mass loss, providing analytic relations and showing that magnetic fields can both enhance and reduce escape depending on their configuration.
- [2025MNRAS.536.1089H] This work models the interaction of stellar CMEs with magnetized exoplanets, demonstrating that the structure and orientation of magnetic fields can significantly increase planetary mass-loss rates under certain conditions.
- [2021MNRAS.508.6001C] This paper shows, via 3D MHD simulations, that planetary magnetic fields alter the geometry and channels of atmospheric escape, with some field strengths slightly increasing escape rates, but not substantially changing the overall timescale of atmospheric loss.
- [2021SSRv..217...36R] This review finds that intrinsic magnetic fields do not always protect atmospheres and may sometimes increase ion escape, challenging the simple shielding paradigm and supporting a nuanced view.

### rank 17 — q_017: not_addressed (premise: still_plausible)

**What are the observable consequences of magma ocean dynamos and interior magnetic fields on the atmospheric properties and potential habitability of rocky exoplanets with thick atmospheres?**

- rationale: None of the post-cutoff abstracts substantively engage with the observable consequences of magma ocean dynamos or interior magnetic fields on atmospheric properties or habitability. The literature continues to explore magma ocean-atmosphere interactions and their effects on habitability, but the specific role of magnetic fields or dynamos remains unaddressed and the premise is still plausible.

### rank 18 — q_018: partially_addressed (premise: supported)

**How do the formation and migration histories of exoplanets imprint on their atmospheric compositions, and can comparative planetology across a large sample reveal distinct formation pathways?**

- rationale: Multiple recent studies and surveys have directly engaged the question by developing models, proposing and conducting comparative observations, and outlining methodologies to link exoplanet atmospheric compositions to their formation and migration histories. However, while these efforts have made substantial progress and are beginning to reveal trends, the field acknowledges significant theoretical and observational challenges remain, and a definitive mapping from atmospheric composition to formation pathway is not yet fully established.
- [2024MNRAS.535..171P] This paper describes a survey and modeling effort specifically designed to test whether formation and migration histories of giant planets imprint on their atmospheric compositions, predicting observable differences in C/O ratios between aligned and misaligned hot Jupiters.
- [2024ESS.....562411K] This abstract details a JWST survey comparing atmospheric compositions of hot Jupiters with different migration histories to directly test if atmospheric composition traces formation and migration.
- [2023jwst.prop.3838K] This proposal outlines a comparative study of aligned and misaligned hot Jupiters to determine if atmospheric composition can be used to infer formation pathways, directly engaging the question.
- [2022ApJ...934...74M] This study develops methodologies to interpret atmospheric compositions in terms of formation and migration histories, highlighting both the potential and the challenges of making such inferences.
- [2021EPSC...15..801M] This work discusses the promise and challenges of using atmospheric retrievals to infer exoplanet formation histories, acknowledging both progress and remaining obstacles.

### rank 19 — q_019: partially_addressed (premise: supported)

**What are the best strategies for validating and benchmarking exoplanet atmospheric radiative transfer codes to ensure reliable interpretation of observed spectra?**

- rationale: Post-cutoff literature has made substantial progress in identifying key challenges (such as opacity model limitations) and proposing validation strategies, including benchmarking retrieval codes against solar system analogs with known atmospheric properties. However, while these works advance the discussion and propose concrete steps, a universally accepted set of best practices or a fully standardized benchmarking framework has not yet been established, leaving the core question open but significantly advanced.
- [2023PSJ.....4...10R] This work explicitly discusses validation of exoplanet atmospheric retrieval codes using solar system analogs with known ground-truth, providing a concrete strategy for benchmarking code performance.
- [2022NatAs...6.1287N] This paper identifies a major limitation in current radiative transfer and retrieval codes due to opacity model uncertainties, and proposes a two-tier approach for improvement, directly engaging with benchmarking and validation challenges.
- [2024EPSC...17..857R] This overview discusses the landscape of radiative transfer and inversion codes, as well as the importance of atomic and molecular databases, which are central to code validation and benchmarking.

### rank 20 — q_020: partially_addressed (premise: supported)

**How do the properties of exoplanetary atmospheres (e.g., temperature, composition, cloud/haze content) affect the polarization signatures in spectropolarimetric observations, and can these be used to break degeneracies in atmospheric retrievals?**

- rationale: Multiple post-cutoff studies have advanced the modeling and interpretation of exoplanetary polarization signatures, showing that atmospheric properties such as temperature, composition, and cloud/haze content significantly affect observed polarization. These works demonstrate that spectropolarimetry can help break degeneracies in atmospheric retrievals, but the literature primarily presents theoretical and simulation-based progress, with the core question of practical retrieval and full degeneracy-breaking in real observations remaining open.
- [2026MNRAS.545f2190W] This study directly investigates how temperature structure, cloud grain size, and cloud optical thickness affect thermal emission polarization spectra, showing that polarization can trace atmospheric properties and potentially break degeneracies.
- [2022A&A...663A..55L] This work models the impact of various cloud condensates on polarization signatures, demonstrating that cloud composition and refractive index properties produce distinct polarimetric features.
- [2024AAS...24323004G] This abstract discusses how polarization is sensitive to cloud properties and can break degeneracies present in flux-only observations, with models exploring the effects of temperature, gravity, and cloud parameters.
- [2022ExA....54.1187R] This review highlights that spectropolarimetry uniquely reveals atmospheric properties such as aerosol composition and cloud patterns, providing detail not accessible via flux-only methods.

### rank 21 — q_021: partially_addressed (premise: supported)

**How can laboratory experiments simulating exoplanet atmospheric photochemistry and haze formation inform models of habitability and the detectability of biosignatures?**

- rationale: Multiple post-cutoff works report laboratory experiments simulating exoplanet atmospheric photochemistry and haze formation, and explicitly connect these results to models of atmospheric spectra, habitability, and biosignature detectability. However, while substantial progress is made in linking laboratory haze studies to atmospheric modeling and interpretation, the core challenge of fully quantifying and predicting biosignature detectability in diverse exoplanet atmospheres remains open.
- [2022BAAS...54e5302Y] This work uses laboratory experiments to constrain haze formation and removal in exoplanet atmospheres, directly informing models of atmospheric opacity and thus detectability of atmospheric features.
- [2026ASTCS..1160059P] This study performs laboratory hydrolysis experiments on haze analogs and demonstrates how changes in haze properties affect atmospheric spectra and interpretations of habitability.
- [2024absc.conf98555P] Laboratory-produced haze analogs are studied for their prebiotic chemistry and optical properties, with implications for biosignature detectability and habitability.
- [2022hw...prop...42B] This proposal highlights the importance of laboratory studies for understanding organic haze formation and its impact on habitability and biosignature interpretation in models.
- [2026Ap&SS.371...33T] This review discusses how laboratory experiments provide critical data for exoplanet atmospheric models, including haze formation and spectroscopic properties relevant to biosignature detection.

### rank 22 — q_022: partially_addressed (premise: supported)

**What are the key factors controlling the transition from primary (nebular) to secondary (outgassed/degassed) atmospheres on super-Earths and sub-Neptunes, and how do these transitions affect observable atmospheric properties?**

- rationale: Post-cutoff literature has made substantial progress in identifying and modeling the key factors controlling the transition from primary to secondary atmospheres on super-Earths and sub-Neptunes, including atmospheric escape, mantle redox state, outgassing, and interior-atmosphere exchange. However, while these studies provide detailed theoretical frameworks and predictions for observable properties, the core question remains open as direct observational confirmation and a comprehensive resolution are still forthcoming.
- [2021BAAS...53c1036K] This abstract discusses the processes and conditions controlling the transition from primary to secondary atmospheres on super-Earths and sub-Neptunes, highlighting atmosphere-interior exchange and atmospheric loss as key factors.
- [2024ApJ...963..157T] This work develops a theoretical framework for the chemistry of secondary and hybrid atmospheres, identifying mantle oxidation state, surface pressure, and primordial gas content as key factors, and discusses observable diagnostics.
- [2026ApJ...997..110K] This study models the transition from primary to secondary atmospheres, showing how atmospheric escape and interior degassing affect atmospheric composition, particularly helium and water abundances.
- [2024EGUGA..26.7320T] This abstract presents a thermodynamic model for outgassing chemistry, simulating both secondary and hybrid atmospheres and identifying mantle redox state, melt temperature, and atmospheric loss as controlling factors.
- [2024ESS.....550002K] This work uses a self-consistent evolutionary model to study the transition from primary to secondary atmospheres, incorporating key physical and geochemical processes and their implications for habitability.

### rank 23 — q_023: partially_addressed (premise: supported)

**How do wind speeds and atmospheric dynamics, including the effects of rotation and convection, influence the chemical disequilibrium and observable spectra of exoplanet and brown dwarf atmospheres?**

- rationale: Multiple post-cutoff studies directly investigate how wind speeds, rotation, and convection drive chemical disequilibrium and alter the observable spectra of exoplanet and brown dwarf atmospheres, using both modeling and observational approaches. While these works make substantial progress in quantifying and characterizing these effects, the core question remains open as the full complexity of atmospheric dynamics and their spectral signatures is not yet fully resolved.
- [2021MNRAS.505.5603B] This study systematically explores how vertical and horizontal mixing, influenced by rotation and wind speeds, drive chemical disequilibrium and affect the observable spectra of synchronously rotating exoplanets.
- [2021EPSC...15...46B] This work models the interplay of dynamical mixing (including wind-driven processes) and photochemistry in exoplanet atmospheres, and discusses their impact on chemical disequilibrium and transmission spectra.
- [2022BAAS...54e.129B] This abstract discusses how vertical mixing and day-night circulation (wind-driven processes) connect atmospheric layers and drive disequilibrium chemistry, affecting observable molecular abundances in exoplanet spectra.
- [2023jwst.prop.4084M] This proposal aims to use disequilibrium chemistry as a tracer of mixing (including convection) in brown dwarf atmospheres, linking mixing processes to observable spectral features.
- [2025epsc.conf.1042P] This study investigates how including disequilibrium chemistry (from vertical mixing and photochemistry) in retrievals changes the interpretation of exoplanet spectra, directly addressing the influence of atmospheric dynamics on observable spectra.

### rank 24 — q_024: partially_addressed (premise: supported)

**What are the observational signatures of atmospheric escape from water-rich super-Earths, and can we detect the products of ocean evaporation (e.g., hydrogen exospheres) in such planets?**

- rationale: Post-cutoff literature has made substantial progress in both modeling and proposing direct observations of atmospheric escape from water-rich super-Earths, including the search for hydrogen exospheres as signatures of ocean evaporation. However, while observational campaigns are planned and models predict the relevant signatures, there is no clear evidence in these abstracts that such exospheres have been definitively detected, leaving the core question open but actively pursued.
- [2021hst..prop16726E] This HST proposal aims to directly search for hydrogen exospheres around volatile-rich super-Earths, specifically targeting observational signatures of atmospheric escape and ocean evaporation products.
- [2022hst..prop16998E] This follow-up HST proposal reiterates the plan to use ultraviolet observations to detect hydrogen exospheres in super-Earths, directly engaging the question of observable escape products.
- [2026ASTCS..1100135T] This study models the atmospheric escape of water from steam atmospheres on sub-Neptunes, predicting the conditions under which extended exospheres might form and their detectability.
- [2022BAAS...54e2805O] This abstract discusses the evolution of escaping atmospheres, including hydrogen and heavier elements, and the implications for observational spectroscopy of super-Earths.

### rank 25 — q_025: partially_addressed (premise: supported)

**How do the properties of exoplanetary atmospheres (e.g., metallicity, clouds, haze) affect the detectability and interpretation of phase curves and secondary eclipses in the optical and infrared?**

- rationale: Post-cutoff literature has made substantial progress in understanding how atmospheric properties such as clouds, hazes, and composition affect the detectability and interpretation of phase curves and secondary eclipses, particularly through multi-wavelength and simulation studies. However, while these works clarify the complexity and introduce new techniques, they do not fully resolve all degeneracies or provide a comprehensive framework for all exoplanet types, leaving the core question open but significantly advanced.
- [2025ApJ...982..159S] This study finds that thermal phase curve properties in hot gas giant exoplanets depend on multiple physical parameters, including evidence that cloud layers probed at different wavelengths affect phase curve interpretation.
- [2025ApJ...978L..40H] This work simulates phase curve and secondary eclipse observations for rocky exoplanets, showing that atmospheric properties (e.g., thickness) introduce degeneracies in detectability and interpretation, especially in the infrared.
- [2023AGUFM.P21B3004E] This presentation discusses how clouds and hazes significantly impact the detection of spectral features in exoplanet atmospheres, affecting the interpretation of atmospheric signals.
- [2022AAS...24040205E] This study analyzes the prevalence of clouds and hazes in exoplanet atmospheres and their implications for the detectability of spectral features, relevant to phase curve and eclipse observations.

### rank 26 — q_026: partially_addressed (premise: supported)

**How do non-equilibrium chemical processes, such as vertical mixing and photochemistry, affect the observable atmospheric spectra of exoplanets across a wide range of temperatures and metallicities, particularly in the μbar regime where molecular diffusion dominates?**

- rationale: Post-cutoff literature has made substantial progress in modeling and retrieving the effects of non-equilibrium processes—vertical mixing and photochemistry—on exoplanet spectra across a range of temperatures and metallicities, with several studies directly addressing the spectral consequences and parameter dependencies. However, while these works advance understanding and provide new tools, the core question—especially regarding the μbar regime where molecular diffusion dominates—remains open, as most studies focus on broader pressure ranges or highlight ongoing uncertainties in high-altitude chemistry and spectral signatures.
- [2024ApJ...977...52S] Directly investigates the impact of vertical mixing and metallicity on exoplanet spectra across a wide parameter space, identifying regions where vertical mixing strongly affects observable spectra.
- [2026AAS...24722904B] Presents a retrieval technique that incorporates both photochemistry and vertical mixing, demonstrating their importance for interpreting exoplanet spectra and constraining atmospheric properties.
- [2022MNRAS.512.4877B] Explores photochemistry's influence on atmospheric composition and spectra across a range of temperatures, noting that photochemistry can affect composition even at depth, though spectral effects are marginal in some regimes.
- [2022BAAS...54e.129B] Discusses the interplay of vertical mixing and photochemistry in connecting upper and lower atmospheres and their impact on transmission spectra for a wide range of exoplanets.

### rank 27 — q_027: partially_addressed (premise: supported)

**What are the dominant sources of aerosols in exoplanet atmospheres, and how do silicates and photochemical hazes vary in prevalence and composition as a function of planetary equilibrium temperature and atmospheric properties?**

- rationale: Post-cutoff literature has made substantial progress in identifying the dominant aerosol sources in exoplanet atmospheres, confirming that silicates dominate at high temperatures and photochemical hazes at lower temperatures, with additional complexity from other condensates and compositional diversity. However, the literature also emphasizes that the full variation in prevalence and composition as a function of planetary properties remains incompletely resolved, with ongoing laboratory and observational work needed to fully answer the question.
- [2021JGRE..12606655G] This review synthesizes observational, modeling, and laboratory evidence, finding that silicate aerosols dominate at high temperatures, while photochemical hazes and other condensates are more prevalent at lower temperatures, directly addressing the variation of aerosol sources with planetary properties.
- [2022BAAS...54e5302Y] This study analyzes trends in haze production and removal in temperate exoplanets, finding a transition in haze behavior around 400-500 K and highlighting the complexity of haze prevalence as a function of temperature.
- [2024APS..MARQ39006M] This abstract discusses recent laboratory and observational advances, including unexpected carbon and sulfur sources for haze formation in warmer exoplanet atmospheres, and emphasizes the need for further work to fully understand aerosol sources.
- [2024EPSC...17...13V] This laboratory study investigates the molecular composition of organic hazes under a range of temperatures and atmospheric compositions relevant to sub-Neptunes, providing insight into the diversity of haze chemistry.

### rank 28 — q_028: answered (premise: supported)

**To what extent do clouds and aerosols introduce degeneracies in the retrieval of temperature-pressure profiles and molecular abundances from transit spectroscopy, especially when day-night temperature gradients are present?**

- rationale: Multiple post-cutoff studies using both observations (JWST) and advanced modeling have directly demonstrated that clouds and aerosols, especially when combined with day-night temperature gradients, introduce significant degeneracies and biases in the retrieval of temperature-pressure profiles and molecular abundances from transit spectroscopy. These works not only confirm the premise but also provide empirical and theoretical quantification of the effect, resolving the core question by showing the extent and mechanisms of these degeneracies.
- [2025ApJ...989L..17F] This study uses JWST spectra to show that inhomogeneous aerosol coverage between morning and evening limbs of hot Jupiters leads to significant limb-to-limb differences in transit spectra, directly demonstrating that clouds and aerosols introduce degeneracies in retrievals when day-night gradients are present.
- [2026ASTCS..1140101M] This work provides definitive evidence of limb-to-limb cloud asymmetry in a hot Jupiter, showing that cloud cycling driven by day-night temperature differences causes strong degeneracies in retrievals of atmospheric properties from transit spectra.
- [2022A&A...658A..42P] This paper quantifies biases in retrieved molecular abundances and temperature profiles from 1D retrievals when 3D day-night temperature gradients and visible absorbers are present, confirming that clouds and aerosols exacerbate degeneracies.
- [2021EPSC...15....5P] This abstract demonstrates that transmission spectra are affected by sharp thermal and compositional gradients at the terminator, leading to significant biases in retrievals if multidimensional effects (including clouds and aerosols) are not accounted for.

### rank 29 — q_029: partially_addressed (premise: supported)

**How does stellar activity, including spots and faculae, bias the inference of exoplanet atmospheric properties from transmission spectroscopy, and what are the most robust methods to mitigate these effects?**

- rationale: Post-cutoff literature robustly confirms that stellar activity (spots, faculae, chromospheric emission) can significantly bias exoplanet atmospheric inferences from transmission spectroscopy, and several studies present or propose advanced modeling and retrieval techniques to mitigate these effects. However, while substantial progress has been made in quantifying biases and developing mitigation tools, the problem is not fully resolved, especially for highly active stars and complex stellar heterogeneities, so the core question remains open.
- [2024ApJ...960..107T] This work quantitatively demonstrates how stellar spots and faculae bias exoplanet transmission spectra and tests retrieval frameworks that include stellar activity parameters to mitigate these biases.
- [2024eas..conf.2078C] Presents a new tool (SAGE) for modeling and removing time-dependent stellar activity effects, including spots and limb-darkening, from transmission spectra.
- [2026A&A...709A.153L] Simulates the impact of unocculted stellar spots on high-resolution transmission spectra, quantifying how spot properties affect line distortions and thus bias atmospheric inferences.
- [2025ApJ...980L..42P] Shows that chromospheric and coronal emission from stellar activity can significantly bias transmission spectra and that accounting for these layers improves atmospheric retrievals.
- [2023jwst.prop.3593S] Proposes the use of MHD simulations to generate realistic spot and faculae spectra for correcting stellar contamination in exoplanet transmission spectra.

### rank 30 — q_030: partially_addressed (premise: supported)

**What are the physical mechanisms responsible for the observed odd harmonics in exoplanet photometry, and can these be unambiguously attributed to atmospheric weather patterns rather than data processing artifacts?**

- rationale: Recent literature has made substantial progress in linking observed odd harmonics in exoplanet photometry to physical atmospheric mechanisms, particularly cloud-driven dynamics and planetary-scale waves, using advanced harmonic analysis and vertical mapping. However, while these studies strongly support a physical origin for the harmonics and provide detailed atmospheric interpretations, they do not fully and unambiguously rule out all possible data processing artifacts, leaving the core question partially open.
- [2026AJ....171..195P] This work uses harmonic analysis of exoplanet analog photometry to identify odd harmonics and attributes them to atmospheric weather patterns, specifically cloud-driven dynamics and planetary-scale waves.
- [2026ASTCS..1140103P] This abstract reports the detection of odd harmonics in a planetary-mass object and links them to atmospheric processes such as cloud modulation and hemispheric asymmetry, supporting a physical (not instrumental) origin.
- [2025AAS...24531906P] This study applies harmonic and cluster analysis to exoplanet analogs, isolating variability sources and associating them with atmospheric mechanisms, including planetary-scale waves.
- [2025arXiv250109494S] This paper discusses the robustness of exoplanet atmospheric detections and highlights the potential for data processing artifacts, but does not directly address odd harmonics or their attribution.

### rank 31 — q_031: answered (premise: supported)

**How do the properties of clouds and atmospheric variability differ between young, low-gravity brown dwarfs and older, higher-gravity field brown dwarfs, and what does this imply for directly imaged exoplanets?**

- rationale: Multiple post-cutoff studies directly compare cloud properties and atmospheric variability between young, low-gravity and older, high-gravity brown dwarfs, finding that youth and low gravity are correlated with enhanced clouds and variability. These results support the premise and provide quantitative and population-level evidence, resolving the core question and informing our understanding of directly imaged exoplanets.
- [2023nsbp.confE..68B] This study quantitatively analyzes cloud properties and variability in young, low-gravity versus older, high-gravity brown dwarfs, finding population-level trends and differences relevant to exoplanet analogs.
- [2022BAAS...54e.206V] Presents a large survey comparing variability trends between young and old brown dwarfs, confirming a correlation between enhanced clouds/variability and youth, directly addressing the question.
- [2021AAS...23731401V] Reports on a survey specifically designed to test the correlation between cloud-induced variability and youth in brown dwarfs, enabling direct comparison between young and old populations.
- [2021csss.confE.167V] Discusses how temperature, surface gravity, and age influence variability properties in brown dwarfs, with implications for directly imaged exoplanets.

### rank 32 — q_032: answered (premise: supported)

**What are the key limitations and systematic uncertainties in current atmospheric retrieval techniques, and how can marginalization over systematics models or stochastic processes improve the robustness of exoplanet atmospheric inferences?**

- rationale: Multiple post-cutoff works directly engage with the limitations and systematic uncertainties in atmospheric retrieval, quantifying the impact of model assumptions (especially opacity models) and demonstrating that marginalizing over systematics via ensemble or Bayesian methods leads to more robust and realistic inferences. These studies both identify the sources of systematic error and provide concrete methodological advances—such as model averaging and improved uncertainty quantification—thus substantially resolving the question and supporting its premise.
- [2024ApJ...966..156N] This paper directly addresses the impact of model uncertainty in atmospheric retrievals and demonstrates ensemble methods (including Bayesian model averaging and stacking) that marginalize over systematics, leading to more robust and realistic parameter uncertainties.
- [2024ESS.....562704N] This talk presents a case study showing how combining results from multiple models to account for model uncertainty resolves contradictory inferences about water abundance in HD 209458b, illustrating the benefit of marginalizing over systematics.
- [2022NatAs...6.1287N] This study quantifies the systematic uncertainties due to opacity models, showing they impose a hard limit on retrieval accuracy and proposing new retrieval procedures and improvements in opacity data to address these limitations.
- [2022SPIE12180E..3LA] This contribution quantifies the impact of systematic effects from opacity table choices in retrievals and highlights the need for inter-model comparisons and improved laboratory data to mitigate these uncertainties.
- [2026ASTCS..1120201L] This talk reviews key limitations and systematic uncertainties in current retrieval techniques and discusses future directions, including more robust inference methods and the use of machine learning for diagnostics.

### rank 33 — q_033: partially_addressed (premise: supported)

**How do the abundances of noble gases and isotopic ratios in giant planet atmospheres constrain models of planet formation and migration, and what are the observational requirements to distinguish between competing formation scenarios?**

- rationale: Post-cutoff literature has made substantial progress in modeling and interpreting how noble gas and isotopic abundances in giant planet atmospheres constrain formation and migration models, and has discussed the observational precision required to distinguish between scenarios. However, the literature acknowledges significant remaining challenges and degeneracies, indicating that while the question is being directly addressed, it is not yet fully resolved.
- [2024eas..conf.2268P] This work models how the abundances of noble gases and isotopic ratios in giant planet atmospheres are shaped by formation and migration, and discusses observational biases and requirements for distinguishing formation scenarios.
- [2022ApJ...934...74M] This study develops a methodology to interpret atmospheric compositions in terms of planet formation and migration, highlighting the complexities and uncertainties in making such inferences.
- [2022cosp...44..268K] This abstract discusses how precise measurements of atmospheric abundances, including metallicity and C/O ratios, can be used to retrieve formation parameters and distinguish between formation scenarios.
- [2023ApJ...943..112C] This paper proposes that measuring refractory elements alongside C/O and O/Si ratios can break degeneracies in formation histories, directly addressing the use of atmospheric abundances to constrain formation models.
- [2022xrp..prop..129S] This proposal outlines the need for accurate and precise abundance measurements (including noble gases and isotopic ratios) to distinguish between competing hot Jupiter formation scenarios.

### rank 34 — q_034: partially_addressed (premise: supported)

**What is the impact of high-energy stellar emissions (XUV, UV) on atmospheric escape rates and the long-term retention of atmospheres on close-in exoplanets, especially super-Earths and warm Neptunes?**

- rationale: The post-cutoff literature provides substantial new observational and theoretical evidence directly linking high-energy stellar emissions (XUV, UV) to atmospheric escape rates and the long-term retention of atmospheres on close-in exoplanets, including super-Earths and warm Neptunes. However, while the importance of high-energy irradiation is strongly supported, uncertainties remain regarding the relative roles of different escape mechanisms and the precise conditions for atmospheric survival, so the core question is not fully resolved.
- [2026ASTCS..1150202C] Reviews observational studies directly connecting stellar high-energy (X-ray, UV) emissions to atmospheric escape in close-in exoplanets, highlighting the importance of these emissions in driving mass loss.
- [2021MNRAS.501L..28K] Shows that EUV-driven atmospheric escape persists on Gyr timescales, challenging previous models and emphasizing the long-term impact of stellar high-energy emissions on atmospheric retention.
- [2025RvMPP...9...18H] Reviews recent observations and models, confirming that stellar XUV is a major driver of atmospheric escape, especially for close-in exoplanets, and discusses its role in shaping planetary evolution.
- [2022eas..conf.2490O] Discusses the demographic signatures of atmospheric escape driven by high-energy stellar radiation, such as the hot Neptune desert and radius valley, but notes ongoing debate with core-powered escape models.
- [2024ESS.....562904N] Presents new modeling suggesting that atomic line cooling can mitigate atmospheric escape even under intense XUV, refining our understanding of atmospheric retention under high-energy irradiation.

### rank 35 — q_035: partially_addressed (premise: supported)

**How do the vertical and horizontal structures of equatorial jets on tidally locked terrestrial exoplanets form, and what observable signatures do these jets imprint on atmospheric spectra and phase curves?**

- rationale: Post-cutoff literature has made substantial progress in linking the structure and formation of equatorial jets on tidally locked exoplanets to observable spectral and phase curve signatures, using both theoretical decomposition and high-resolution modeling. However, while these works clarify the contributions of different circulation components and their observational imprints, the full formation mechanisms and their detailed observable consequences remain an active area of research, leaving the core question partially addressed.
- [2023AGUFM.P21B3013L] This abstract directly analyzes the vertical and horizontal structure of equatorial jets on tidally locked planets, decomposing circulation components and linking them to observable phase curve signatures.
- [2022ApJ...941..171L] This work partitions the temperature structure of tidally locked exoplanets into components associated with jets and other circulation features, connecting these to observable atmospheric properties.
- [2026arXiv260623910B] This study models how the strength and presence of equatorial jets affect Doppler shifts in transmission spectra, providing insight into observable signatures of jet structure.

### rank 36 — q_036: partially_addressed (premise: still_plausible)

**What are the dominant mechanisms for angular momentum transport and zonal jet formation in giant planet atmospheres, and how do instabilities such as the Goldreich-Schubert-Fricke instability contribute to observed atmospheric dynamics?**

- rationale: Recent literature has made substantial progress in characterizing the flow regimes, vertical mixing, and jet structures in giant planet and hot Jupiter atmospheres, including the roles of shear instabilities and rotation. However, the dominant mechanisms for angular momentum transport and the specific contribution of instabilities like Goldreich-Schubert-Fricke remain incompletely resolved, with some instabilities found to have only minor effects and observational-model discrepancies persisting.
- [2022MNRAS.517.2714M] Directly investigates turbulent transport and shear instabilities in hot Jupiter atmospheres, finding that vertical mixing from such instabilities is significant only in the hottest exoplanets and has minor momentum feedback on mean flows.
- [2025Natur.639..902S] Presents observational evidence of vertical and zonal jet structure in an ultra-hot Jupiter, highlighting gaps between models and observed atmospheric dynamics.
- [2024A&A...691A.232S] Explores how rotation and flow regimes affect jet formation and vertical transport in hot Jupiter atmospheres, identifying different dynamical regimes but not pinpointing a single dominant mechanism.

### rank 37 — q_037: partially_addressed (premise: supported)

**How do the properties of mineral atmospheres on hot super-Earths evolve under intense photo-evaporation, and what are the observable consequences for atmospheric composition and mass loss rates?**

- rationale: Post-cutoff literature has made substantial progress in modeling the evolution of mineral and metal-rich atmospheres on hot super-Earths under intense photo-evaporation, including predictions for observable atmospheric composition and mass loss rates. However, while these works advance theoretical understanding and discuss observational consequences, the core question of detailed, empirically validated evolution and specific observable signatures of mineral atmospheres remains open.
- [2024ESS.....562703S] This work models the evolution of super-Earth atmospheres under intense irradiation, showing transitions to metal-rich atmospheres and discussing observable consequences for composition and mass loss rates.
- [2023eas..conf.2284O] This abstract discusses the evolution of highly irradiated planets, including the fate of rock vapor-dominated (mineral) atmospheres and the observational implications of escaping heavy element atmospheres.

### rank 38 — q_038: answered (premise: supported)

**What are the minimum spectral resolution and signal-to-noise requirements for robust detection of key biosignature gases (e.g., O2, H2O, O3) in Earth-like exoplanet atmospheres using reflected light spectroscopy?**

- rationale: Multiple post-cutoff studies directly simulate and quantify the minimum spectral resolution and signal-to-noise requirements for detecting O2, O3, and H2O in Earth-like exoplanet atmospheres using reflected light spectroscopy, including for different atmospheric compositions and epochs. These works provide explicit, quantitative answers to the question, confirming and refining the requirements for robust biosignature detection with next-generation observatories.
- [2026arXiv260426925G] Directly quantifies the minimum spectral resolution and S/N needed for robust detection of O2, O3, and H2O in Earth-like atmospheres using reflected light, with detailed results for different epochs and instrument constraints.
- [2023AJ....166..157D] Demonstrates that O3 can be robustly detected in Proterozoic-like atmospheres at R=7 and S/N~10 in the UV, and discusses requirements for O2 and O3 detectability in reflected light.
- [2026absc.conf50204G] Simulates biosignature detection for Earth through time, showing how spectral resolution and S/N affect detectability of O2, O3, and other gases, and quantifies exposure time requirements.
- [2024AJ....167...27L] Presents detectability of O2 and O3 as explicit functions of S/N, wavelength, and abundance, and defines requirements for simultaneous detection in reflected light spectra.

### rank 39 — q_039: partially_addressed (premise: supported)

**How do the atmospheric compositions of hot Jupiters and brown dwarfs differ as a function of irradiation, and can observations of objects like KELT-1b and R147-BD bridge the gap between these populations?**

- rationale: Recent literature has made substantial progress in empirically and theoretically comparing the atmospheric compositions of hot Jupiters and brown dwarfs as a function of irradiation, including direct spectral comparisons and retrievals across both populations. However, while these studies bridge the gap and map trends, they do not fully resolve all differences or definitively establish a unified framework, leaving the core question open but significantly advanced.
- [2026ASTCS..1130001F] This study directly compares JWST spectra of hot Jupiters and brown dwarfs across a range of irradiation, mapping key molecular features and color sequences to bridge the populations.
- [2023AAS...24132402L] This work retrieves atmospheric properties of highly irradiated brown dwarfs and compares their temperature inversions and molecular abundances to those of hot and ultra-hot Jupiters.
- [2021csss.confE..94L] This abstract presents models and spectra of highly irradiated brown dwarfs, explicitly comparing their atmospheric responses to irradiation with those of ultra-hot Jupiters.
- [2023NatAs...7.1329H] This paper reports on an extremely irradiated brown dwarf as a hot Jupiter analogue, discussing its atmospheric properties in the context of irradiation and comparing it to KELT-9b.

### rank 40 — q_040: partially_addressed (premise: still_plausible)

**What are the effects of precipitation of energetic electrons and magnetospheric interactions on the upper atmospheres of hot Jupiters, and how do these processes influence atmospheric heating and escape?**

- rationale: Recent literature has made substantial progress in modeling the effects of magnetic fields and magnetospheric interactions on the upper atmospheres of hot Jupiters, particularly regarding atmospheric circulation and heating via Ohmic dissipation. However, direct modeling or observational study of energetic electron precipitation and its specific impact on atmospheric heating and escape remains largely unaddressed, leaving the core question open.
- [2025AAS...24531406B] This work models the effects of magnetic fields on atmospheric circulation in ultrahot Jupiters, identifying observational signatures of magnetic interactions but does not address energetic electron precipitation or its direct impact on heating and escape.
- [2024ApJ...976...32B] This study uses 3D MHD models to explore how magnetic fields alter atmospheric circulation and spectral signatures in ultrahot Jupiters, advancing understanding of magnetospheric interactions but not specifically energetic electron precipitation or escape rates.
- [2022MNRAS.517.3113D] This paper discusses magnetic induction, Ohmic heating, and atmospheric currents in hot Jupiters, providing insight into magnetospheric interactions and heating, but does not directly address electron precipitation or atmospheric escape.
- [2026ASTCS..1160086F] This work models hydrodynamic escape and atmospheric heating in hot Jupiters, focusing on XUV-driven processes and radiative cooling, but does not include magnetospheric or energetic electron precipitation effects.

### rank 41 — q_041: partially_addressed (premise: supported)

**How can high-resolution spectroscopy and cross-correlation techniques be optimized to detect molecular species and thermal inversions in non-transiting exoplanet atmospheres?**

- rationale: Post-cutoff literature made substantial progress in optimizing high-resolution spectroscopy and cross-correlation techniques for detecting molecular species in non-transiting exoplanet atmospheres, including new Bayesian retrieval frameworks, improved stellar contamination correction, and strategies for differential phase extraction. However, while these works advance methodology and demonstrate feasibility, the core challenge of robustly detecting thermal inversions in non-transiting atmospheres remains open, so the question is only partially addressed and the premise is supported.
- [2021AJ....161..180F] Directly addresses optimization of high-resolution spectroscopy and cross-correlation for detecting molecular species in non-transiting exoplanet atmospheres, proposing differential phase techniques and quantifying detectability limits.
- [2021atat.confE..12G] Presents a Bayesian framework to extract quantitative atmospheric information from high-resolution cross-correlation data, including methods to mitigate filtering losses, demonstrated on a non-transiting planet.
- [2024xrp..prop...98L] Proposes development of multi-dimensional retrieval methods and 3D model grids to interpret high-resolution cross-correlation spectra, aiming to identify diagnostic features for molecules and temperature structure.
- [2021spc..confE..26C] Describes improved correction for stellar contamination in high-resolution spectroscopy, enhancing detectability of planetary signals, with application to emission spectra of non-transiting planets.

### rank 42 — q_042: partially_addressed (premise: supported)

**What are the key challenges in distinguishing between surface and atmospheric contributions to the observed albedo of hot super-Earths, and how can we robustly infer the presence of clouds versus bare lava surfaces?**

- rationale: Post-cutoff literature has made substantial progress in quantifying and modeling the degeneracies between surface and atmospheric (especially cloud) contributions to the observed albedo of hot super-Earths, and in developing retrieval techniques that attempt to separate these effects. However, the core challenge remains unresolved, as robustly inferring clouds versus bare surfaces is still limited by degeneracies and current instrumental precision, though the premise that this is a key challenge is strongly supported.
- [2022BAAS...54e.187I] This abstract discusses the challenge of distinguishing surface and atmospheric contributions in emission spectra, showing that surface albedo can bias atmospheric retrievals and that robust inference is difficult without wavelength-dependent models.
- [2022ApJ...931...48W] This work directly addresses the degeneracy between cloud properties and wavelength-dependent surface albedo in retrievals, finding that disentangling the two is challenging and often leads to biased results.
- [2024AJ....168..287N] This study simulates cloud formation on lava planets and finds that distinguishing between cloudy and cloud-free cases is possible but requires precision at the limit of current instruments.
- [2022MNRAS.511..440T] This paper demonstrates the difficulty of mapping surface albedo in the presence of variable clouds, showing that degeneracies remain a major challenge.

### rank 43 — q_043: partially_addressed (premise: supported)

**How do the properties of exoplanet atmospheres, such as mean molecular weight and bulk composition, vary across the rocky/gaseous divide, and what observational strategies are most effective for constraining these properties?**

- rationale: Recent literature has made substantial progress in measuring and interpreting exoplanet atmospheric properties across the rocky/gaseous divide, including population-level studies and new observational strategies (e.g., JWST, spectral analysis). However, the core question remains open, as the field is still developing robust constraints on mean molecular weight and bulk composition, especially for terrestrial and sub-Neptune planets.
- [2022BAAS...54e.400E] This abstract discusses population studies of exoplanet atmospheres, highlighting efforts to find chemical trends as a function of bulk planetary parameters, directly engaging the question of how atmospheric properties vary across planet types.
- [2025A&A...699A..67H] This work establishes links between atmospheric spectra and surface rock composition for rocky exoplanets, providing new strategies for constraining bulk composition and mean molecular weight.
- [2024APS..MARQ39007K] This abstract reviews recent observational advances in measuring exoplanet atmospheric composition, including results from JWST and ELTs, and discusses implications for understanding atmospheric properties.
- [2025Sci...390S3660L] This review summarizes current understanding of exoplanets with diverse bulk compositions and discusses how atmospheric observations can distinguish between different planetary regimes.

### rank 44 — q_044: partially_addressed (premise: supported)

**How do the spectral features of alkali metals and molecular species in the UV and optical constrain the properties of exoplanet exospheres and atmospheric escape processes?**

- rationale: Post-cutoff literature has made substantial progress in modeling and interpreting the spectral features of alkali metals and molecular species in the UV and optical for constraining exoplanet exospheres and atmospheric escape, including new frameworks and synthetic spectra databases. However, the literature acknowledges that many aspects remain unresolved, such as model degeneracies and the full diagnostic power of these features, so the core question is not fully answered.
- [2023A&A...675A.193L] This work expands the inventory of spectral lines used to trace atmospheric escape, models transmission spectra including alkali metals and molecular species, and discusses how these features constrain outflow properties.
- [2025A&A...698A.112L] This paper presents a database of synthetic transmission spectra for exoplanets, emphasizing the use of multiple spectral lines (including alkali metals) to constrain atmospheric escape and exospheric properties.
- [2022FrASS...901873S] This study discusses the challenges and implications of detecting alkali metal absorption (Na, K) in exoplanet exospheres, including their role in atmospheric escape diagnostics.

### rank 45 — q_045: partially_addressed (premise: supported)

**What is the role of surface gravity in modulating atmospheric variability and cloud properties in young exoplanets and brown dwarfs, and how can variability studies inform models of atmospheric structure?**

- rationale: Multiple post-cutoff works directly investigate the influence of surface gravity on atmospheric variability and cloud properties in young exoplanets and brown dwarfs, with several studies proposing or presenting variability surveys and retrievals that compare low- and high-gravity objects. However, while these works make substantial progress and explicitly pose the question, they indicate that the effect of surface gravity is not yet well understood or definitively resolved, leaving the core question open but advanced.
- [2022fine.prop...94K] This proposal aims to directly compare low and high surface gravity objects to study how surface gravity affects atmospheric variability in ultracool atmospheres, addressing the core question.
- [2021csss.confE.167V] This abstract discusses how surface gravity, among other parameters, can influence observed variability properties in young, low-gravity exoplanet analogs.
- [2021AAS...23731401V] This study presents variability monitoring of young, low-mass brown dwarfs to test the correlation between cloud-induced variability and youth, which is related to surface gravity.

### rank 46 — q_046: partially_addressed (premise: supported)

**How can population-based statistical approaches to the habitable zone, which account for unknown atmospheric and geophysical properties, improve our understanding of exoplanet habitability compared to traditional single-planet models?**

- rationale: Multiple post-cutoff studies have developed and applied population-based statistical approaches to the habitable zone, explicitly addressing how such methods can improve our understanding of exoplanet habitability by incorporating unknown atmospheric and geophysical properties. These works demonstrate substantial progress and methodological innovation, but the core question of how much these approaches improve our understanding compared to traditional models remains open, as empirical validation is still limited by current observational capabilities.
- [2022AJ....163..140L] This work develops a hierarchical Bayesian framework for population-level atmospheric retrievals, directly applying statistical approaches to the habitable zone and demonstrating their ability to infer population trends in exoplanet atmospheres.
- [2023AGUFM.P51D2712U] This abstract describes a statistical framework for testing the habitable zone concept using population-level atmospheric data, explicitly aiming to refine or refute habitability hypotheses.
- [2024PSJ.....5....3S] This study uses a statistical population-based framework (Bioverse) to assess the detectability of habitable zone boundaries via exoplanet demographics, integrating unknown atmospheric and geophysical properties.
- [2021AGUFM.P55D1969A] This work applies a population-level statistical model (astro-eco framework) to predict biosignature patterns and atmospheric properties across exoplanets, accounting for diverse planetary characteristics.

### rank 47 — q_047: partially_addressed (premise: supported)

**How do the limitations of current molecular line lists and spectroscopic databases (e.g., HITRAN, HITEMP) affect the accuracy of atmospheric retrievals for high-temperature exoplanet atmospheres?**

- rationale: Post-cutoff literature directly engages with the question by discussing the limitations of current molecular line lists and spectroscopic databases, and their impact on the accuracy of atmospheric retrievals for high-temperature exoplanet atmospheres. However, while these works highlight and partially address the limitations (e.g., through database expansions and combining resources), they do not claim that the core challenge has been fully resolved, leaving the question partially addressed and the premise supported.
- [2023AAS...24126404H] This abstract explicitly discusses the limitations of current spectroscopic data (HITRAN, HITEMP) when applied to the interpretation of planetary spectra, highlighting ongoing challenges.
- [2024EPSC...17.1084B] This work notes that the lack of adequate procedures for collisional line-shape parameters and pressure-broadening coefficients limits the quality of atmospheric modeling and retrievals for exoplanets.
- [2022FrASS...8..218T] This review addresses the impact of incomplete or inaccurate molecular line lists on the modeling of exoplanet atmospheres, discussing the trade-off between completeness and accuracy.
- [2022EPSC...16..619K] This abstract describes the necessity of combining multiple databases to improve the accuracy of molecular absorption calculations for diverse exoplanetary atmospheres, implicitly acknowledging current limitations.

### rank 48 — q_048: partially_addressed (premise: supported)

**What are the most effective strategies for prioritizing exoplanet targets for atmospheric biosignature searches, given limited observing resources and the need to minimize false positives and negatives?**

- rationale: Several post-cutoff works directly engage with strategies for prioritizing exoplanet targets for atmospheric biosignature searches, including decision tree frameworks, target list optimization, and resource allocation. While these studies make substantial progress and provide concrete recommendations, the core question of the most effective overall strategy remains open due to the evolving nature of observational capabilities and biosignature interpretation frameworks.
- [2023AAS...24141601Y] This work implements a decision tree framework for prioritizing atmospheric biosignature searches, explicitly addressing strategies to maximize efficiency and minimize false positives.
- [2025AJ....170..216B] This paper proposes a new approach to compiling exoplanet target lists for atmospheric characterization, quantifies observing resource needs, and provides recommendations for optimizing target selection.
- [2024AGUFMP43C.3018L] This abstract discusses Bayesian analysis and optimal wavelength selection to maximize biosignature detection efficiency given limited observing time, directly engaging with prioritization strategies.
- [2026ASTCS..1160020K] This work highlights the importance of combining atmospheric and surface biosignatures, and discusses trade-offs and optimization strategies for observation time and target selection.

### rank 49 — q_049: partially_addressed (premise: supported)

**How do the properties of clouds and atmospheric circulation on the nightside of highly irradiated brown dwarfs and hot Jupiters affect their emission spectra and phase curves?**

- rationale: Post-cutoff literature has made substantial progress in modeling and observing the effects of nightside clouds and atmospheric circulation on the emission spectra and phase curves of highly irradiated brown dwarfs and hot Jupiters. Multiple studies directly simulate or retrieve these effects, showing how cloud properties and circulation shape observable features, but the full diversity and detailed mechanisms remain under active investigation.
- [2021ApJ...908..101R] Directly models how nightside clouds and atmospheric circulation affect phase curves and emission spectra of hot Jupiters, showing clouds increase phase-curve amplitude and decrease offset.
- [2021MNRAS.501...78P] Demonstrates that nightside clouds on hot Jupiters increase phase curve amplitude and decrease offset, with effects sensitive to cloud properties, matching observed diversity.
- [2022ApJ...934...79K] Simulates patchy nightside clouds on ultra-hot Jupiters, showing their distribution and radiative feedback are set by atmospheric dynamics and affect emission.
- [2022AJ....163....8L] Presents phase-resolved emission spectra of an irradiated brown dwarf, revealing wavelength-dependent day-night spectral variation and pressure-dependent temperature contrast.
- [2023AAS...24132402L] Retrieves phase-resolved spectra of highly irradiated brown dwarfs, showing longitudinally evolving temperature and abundance profiles, and the disappearance of dayside inversions on the nightside.

### rank 50 — q_050: partially_addressed (premise: supported)

**How can direct imaging and reflection spectroscopy be used to uniquely determine the methane mixing ratio and cloud deck pressure in cold exoplanet atmospheres, and what are the limitations imposed by overlying haze layers?**

- rationale: Post-cutoff literature has made substantial progress in using direct imaging and reflection spectroscopy to retrieve methane mixing ratios and cloud deck pressures in cold exoplanet atmospheres, with several studies explicitly addressing the limitations imposed by clouds and hazes. However, while methodologies and limitations are explored and retrievals are demonstrated, the literature does not yet claim a unique or fully robust solution to the degeneracies introduced by overlying haze layers, leaving the core question open but advanced.
- [2021ApJ...910..158M] This study simulates direct imaging reflection spectra of cool giants and investigates how cloud parameterizations affect retrievals of methane abundance and cloud structure, highlighting limitations due to cloud complexity.
- [2024ESS.....563203H] This work uses high-resolution spectroscopy of Titan as an exoplanet analog to constrain haze and methane cloud vertical distributions, directly addressing the impact of haze on atmospheric retrievals.
- [2025AAS...24531904R] This dissertation discusses the challenges in interpreting spectra of cold exoplanets due to clouds, disequilibrium chemistry, and vertical mixing, and presents retrieval analyses relevant to methane and cloud deck inference.

### rank 51 — q_051: partially_addressed (premise: supported)

**How does the presence of a deep magma ocean in sub-Neptune exoplanets affect the atmospheric composition and volatile content, and can measurements of atmospheric mean molecular weight break the degeneracy between radius and volatile mass?**

- rationale: Post-cutoff literature has made substantial progress in modeling and observing the effects of deep magma oceans on sub-Neptune atmospheric composition and volatile content, confirming that magma-atmosphere interactions significantly alter observable properties such as C/O ratios, H2O abundance, and mean molecular weight. However, while these studies clarify the mechanisms and propose observational strategies, the degeneracy between radius and volatile mass is not yet fully resolved by atmospheric mean molecular weight measurements alone, leaving the core question open but advanced.
- [2024ApJ...975...14S] Directly models how magma oceans affect atmospheric C, O, and H abundances in sub-Neptunes, showing substantial impact on atmospheric composition and volatile content.
- [2024AAS...24313305M] Discusses the importance of magma-atmosphere chemical interactions in sub-Neptunes and their implications for interpreting atmospheric observations.
- [2024jwst.prop.6284C] Proposes JWST observations to detect signatures of magma-atmosphere interaction in a sub-Neptune, aiming to constrain atmospheric composition and volatile sources.
- [2022MNRAS.514.6025M] Shows that silicate vapor from magma oceans alters atmospheric mean molecular weight and affects radius/volatile mass inferences, directly addressing the degeneracy.

### rank 52 — q_052: partially_addressed (premise: supported)

**What are the dominant mechanisms responsible for the inflated radii of hot Jupiters, and can a single mechanism explain the entire observed distribution or is a combination required?**

- rationale: Recent literature has made substantial progress in modeling and evaluating specific mechanisms, especially Ohmic dissipation, and has ruled out others such as vertical advection of heat alone. However, reviews and modeling studies consistently conclude that no single mechanism fully explains the entire observed distribution of inflated radii, and that a combination of processes is likely required, leaving the core question open but advanced.
- [2024arXiv240505307T] This review discusses the range of proposed inflation mechanisms for hot Jupiters, evaluates evidence for and against them, and concludes that more than one mechanism may be operating in concert.
- [2024arXiv240311501A] This study quantitatively models Ohmic dissipation as a mechanism for radius inflation and finds it can broadly reproduce observed radii, but does not claim it is the sole mechanism.
- [2025A&A...701A...8V] This work investigates Ohmic dissipation coupled with internal dynamo evolution and finds it can explain the observed range of radii, but does not exclude other mechanisms.
- [2024EPSC...17..225U] This abstract reviews the evidence for Ohmic heating as a dominant mechanism, noting that irradiation alone is insufficient and that Ohmic heating is a leading explanation.
- [2022A&A...666L..11S] This study finds that vertical advection of heat by atmospheric dynamics alone cannot explain radius inflation, ruling out one proposed mechanism.

### rank 53 — q_053: answered (premise: supported)

**To what extent do morning and evening terminator regions of exoplanet atmospheres exhibit distinct temperature, pressure, and compositional profiles, and how do these differences affect transmission spectra?**

- rationale: Post-cutoff literature has directly measured and resolved differences in temperature, composition, and spectral features between morning and evening terminators of exoplanet atmospheres, notably with JWST and high-resolution ground-based spectroscopy. These results confirm the premise that terminator regions are inhomogeneous and demonstrate how these differences affect transmission spectra, substantially resolving the original research question.
- [2024Natur.632.1017E] This study directly reports the detection of inhomogeneous terminators on WASP-39 b, retrieving distinct morning and evening transmission spectra and showing the evening terminator is hotter with larger spectral features.
- [2023AAS...24132403G] This work spatially resolves the terminator of WASP-76b, finding differences in Fe abundance, temperature, and wind speed between morning and evening limbs, supporting distinct profiles and their spectral impact.

### rank 54 — q_054: partially_addressed (premise: supported)

**How do clouds and hazes at different altitudes and compositions affect the detectability of alkali metals (e.g., Na, K) and molecular features in exoplanet transmission spectra, especially in cases with conflicting observational results?**

- rationale: Post-cutoff literature has made substantial progress in quantifying how clouds and hazes at different altitudes and compositions affect the detectability of alkali metals and molecular features in exoplanet transmission spectra. Several studies demonstrate that clouds and hazes can dampen or even flatten spectral features, but most planets still show detectable modulation, and new work has improved the accuracy of alkali metal detection by accounting for stellar and atmospheric effects; however, the interplay between conflicting observational results and the full range of cloud/haze properties remains incompletely resolved.
- [2022AGUFM.P35C1893E] This study analyzes a large sample of exoplanet transmission spectra, finding that clouds and hazes dampen spectral features and are vertically distributed, but most planets still show detectable spectral modulation.
- [2022ApJ...941L...5E] This work identifies trends in cloud/haze presence and their effect on spectral modulation, showing that while clouds/hazes are common, most planets retain detectable features in transmission spectra.
- [2026ApJ..1002..221P] This paper demonstrates that hydrolyzed hazes in water-rich exoplanet atmospheres can almost completely flatten molecular features in model spectra, directly addressing how haze composition and altitude affect detectability.
- [2026ASTCS..1160059P] This study shows that photochemical hazes, especially after hydrolysis, increase optical opacity and obscure molecular absorption features, impacting the interpretation of transmission spectra.
- [2024A&A...692A..43C] This work improves sodium detection in exoplanet atmospheres by correcting for stellar effects, confirming Na I in several systems and refining our understanding of its detectability.

### rank 55 — q_055: posed_but_open (premise: still_plausible)

**What are the physical processes that produce strong Hα signals in ultra-hot Jupiters, and how do recombination cascades and high ionizing fluxes contribute to the observed n=2 hydrogen population?**

- rationale: The post-cutoff literature continues to observe and discuss strong Hα signals in ultra-hot Jupiters and their correlation with other species, indicating ongoing interest in the processes populating excited hydrogen states. However, none of the abstracts directly resolve or substantially advance the understanding of the specific physical mechanisms—such as the roles of recombination cascades and high ionizing fluxes—in producing the observed n=2 hydrogen population, leaving the core question open.
- [2022eas..conf..287Z] This abstract discusses Hα absorption in ultra-hot Jupiters and its correlation with FeII, suggesting an exospheric origin and linking it to mass loss, but does not directly address the physical processes (such as recombination cascades or ionizing fluxes) responsible for the n=2 hydrogen population.

### rank 56 — q_056: partially_addressed (premise: supported)

**How does the buoyancy barrier in non-isothermal protoplanetary envelopes suppress atmospheric recycling, and what are the implications for the formation of super-Earths versus gas giants?**

- rationale: Post-cutoff literature has made substantial progress in simulating and characterizing the efficiency and limits of atmospheric recycling in non-isothermal protoplanetary envelopes, including the identification of regions where recycling is suppressed (potentially by a buoyancy barrier). However, while these studies support the premise and clarify the mechanisms involved, they do not fully resolve the detailed physical nature of the buoyancy barrier or its universal implications for the super-Earth/gas giant dichotomy, leaving the core question partially open.
- [2022BAAS...54e4505B] This abstract discusses the suppression of atmospheric recycling in the inner regions of protoplanetary envelopes and its implications for super-Earth formation, directly engaging with the buoyancy barrier concept.
- [2022A&A...661A.142M] This work explores the efficiency of atmospheric recycling as a function of core mass and optical depth, addressing how recycling can prevent runaway accretion and thus relates to the formation of super-Earths versus gas giants.
- [2022eas..conf.1226M] This abstract confirms that atmospheric recycling can prevent runaway gas accretion in super-Earths, supporting the premise that recycling efficiency is key to planet type outcomes.

### rank 57 — q_057: partially_addressed (premise: supported)

**What is the role of stellar magnetism and winds in the long-term evolution and evaporation of exoplanetary atmospheres, particularly for planets around cool, main-sequence stars?**

- rationale: Post-cutoff literature has made substantial progress in modeling and characterizing the effects of stellar magnetism and winds on exoplanetary atmospheric evolution, particularly through advanced MHD simulations and observational efforts. However, while these studies support the premise and clarify mechanisms, they do not fully resolve the long-term quantitative impact or provide a comprehensive answer, leaving the core question open but significantly advanced.
- [2021ApJ...913..130H] This study uses 3D MHD simulations to show that stellar wind interactions with exoplanet atmospheres around cool stars can accelerate and advect atmospheric outflows, affecting atmospheric loss and observable signatures.
- [2021BAAS...53c1015H] This work presents 3D MHD simulations demonstrating that stellar wind interactions can cause significant atmospheric erosion in exoplanets around low-mass stars, supporting the premise and advancing understanding of the process.
- [2023eas..conf..400C] This abstract discusses how stellar magnetism and winds, particularly in cool stars, influence wind properties and potentially constrain the habitable zone by affecting exoplanet atmospheres.
- [2024AAS...24321903P] This review highlights recent advances in characterizing stellar magnetospheric environments and their impact on exoplanetary atmospheres, emphasizing the importance of stellar magnetism and winds.

### rank 58 — q_058: answered (premise: supported)

**How do the chemical reactions between magma and atmosphere on sub-Neptunes with varying oxidation states influence observable atmospheric properties, and can these be constrained by current or future observations?**

- rationale: Multiple post-cutoff studies directly model and quantify how chemical reactions between magma and atmosphere, including the effects of varying oxidation states, influence observable atmospheric properties such as C/O ratio, H2O, and CO2 abundances. These works both predict and, in at least one case, fit observed spectra (e.g., JWST data) using models that incorporate magma-atmosphere chemical coupling, thus substantially resolving the question and supporting its premise.
- [2024ApJ...975...14S] This study models how magma-atmosphere chemical equilibrium, including varying redox states, controls the abundances of H, O, and C in sub-Neptune atmospheres, and predicts observable trends in C/O and H2O fractions.
- [2025ApJ...988L..55W] This work quantifies how magma ocean–atmosphere interactions set the atmospheric C/O ratio, showing it is determined by chemical equilibrium with the magma and varies with planetary and atmospheric properties, and couples these models to observable atmospheric spectra.
- [2025ApJ...995...95N] This paper presents a modeling framework that links magma-atmosphere chemical reactions to observable atmospheric signatures, and successfully fits JWST spectra of a sub-Neptune using these models.
- [2025epsc.conf..635C] This study uses ab initio simulations to show that hydrogen-magma reactions alter the redox state and atmospheric chemistry, producing observable water vapor and affecting atmospheric properties.
- [2024jwst.prop.6284C] This JWST proposal aims to directly observe signatures of magma-atmosphere interaction, specifically targeting C/O ratios and volatile abundances as diagnostics of such processes.

### rank 59 — q_059: partially_addressed (premise: supported)

**What are the key factors controlling the duration and volatile outgassing of terrestrial magma oceans, and how do these influence the initial atmospheric composition and subsequent escape processes?**

- rationale: Multiple recent studies have directly modeled how mantle redox state, volatile inventory, and stellar environment control the duration of magma oceans, volatile outgassing, and the resulting atmospheric composition and escape. While these works have made substantial progress in quantifying and simulating these processes, the full range of controlling factors and their interplay—especially for diverse exoplanetary systems—remains an active area of research, leaving the core question partially open.
- [2021BAAS...53c1102K] Directly investigates how mantle redox state controls volatile outgassing, atmospheric composition, and escape during the magma ocean period.
- [2025epsc.conf.1896N] Models how volatile concentrations and redox state in the magma ocean determine the composition and pressure evolution of the outgassed atmosphere.
- [2026absc.conf28375O] Quantifies how stellar properties and magma ocean cooling timescales affect atmospheric retention and volatile loss, linking these to initial atmospheric composition.
- [2026arXiv260620249S] Shows that volatile inventory and mantle redox state hierarchically control magma ocean duration, volatile outgassing, and resulting atmospheric composition.
- [2023AGUFM.P24A..01K] Presents a model tracking volatile partitioning, atmospheric escape, and redox evolution, directly addressing the interplay between magma ocean evolution and atmospheric outcomes.

### rank 60 — q_060: partially_addressed (premise: supported)

**How can the degeneracies between effective temperature, cloudiness, and disequilibrium chemistry in gas-giant exoplanet atmospheres be broken using broad-wavelength spectroscopic observations?**

- rationale: Several post-cutoff studies directly address the interplay and degeneracies between effective temperature, cloudiness, and disequilibrium chemistry in gas-giant exoplanet atmospheres using broad-wavelength spectroscopic observations. While these works make substantial progress—by incorporating disequilibrium chemistry into retrievals, comparing models to data, and discussing the impact of clouds and chemistry on spectra—they do not fully resolve the degeneracy problem, leaving the core question open but significantly advanced.
- [2025epsc.conf.1042P] This study directly investigates how including disequilibrium chemistry in retrievals affects the inference of key atmospheric parameters from broad-wavelength spectroscopic data, addressing the challenge of degeneracies.
- [2021A&A...648A.127B] This work uses Spitzer photometry and model grids including disequilibrium chemistry to analyze how infrared observations can distinguish between chemical and temperature effects in gas giant atmospheres.
- [2021AJ....162...37R] This paper presents a large sample analysis of HST spectra, assessing the prevalence of disequilibrium chemistry as a function of temperature, and discusses the implications for interpreting spectroscopic data.
- [2022BAAS...54e.129B] This abstract discusses the impact of disequilibrium chemistry and vertical mixing on transmission spectroscopy, highlighting the uncertainties and connections between atmospheric layers.

### rank 61 — q_061: partially_addressed (premise: supported)

**What are the limitations and biases in current mass-radius relations for small exoplanets due to selection effects in radial velocity follow-up, and how can these be mitigated to improve atmospheric characterization?**

- rationale: Recent literature has made substantial progress in identifying and quantifying the limitations and biases in mass-radius relations for small exoplanets due to selection effects in radial velocity follow-up, and has proposed or tested mitigation strategies such as alternative mass determination methods and improved survey designs. However, while these studies clarify the nature and impact of these biases and suggest ways forward, a comprehensive resolution—such as a fully unbiased mass-radius relation or universally adopted mitigation protocol—remains outstanding.
- [2025AJ....169...97D] Directly investigates how uncertainties in planetary mass, often stemming from RV follow-up limitations, bias atmospheric retrievals for small exoplanets.
- [2024ApJ...969L..22S] Explores how prior knowledge of mass and orbital parameters, often obtained via RV, impacts the accuracy of atmospheric and bulk property characterization.
- [2025arXiv250925323D] Discusses alternative approaches to mass determination that could mitigate RV selection biases and accelerate atmospheric characterization.
- [2022ExA....53..589B] Quantifies the challenges and biases in RV mass recovery for small exoplanets, relevant to selection effects and their impact on atmospheric studies.

### rank 62 — q_062: answered (premise: supported)

**How do atmospheric escape processes, as traced by helium 10830 Å absorption, vary across different exoplanet types, and what are the key physical parameters controlling the strength of this signal?**

- rationale: Multiple post-cutoff studies have directly modeled and empirically analyzed helium 10830 Å absorption across a range of exoplanet types, identifying key controlling parameters such as irradiation, temperature, and planetary size. These works collectively resolve the question by demonstrating that while age and irradiation influence the signal, the diversity of planetary and stellar properties is the dominant factor, and they clarify the physical mechanisms underlying the observed absorption strengths.
- [2025MNRAS.539.2144A] This study models helium 10830 Å absorption across a population of exoplanets, finding that while younger planets tend to show stronger signals, the diversity of system parameters (e.g., irradiation, planetary size) dominates the observed variation, directly addressing the question of key controlling parameters.
- [2024ESS.....562706B] This work presents a theoretical model linking helium absorption to planetary and stellar properties, showing that the helium triplet fraction is primarily set by gas temperature and that absorption scales with incident irradiation, identifying key physical parameters controlling the signal.
- [2024eas..conf...80A] This abstract discusses the weak correlation between age and helium absorption across exoplanet populations, emphasizing the importance of diverse planetary parameters in determining the strength of the helium signal.
- [2022EPSC...16.1011L] This presentation analyzes He 10830 Å absorption in about ten diverse exoplanets, drawing general conclusions about mass-loss rates, H/He abundances, and escape regimes, thus empirically addressing variation across exoplanet types and key parameters.
- [2025MNRAS.537.1305B] This study develops a model for helium absorption, showing that the triplet population is sensitive to temperature and that absorption is not simply a measure of outflow size, clarifying the physical interpretation of the signal.

### rank 63 — q_063: partially_addressed (premise: supported)

**How do the properties of aerosols and clouds in exoplanet atmospheres, as inferred from phase curves and scattering models, inform our understanding of atmospheric chemistry and dynamics?**

- rationale: Post-cutoff literature has made substantial progress in connecting aerosol and cloud properties inferred from phase curves and scattering models to atmospheric chemistry and dynamics, with both observational and modeling advances. However, while these studies deepen our understanding and provide new constraints, the core question remains open as the full complexity of these interactions is not yet fully resolved.
- [2021JGRE..12606655G] This review discusses how phase curves and scattering models reveal aerosol distributions and compositions, linking these properties to atmospheric chemistry and dynamics.
- [2021DPS....5330503H] This work presents experimental phase curves for exoplanet-relevant aerosols, directly connecting scattering properties to cloud composition and atmospheric processes.
- [2024APS..MARQ39006M] This abstract highlights how aerosols affect atmospheric chemistry and dynamics, referencing phase curve and observational constraints.
- [2024ESS.....562431D] This study uses phase curves to probe dynamical cloud formation, linking observed variability to condensation and evaporation processes in exoplanet atmospheres.
- [2022eas..conf.2364H] This modeling work connects cloud properties and their global distribution to atmospheric chemistry and dynamics, using phase curve-relevant outputs.

### rank 64 — q_064: not_addressed (premise: still_plausible)

**What is the impact of non-LTE effects on the inferred elemental abundances (e.g., Mg/Si) in planet-hosting stars, and how do these stellar abundances relate to the formation and composition of rocky exoplanets?**

- rationale: None of the post-cutoff abstracts substantively engage with the specific impact of non-LTE effects on inferred elemental abundances in planet-hosting stars. While several works discuss the importance of stellar abundances for exoplanet composition and the challenges in measuring them, the explicit role of non-LTE effects is not addressed, leaving the core question open and its premise untested.

### rank 65 — q_065: partially_addressed (premise: supported)

**How do the atmospheric compositions and thermal structures of warm giant exoplanets (T_eq < 1000 K) differ from their hotter counterparts, and what constraints can be placed on their formation and evolution from current and future observations?**

- rationale: Post-cutoff literature has made substantial progress in characterizing the atmospheric compositions and thermal structures of warm giant exoplanets, with new observations (e.g., JWST) providing precise constraints on key properties such as metallicity and C/O ratio. However, while these studies advance our understanding and begin to differentiate warm giants from hotter counterparts, the full picture of how these differences constrain formation and evolution remains an active area of research, leaving the core question partially addressed.
- [2023FrASS..1079000M] This review discusses the characterization of warm giant exoplanets, the connection between atmospheric and interior compositions, and how new observations (e.g., JWST, ARIEL) can constrain formation and evolution models.
- [2025PNAS..12216193W] This paper presents precise measurements of metallicity and C/O ratio for a warm giant exoplanet using JWST, directly addressing atmospheric composition and implications for formation.
- [2024jwst.prop.4938F] This proposal aims to observe the atmospheres of two warm giants to constrain their compositions and formation scenarios, highlighting the unique diagnostic power of warm giants compared to hotter planets.
- [2023A&A...671A.122H] This study models cloud formation and chemical regimes across a range of exoplanet temperatures, including warm giants, to inform observational campaigns and understand atmospheric diversity.

### rank 66 — q_066: partially_addressed (premise: supported)

**How do the assumptions of spatial uniformity in transmission spectroscopy affect the interpretation of exoplanet atmospheric properties, and can spatially resolved spectra during transit reveal 3D atmospheric structure?**

- rationale: Multiple post-cutoff works directly address the impact of spatial uniformity assumptions in transmission spectroscopy, demonstrating that 1D models can introduce biases and that multidimensional (2D/3D) models are increasingly necessary for accurate interpretation. Several studies and proposals also show that spatially and temporally resolved spectra during transit can begin to reveal 3D atmospheric structure, but the field is still developing and has not yet fully resolved all aspects of the question.
- [2022eas..conf.1370P] This work directly studies the impact of 3D atmospheric structure on transmission spectra and the biases introduced by 1D assumptions, providing quantitative guidance for retrieval models.
- [2022A&A...658A..41F] This paper presents a tool for computing transmission spectra from 1D, 2D, and 3D atmospheric structures, illustrating the necessity of multidimensional models for accurate interpretation.
- [2021AAS...23711109N] This abstract explores how incorporating 3D temperature structures into transmission spectrum models changes the interpretation compared to 1D models, and discusses the detectability of these effects.
- [2022BAAS...54e.301L] This work demonstrates the use of transit limb scanning and time-resolved high-resolution spectra to recover spatially resolved atmospheric properties, directly addressing the potential to reveal 3D structure.
- [2021jwst.prop.2113E] This proposal aims to empirically test the assumption of limb homogeneity by extracting separate spectra for the morning and evening limbs, targeting direct observational constraints on 3D structure.

### rank 67 — q_067: partially_addressed (premise: supported)

**What are the dominant sources of systematics in ground-based and space-based exoplanet transit spectroscopy, and how can advanced statistical methods (e.g., ICA, Bayesian marginalization, Gaussian processes) improve the reliability of atmospheric retrievals?**

- rationale: The post-cutoff literature makes substantial progress in identifying and mitigating dominant sources of systematics in exoplanet transit spectroscopy, with several works directly addressing the impact of instrumental, astrophysical, and data processing systematics on atmospheric retrievals. Advanced statistical methods such as Gaussian Processes, Bayesian frameworks, and covariance-aware likelihoods are shown to improve the reliability of retrievals, but the field continues to grapple with unresolved challenges, particularly in fully quantifying and correcting all sources of systematics across diverse observational regimes.
- [2023A&A...678A..41N] Directly investigates how systematic effects from data processing algorithms impact atmospheric retrievals and demonstrates that advanced statistical treatments (e.g., including the full covariance matrix) improve reliability.
- [2021EPSC...15..700P] Presents a new Gaussian Process-based method to address ground-based systematics in exoplanet transit spectroscopy, specifically targeting the limitations of traditional reference star corrections.
- [2021atat.confE..12G] Discusses the application of fully Bayesian approaches to high-resolution retrievals and addresses the challenge of filtering systematics, proposing statistical solutions.
- [2022BAAS...54e.105W] Highlights the importance of robust statistical metrics in atmospheric retrievals and the sensitivity of inferences to specific data points, advocating for Bayesian approaches.
- [2026ASTCS..1120201L] Reviews the dominant sources of systematics in retrievals from both ground and space, and outlines future directions including advanced inference methods and machine learning.

### rank 68 — q_068: answered (premise: supported)

**How do the observed UV and blue-optical transmission spectral features in ultra-hot Jupiters constrain the presence and rainout of metals and condensates, and what are the implications for atmospheric modeling?**

- rationale: Post-cutoff literature directly engaged the question by modeling and interpreting UV and blue-optical transmission spectra, identifying the roles of metals and condensates, and confirming that observed features constrain condensation and rainout processes. Observational and modeling advances have resolved how these spectral features inform atmospheric modeling, supporting the premise that such spectra are diagnostic of metal and condensate processes in ultra-hot Jupiter atmospheres.
- [2021AAS...23711101L] Directly models and interprets UV/blue-optical transmission spectra of ultra-hot Jupiters, showing how observed features constrain the presence and rainout of metals and condensates, and matches models to observations.
- [2022BAAS...54e4702L] Presents UV transmission spectra of WASP-178b, identifies specific metal and silicate absorption features, and links the onset of silicate condensation to observed spectral changes, confirming the role of condensate rainout.

### rank 69 — q_069: partially_addressed (premise: supported)

**What are the physical and chemical processes that determine the detectability of biosignatures and technosignatures in exoplanet atmospheres, and how can laboratory simulations and remote sensing inform these searches?**

- rationale: Post-cutoff literature made substantial progress in modeling, simulating, and constraining the detectability of biosignatures and technosignatures in exoplanet atmospheres, including the use of laboratory data, remote sensing, and advanced retrieval techniques. However, while these works advanced understanding and methodology, the core question of fully characterizing all relevant physical and chemical processes and their interplay in real exoplanetary environments remains open.
- [2025PSJ.....6...96C] This work simulates the detectability of biosignature and false-positive gases in exoplanet atmospheres, directly addressing the physical and chemical processes that affect biosignature detection.
- [2021cosp...43E.527Z] This abstract discusses computational quantum chemistry methods to generate spectra for potential biosignature gases, informing the chemical processes relevant to detectability.
- [2021BAAS...53c0606Y] This study uses thermodynamic modeling and simulated remote observations to assess the detectability of chemical disequilibrium biosignatures in exoplanet atmospheres.
- [2023AJ....166...39C] This paper models the detectability thresholds for prebiosignature molecules in exoplanet atmospheres using simulated JWST data, addressing the physical and observational constraints.
- [2026arXiv260120620B] This review highlights advances in modeling, retrieval, and instrumentation for biosignature detection, integrating laboratory, remote sensing, and theoretical approaches.

### rank 70 — q_070: partially_addressed (premise: supported)

**How do the properties of planetary ionospheres, as inferred from comparative studies of Mars and Earth, inform our understanding of atmospheric escape and evolution on exoplanets with and without magnetic fields?**

- rationale: The post-cutoff literature makes substantial progress in understanding how planetary ionospheres and magnetic fields affect atmospheric escape, with several studies directly comparing Mars and Earth and extending these insights to exoplanets. However, while the role of magnetic fields is shown to be more nuanced than previously thought and new models and scaling laws are developed, several abstracts note that key questions—such as the exact mechanisms, composition of escaping ions, and long-term evolutionary consequences—remain open, so the core question is not fully resolved.
- [2021SSRv..217...36R] This review directly compares ion escape processes at Mars and Earth, discusses the influence of magnetic fields, and concludes that intrinsic magnetic fields are not strictly required to prevent atmospheric escape, providing a nuanced view relevant to exoplanets.
- [2023AGUFM.P31A..02G] This study critically examines the role of magnetization in atmospheric escape, challenging the simplistic 'magnetic shield' paradigm and reviewing escape processes in light of recent observations, with implications for exoplanetary atmospheres.
- [2023AGUFMSA21B2685H] This work uses simulations to derive scaling laws for atmospheric ion escape as a function of planetary size, magnetic field strength, and ion production, directly addressing how these factors inform atmospheric evolution on exoplanets.
- [2021BAAS...53c1213K] This abstract presents new modeling tools for atmospheric escape from magnetized rocky exoplanets, validated against Earth and applied to scenarios relevant to Mars and Venus, thus linking solar system comparative studies to exoplanetary contexts.
- [2024EGUGA..26.2004D] This review discusses ion escape processes across solar system planets and their implications for atmospheric evolution and habitability, explicitly raising open questions about composition and escape mechanisms.

### rank 71 — q_071: partially_addressed (premise: supported)

**What are the key factors that control the efficiency of volcanic CO2 outgassing on stagnant-lid super-Earths, and how does this affect their long-term atmospheric evolution and habitability?**

- rationale: Post-cutoff literature has made substantial progress in identifying and modeling the key factors controlling volcanic CO2 outgassing on stagnant-lid super-Earths, such as mantle rheology, redox state, volatile content, and kinetics of gas speciation. However, while these studies clarify the mechanisms and their implications for atmospheric evolution and habitability, they do not fully resolve the quantitative efficiency of CO2 outgassing or its ultimate impact on long-term habitability, leaving the core question open.
- [2024EGUGA..2613059T] This abstract directly investigates how rheological uncertainties, including mantle viscosity and the properties of post-perovskite, affect the efficiency of volcanic outgassing on stagnant-lid super-Earths.
- [2022JGRE..12707123L] This study models how mantle redox state and volatile content control the composition and evolution of secondary volcanic atmospheres on super-Earths, linking interior properties to atmospheric outcomes.
- [2023JGRE..12807528L] This work explores the kinetics of volcanic gas speciation and its implications for the long-term evolution of volcanic atmospheres, relevant to understanding atmospheric evolution and potential habitability.
- [2023AGUFM.P13C2811S] This abstract discusses how different interior outgassing scenarios affect atmospheric composition and the location of the habitable zone, directly addressing the link between outgassing efficiency and habitability.

### rank 72 — q_072: posed_but_open (premise: still_plausible)

**How do the formation and migration histories of compact multi-planet systems with misaligned ultra-short period planets (e.g., K2-266) affect the atmospheric properties and evolution of their constituent planets?**

- rationale: Several post-cutoff works independently pose the question of how formation and migration histories, particularly orbital alignment, affect planetary atmospheric properties, but they focus on hot Jupiters rather than compact multi-planet systems with misaligned ultra-short period planets like K2-266. No abstract directly addresses the atmospheric evolution in the specific context of compact multi-planet systems with misaligned USPs, leaving the core question open and the premise still plausible but untested.
- [2024MNRAS.535..171P] This work directly investigates how formation and migration histories (including misalignment) affect atmospheric compositions, but focuses on hot Jupiters rather than compact multi-planet systems with ultra-short period planets.
- [2024ESS.....562411K] This abstract describes a survey comparing aligned and misaligned hot Jupiters to test if atmospheric composition traces formation and migration history, but does not address compact multi-planet systems or ultra-short period planets.
- [2024eas..conf.2301P] This program compares atmospheric compositions of aligned and misaligned hot Jupiters to infer formation pathways, but does not extend to compact multi-planet systems with misaligned ultra-short period planets.

### rank 73 — q_073: partially_addressed (premise: supported)

**How do the physical conditions in the atmospheres of hot Jupiters affect the generation and escape of radio emission, and what are the prospects for detecting exoplanetary radio signals given the constraints of expanded ionospheres?**

- rationale: Post-cutoff literature, especially 2025Icar..44116708J, directly models the impact of hot Jupiter ionospheric conditions on radio signal reflection and absorption, and assesses detectability prospects, making substantial progress on the question. However, while the work advances understanding and provides detectability estimates, it does not fully resolve all aspects of radio emission generation and escape, leaving the core question partially open.
- [2025Icar..44116708J] Directly investigates how high-density ionospheres in hot Jupiters affect radio signal reflection and absorption, and discusses detectability with next-generation radio telescopes.
- [2021AAS...23711103H] Explores hydrodynamic escape and radiative cooling in hot Jupiter atmospheres, relevant to understanding atmospheric structure and escape processes that impact radio emission generation and escape.

### rank 74 — q_074: partially_addressed (premise: still_plausible)

**What are the effects of magnetic diffusion and Alfvénic wave dissipation on atmospheric escape rates from hot Jupiters, and how do these processes depend on planetary and stellar parameters?**

- rationale: Post-cutoff literature has made substantial progress in modeling the effects of planetary magnetic fields and Alfvénic regimes on atmospheric escape rates from hot Jupiters, particularly through advanced 3D MHD simulations that explore dependencies on planetary magnetic field strength and interaction regime. However, while these studies address magnetic confinement and outflow structure, they do not fully resolve the quantitative role of magnetic diffusion and Alfvénic wave dissipation, nor do they comprehensively map the dependence on a wide range of planetary and stellar parameters, leaving the core question open.
- [2024MNRAS.534.3622P] This study uses 3D radiation-MHD simulations to directly investigate how planetary magnetic field strength and sub-Alfvénic interactions affect atmospheric escape rates from hot Jupiters, finding that escape rates depend on magnetic regime and field strength.
- [2023IAUS..370..232V] This work examines the effect of planetary magnetic fields on observational signatures of atmospheric escape in hot Jupiters, relevant to the magnetic diffusion aspect of the question.

### rank 75 — q_075: partially_addressed (premise: supported)

**How can high-resolution spectroscopy and new observational techniques (e.g., refracted light, phase curves, direct imaging) be used to discriminate between different atmospheric compositions and structures in exoplanets?**

- rationale: Post-cutoff literature demonstrates substantial progress in using high-resolution spectroscopy and new observational techniques to discriminate between exoplanet atmospheric compositions and structures, including joint analyses and retrieval frameworks that combine multiple methods. However, while these works show the power and promise of these techniques and report successful discrimination in some cases, the literature indicates that the field is still developing, with heterogeneous samples and some core challenges remaining unresolved.
- [2025ARA&A..63...83S] This review details how high-resolution spectroscopy enables discrimination of atmospheric species, temperature structures, and even isotopic ratios, directly addressing the use of advanced techniques to distinguish atmospheric compositions and structures.
- [2026AAS...24713403S] This dissertation presents joint analyses combining high- and low-resolution spectroscopy, demonstrating their complementary strengths in constraining exoplanet atmospheric properties and compositions.
- [2022EPSC...16.1233M] This work introduces a new approach for simultaneous modeling of low- and high-resolution spectra, resolving controversies in atmospheric composition and advocating for joint analysis to maximize information.
- [2023AAS...24114202D] This abstract describes the use of high-contrast imaging and reflection spectroscopy, with Bayesian retrievals to distinguish between different atmospheric compositions (e.g., H2O- or CO2-dominated) in temperate rocky exoplanets.

### rank 76 — q_076: partially_addressed (premise: supported)

**What are the dominant microphysical processes (nucleation, condensation, evaporation) that control cloud formation and evolution in exoplanet atmospheres, and how do these processes vary with temperature, metallicity, gravity, and eddy mixing?**

- rationale: Post-cutoff literature has made substantial progress in modeling and simulating the microphysical processes (nucleation, condensation, evaporation) that control cloud formation and evolution in exoplanet atmospheres, and has systematically explored their dependence on temperature, metallicity, gravity, and eddy mixing. However, while these studies provide detailed models and identify key dependencies, the question of which processes are universally dominant and how they interact across the full diversity of exoplanet atmospheres remains open, so the question is partially addressed and the premise is supported.
- [2024A&A...682A.150K] This work presents a fully time-dependent, non-equilibrium model of cloud formation in exoplanet atmospheres, explicitly modeling nucleation, condensation, and their interaction with gas-phase chemistry.
- [2024ApJ...966..152Y] This study uses a microphysical model to simulate nucleation, condensation, evaporation, and other processes, and systematically explores how these vary with planetary parameters such as gravity, pressure, and stellar flux.
- [2022BAAS...54e.267Y] This abstract reports on the impact of planetary parameters (gravity, pressure, stellar radiation, vertical mixing) on cloud microphysics, including nucleation, condensation, and evaporation, in terrestrial exoplanets.
- [2023A&A...671A.122H] This paper applies a kinetic cloud model to 3D GCMs, modeling nucleation, growth, evaporation, and gravitational settling, and examines how cloud formation trends vary with host star and planetary parameters.
- [2022eas..conf.2364H] This overview discusses how cloud microphysical processes (nucleation, growth, evaporation) and their global distributions are determined by system parameters, including temperature and gravity.

### rank 77 — q_077: partially_addressed (premise: still_plausible)

**What causes the observed scatter and local minimum in cloudiness at ~1300 K in exoplanet atmospheres, and can current cloud microphysics models reproduce this feature?**

- rationale: Recent literature has advanced microphysical cloud modeling, including detailed treatments of particle growth, fragmentation, and porosity, and applied these models to exoplanet atmospheres in the relevant temperature regime. However, while these works address the processes that could cause scatter and minima in cloudiness near 1300 K, they do not explicitly confirm that current models can fully reproduce the observed feature, leaving the core question open but with substantial progress made.
- [2022eas..conf..773S] This work uses a kinetic cloud formation model to study how particle-particle collisions (coagulation, fragmentation) affect cloud properties across a range of temperatures, including the regime near 1300 K, and investigates resulting optical depths.
- [2021EGUGA..2310235S] This abstract discusses the application of a microphysical cloud model (including growth, fragmentation, and porosity) to gas-giant exoplanets, with attention to how these processes affect cloud optical depths and particle properties.
- [2024A&A...692A.222K] This study presents a 3D model coupling atmospheric dynamics and detailed kinetic cloud microphysics, allowing exploration of cloud particle distributions and opacities in warm Saturn-like exoplanets, relevant to understanding cloudiness trends.

### rank 78 — q_078: answered (premise: supported)

**How does the presence and composition of high-altitude clouds or hazes affect the detectability and interpretation of molecular features in exoplanet transmission spectra, especially for super-Earths like GJ1214b?**

- rationale: Multiple post-cutoff studies, including those using JWST data, have directly modeled and constrained the effects of high-altitude clouds and hazes on the detectability and interpretation of molecular features in exoplanet transmission spectra, with a particular focus on GJ 1214b. These works demonstrate that both the presence and composition of clouds/hazes can significantly obscure or modify molecular signatures, and that new observational and modeling techniques can partially or fully disentangle these effects, thus substantially resolving the original research question.
- [2023ApJ...943L..26C] This study directly investigates how photochemical haze composition (specifically C/O ratio) affects the detectability of molecular features in GJ 1214b's transmission spectrum, showing that haze properties can obscure or reveal molecular signatures.
- [2024EPSC...17..574L] This work uses JWST data and self-consistent modeling to characterize the interplay of clouds and hazes in GJ 1214b, demonstrating how their properties affect spectral interpretation and molecular detectability.
- [2023DPS....5522308L] This abstract explores whether photochemical hazes or clouds are responsible for GJ 1214b's featureless spectrum, modeling their formation and impact on observed spectra.
- [2022eas..conf..512D] This study discusses how high-resolution spectroscopy can detect molecular features above cloud decks, directly addressing the challenge posed by clouds/hazes in transmission spectra.

### rank 79 — q_079: partially_addressed (premise: supported)

**To what extent do non-uniform (inhomogeneous) aerosol and cloud distributions on exoplanets affect observed transmission spectra, and can ingress/egress spectra be used to map global aerosol structure?**

- rationale: Post-cutoff literature has made substantial progress in modeling and understanding the effects of inhomogeneous aerosol and cloud distributions on exoplanet transmission spectra, confirming that such heterogeneity can significantly alter observed features. However, while the impact on spectra is addressed, the specific use of ingress/egress spectra to map global aerosol structure is not directly resolved in the provided abstracts, leaving that aspect of the question open.
- [2022eas..conf.1370P] This work directly studies the impact of 3D (inhomogeneous) atmospheric structure on transmission spectra and discusses retrieval biases, addressing the effect of non-uniform aerosols and clouds.
- [2026MNRAS.545f2066O] This paper investigates how clumpy (heterogeneous) aerosol distributions affect transmission spectra, showing that such distributions can explain observed flat spectra in sub-Neptunes.
- [2021JGRE..12606655G] This review summarizes evidence for inhomogeneous aerosol distributions in exoplanet atmospheres and their impact on observed spectra.

### rank 80 — q_080: answered (premise: supported)

**What is the physical origin of the clustering of hot Jupiter nightside temperatures around 1100 K, and can this be explained solely by optically thick nightside clouds, or are additional processes required?**

- rationale: Post-cutoff literature directly addressed the physical origin of the clustering of hot Jupiter nightside temperatures around 1100 K, with multiple studies showing that optically thick nightside clouds—especially silicates—can explain the observed phenomenon. These works also note that the radiative timescale's dependence on temperature plays a role, but do not require additional processes beyond clouds and radiative physics to explain the clustering, thus substantially resolving the question and supporting the premise.
- [2021ApJ...918L...7G] This study directly investigates the clustering of hot Jupiter nightside temperatures around 1100 K and finds that optically thick silicate clouds on the nightside can explain the observed temperature constancy.
- [2021MNRAS.501...78P] This work shows that nightside clouds can explain the low, nearly constant nightside temperatures, but also notes that the radiative timescale's temperature dependence contributes to the effect.

### rank 81 — q_081: partially_addressed (premise: supported)

**How do bulk atmospheric composition (e.g., molecular mass, specific heat) and metallicity affect the atmospheric dynamics, temperature, and wind distributions of tidally locked sub-Jupiter-sized exoplanets?**

- rationale: Recent literature has made substantial progress in modeling how bulk atmospheric composition and metallicity affect the temperature structure, chemistry, and dynamics of tidally locked sub-Jupiter exoplanets, particularly through 3D GCMs and coupled chemistry-cloud models. However, while these studies demonstrate strong feedbacks and dependencies, they do not fully resolve the quantitative relationships or provide a comprehensive predictive framework, leaving the core question open but significantly advanced.
- [2024MNRAS.529.2686L] This study uses a 3D general circulation model to simulate a metal-enhanced sub-Jupiter exoplanet, directly investigating how metallicity and chemical/cloud feedback affect 3D temperature structure and atmospheric dynamics.
- [2025AAS...24531401M] This work explores how planetary properties such as metallicity and intrinsic heat flux influence atmospheric chemistry and temperature structure in sub-Neptunes and gas giants, including tidally locked planets.
- [2021MNRAS.505.5603B] This paper models the impact of temperature, rotation, and mixing on the chemistry and wind distributions of tidally locked exoplanets, finding temperature to be a dominant factor.

### rank 82 — q_082: partially_addressed (premise: supported)

**What processes move the infrared photospheres of cooler hot Jupiters to lower pressures, leading to discrepancies between observed and predicted dayside-nightside temperature differences?**

- rationale: Post-cutoff literature has made substantial progress in identifying nightside silicate clouds as a key process moving the infrared photosphere to lower pressures in cooler hot Jupiters, thereby explaining much of the observed discrepancy in dayside-nightside temperature differences. However, while these studies provide strong evidence and modeling support for the cloud hypothesis, some aspects—such as the full diversity of observed temperature contrasts and the precise interplay of dynamics, opacity, and cloud microphysics—remain incompletely resolved.
- [2021ApJ...918L...7G] This study directly investigates how nightside silicate clouds in hot Jupiters move the infrared photosphere to lower pressures, explaining observed temperature discrepancies.
- [2021AAS...23723705K] This dissertation discusses the role of clouds, especially silicates, in setting nightside temperatures and the resulting day-night temperature differences in hot Jupiters.
- [2026ApJ..1004..102F] This work finds that 3D models still overpredict emission and identifies nightside clouds as a likely explanation for observed discrepancies, but notes that models do not fully reproduce all observed features.
- [2023ApJ...957...22Z] This paper explores how atmospheric dynamics and opacity inhomogeneities, including those from clouds, affect heat flow and the location of the infrared photosphere in hot Jupiters.

### rank 83 — q_083: not_addressed (premise: still_plausible)

**How do CO2 ice clouds influence the outer boundary of the habitable zone for terrestrial exoplanets around different stellar types, and what are the limits of the scattering greenhouse effect?**

- rationale: None of the provided post-cutoff abstracts substantively engage with the specific question of how CO2 ice clouds influence the outer boundary of the habitable zone or the limits of the scattering greenhouse effect. The premise that CO2 ice clouds could affect the habitable zone's outer edge remains plausible but untested in this literature.

### rank 84 — q_084: partially_addressed (premise: supported)

**What are the dominant sources of extended and escaping atmospheres (e.g., He, H, C, Mg, Ca) in close-in exoplanets, and how do processes like photoevaporation and outgassing from Trojan satellites contribute?**

- rationale: Post-cutoff literature has made substantial progress in identifying photoevaporation and hydrodynamic escape as dominant sources of extended and escaping atmospheres in close-in exoplanets, with some work also modeling outgassing from planetary interiors as a contributor. However, while these studies advance understanding and provide new models and observational strategies, the relative contributions of all processes (including outgassing from Trojans) and the detailed composition of escaping atmospheres remain incompletely resolved.
- [2026ASTCS..1130201M] Reviews physical processes driving atmospheric escape in exoplanets, emphasizing photoevaporation and the role of atmospheric composition, with models and observations supporting hydrodynamic outflows as dominant for close-in planets.
- [2022eas..conf.2490O] Discusses atmospheric escape in close-in exoplanets, highlighting photoevaporation and core-powered escape as dominant mechanisms, and notes spectroscopic detection of escaping H and He.
- [2026PSJ.....7...84A] Presents a model where volcanic outgassing from tidally heated exoplanets can sustain H2-dominated atmospheres, directly addressing outgassing as a source of extended atmospheres.
- [2022BAAS...54e2805O] Explores how atmospheric escape can alter the chemical inventory of exoplanet atmospheres, including the loss of heavy elements and the evolution of C/O ratios, using multi-species escape models.

### rank 85 — q_085: partially_addressed (premise: supported)

**How does the variability of the host star (e.g., starspots, flares, rotational modulation) impact the detectability and accuracy of exoplanet phase curves and atmospheric characterization?**

- rationale: Post-cutoff literature has made substantial progress in quantifying and modeling the impact of host star variability—such as spots, flares, and rotational modulation—on the detectability and accuracy of exoplanet phase curves and atmospheric characterization. However, while these studies have clarified the mechanisms and emphasized the need for improved modeling and correction techniques, the core challenge of fully disentangling stellar and planetary signals remains open.
- [2021tsc2.confE.105L] This work demonstrates that unmodeled stellar variability can mimic or obscure exoplanet phase curve signals, directly addressing the impact of host star variability on phase curve detectability and accuracy.
- [2022EPSC...16..266T] This abstract discusses how stellar activity, particularly spots and faculae, contaminates exoplanet transmission spectra and emphasizes the need for complex stellar models to disentangle planetary and stellar signals.
- [2026A&A...709A.153L] This study simulates the impact of stellar spots on high-resolution transmission spectra, showing how spot properties affect the detectability and characterization of exoplanet atmospheres.
- [2021tsc2.confE.137S] This work highlights how stellar variability in exoplanet host stars can lead to false positive exoplanet signatures, especially when variability periods match planetary orbital periods.

### rank 86 — q_086: answered (premise: supported)

**What are the chemical and physical processes responsible for the observed depletion of CH4 and NH3 and the presence of H2O in the atmosphere of habitable-zone exoplanet K2-18b, and do these indicate chemical disequilibrium?**

- rationale: Post-cutoff literature directly addresses the chemical and physical processes responsible for the observed abundances of CH4, NH3, and H2O in K2-18b's atmosphere, using new JWST data and advanced non-equilibrium chemistry models. These studies confirm the necessity of non-equilibrium processes to explain the observed atmospheric composition, robustly detect methane, and support the premise that chemical disequilibrium is present in K2-18b's atmosphere.
- [2025sf2a.conf...55J] This study uses JWST data and non-equilibrium chemistry models to show that methane (CH4) is robustly detected in K2-18b's atmosphere, and that non-equilibrium chemistry is necessary to interpret the observed atmospheric features.
- [2025A&A...701A..33J] This work explores the parameter space of metallicity, C/O ratio, and vertical mixing for K2-18b using non-equilibrium models and JWST data, confirming the importance of non-equilibrium chemistry in explaining the atmospheric composition.
- [2026ApJ..1002L..34P] This paper reports the detection of methane and carbon dioxide in K2-18b's atmosphere using JWST, and conducts a broad search for other trace molecules, supporting the presence of chemical disequilibrium.

### rank 87 — q_087: answered (premise: supported)

**How do photochemical processes in exoplanet atmospheres produce potential biosignature gases (e.g., O2, organics) abiotically, and what are the implications for false positive biosignature detection?**

- rationale: Multiple post-cutoff studies directly model and experimentally investigate photochemical and related abiotic processes that generate potential biosignature gases (O2, organics) in exoplanet atmospheres, quantifying their production and implications for false positive detection. These works confirm that such abiotic processes can produce detectable levels of these gases under certain conditions, supporting the premise and substantially resolving the question by clarifying the mechanisms and limits of abiotic biosignature gas production.
- [2024AGUFMP43C.3024T] This study directly models photochemical production of O2 and O3 in CO2-rich, H2O-poor exoplanet atmospheres, quantifying abiotic pathways and their implications for false positive biosignature detection.
- [2024A&A...686A..58B] This work combines laboratory experiments and photochemical modeling to show how lightning and photochemistry can abiotically produce potential biosignature gases, and assesses their detectability and implications for false positives.
- [2022JGRE..12706853F] This paper simulates abiotic O2 and O3 production via atmospheric exchange and photochemistry, evaluating the plausibility of false positive biosignature detections in exoplanet atmospheres.
- [2021AAS...23750507F] This abstract describes photochemical modeling of abiotic O2 and O3 production from external influxes, directly addressing the potential for false positive biosignature detection.

### rank 88 — q_088: partially_addressed (premise: supported)

**How do atmospheric tides and core-mantle friction interact to determine the spin evolution and equilibrium rotation states of Earth-sized exoplanets, especially in the habitable zone?**

- rationale: Recent literature has made substantial progress in modeling the interaction between atmospheric tides and solid-body (including core-mantle) tides, especially regarding their combined effect on the spin evolution and equilibrium rotation states of Earth-sized exoplanets in habitable zones. However, while the dependence on atmospheric properties and the feasibility of asynchronous rotation have been clarified, a comprehensive resolution of the interplay with core-mantle friction specifically remains open, leaving the core question only partially addressed.
- [2024PSJ.....5..218S] Directly investigates how atmospheric thermal tides interact with gravitational tides to determine equilibrium rotation states of Earth-sized exoplanets in habitable zones, finding that asynchronous rotation is only feasible under specific atmospheric conditions.
- [2022PSJ.....3..162N] Develops theory and simulations for atmospheric gravitational tides on Earth-like planets, showing strong atmospheric tides can impact meteorology but have limited effect on climate and do not dominate over solid-body tides.
- [2022EPSC...16.1007R] Reviews the importance of both solid and atmospheric tides in determining spin evolution and equilibrium states, noting the need to include atmospheric tides for planets with atmospheres.

### rank 89 — q_089: answered (premise: supported)

**What is the impact of topography and land/ocean distribution on the climate and habitability of exoplanets, and how do these factors alter predictions from aquaplanet models?**

- rationale: Post-cutoff literature has directly engaged with and substantially resolved the question by demonstrating, through advanced modeling, that topography and land/ocean distribution significantly alter climate dynamics and habitability predictions compared to aquaplanet models. These studies confirm the premise that such surface features are critical for accurate exoplanet habitability assessment, moving beyond the limitations of aquaplanet assumptions.
- [2024ApJ...974..139S] This study directly investigates how landmass distribution and orography affect atmospheric dynamics and chemistry on a terrestrial exoplanet, showing significant departures from aquaplanet models.
- [2025EGUGA..27.4476G] This work compares the impact of topography and land/ocean layout on exoplanet climate and habitability, highlighting their critical role and the limitations of parameterized (often aquaplanet) models.

### rank 90 — q_090: partially_addressed (premise: supported)

**How do the properties of clouds and hazes (composition, particle size distribution, vertical structure) in exoplanet atmospheres affect lightning occurrence and atmospheric ionization?**

- rationale: Several post-cutoff studies directly model the relationship between cloud properties (such as cloud-top height, particle size distribution, and vertical structure) and lightning occurrence or atmospheric ionization in exoplanet atmospheres, often using advanced climate-chemistry models. However, while these works make substantial progress in linking cloud/haze microphysics to lightning and ionization, they do not fully resolve the detailed mechanisms or quantify the effects across the full diversity of exoplanet atmospheres, leaving the core question open.
- [2022MNRAS.517.2383B] This study directly models lightning occurrence in exoplanet atmospheres, parameterizing lightning as a function of cloud-top height and examining the chemical impact of lightning, thus linking cloud properties to lightning and atmospheric ionization.
- [2022BAAS...54e.138B] This abstract describes modeling of lightning on exoplanets, with lightning parameterized by cloud-top height and its chemical effects, addressing the connection between cloud properties and lightning occurrence.
- [2021AGUFM.P45B2426B] This work uses a global circulation model to study lightning emergence and its chemical impact on exoplanets, considering the distribution of lightning flashes and their influence on atmospheric composition.
- [2023A&A...671A.122H] This paper models cloud formation and the emergence of ionospheres in exoplanet atmospheres, examining how cloud properties and atmospheric structure relate to ionization processes.
- [2026ASTCS..1160083N] This study develops a microphysical model of cloud-haze interactions, showing how these interactions affect particle size distributions and vertical structure, which are relevant to lightning and ionization potential.

### rank 91 — q_091: partially_addressed (premise: supported)

**Can the polarization of thermal emission from exoplanets and brown dwarfs be robustly detected, and what constraints does this place on their rotation rates and cloud properties?**

- rationale: Post-cutoff literature has made substantial progress in modeling and predicting the polarization of thermal emission from exoplanets and brown dwarfs, showing that such signals are in principle detectable and sensitive to rotation and cloud properties. However, robust, routine observational detections and the use of polarization to tightly constrain rotation rates and cloud properties remain in the modeling and preparatory stage, with only limited direct detections reported so far.
- [2022ApJ...927...51C] Presents detailed models predicting detectable polarization in thermal emission from exoplanets and brown dwarfs, linking polarization to rotation and cloud properties.
- [2026MNRAS.545f2190W] Demonstrates how polarized thermal emission can constrain cloud grain size and temperature structure, with explicit modeling of polarization spectra.
- [2024AAS...24323004G] Models expected polarization signals for specific directly imaged exoplanets, exploring the effects of cloud properties and inclination on detectability.

### rank 92 — q_092: partially_addressed (premise: supported)

**How do magnetic fields in exoplanet atmospheres influence atmospheric escape, composition, and interaction with stellar wind, and can spectropolarimetric observations in the He I 1083 nm line reliably detect such fields?**

- rationale: Post-cutoff literature has made substantial progress in modeling and interpreting how exoplanetary magnetic fields influence atmospheric escape and the resulting signatures in the He I 1083 nm line, including the development of methods to constrain magnetic field strengths from transit spectroscopy. However, while these studies advance theoretical understanding and propose observational diagnostics, they do not yet provide definitive, routine detection of exoplanetary magnetic fields via spectropolarimetry, leaving the core question partially open.
- [2024MNRAS.527.5117S] This work directly investigates the detectability of exoplanetary magnetic fields via He I 1083 nm transit spectroscopy, modeling how magnetic field strength alters the line profile and discussing observational constraints.
- [2022eas..conf.1372N] This study uses 3D hydrodynamic simulations to explore how planetary magnetic fields and stellar wind interactions affect the He I 1083 nm line, linking magnetic field-induced anisotropy to observable spectral features.
- [2024xrp..prop...96M] This abstract discusses the importance of magnetic fields for atmospheric escape and the potential for helium absorption signatures to probe planetary magnetic fields, highlighting the need for such measurements.
- [2024cosp...45..502R] This work analyzes how magnetic fields affect atomic alignment and absorption in multiplet lines during exoplanet transits, providing theoretical groundwork for interpreting spectropolarimetric observations.

### rank 93 — q_093: answered (premise: supported)

**What are the limitations of current molecular opacity databases and line profile models (e.g., Voigt profile, line sampling) for exoplanet atmosphere modeling, and how do these affect retrievals of atmospheric composition?**

- rationale: Multiple post-cutoff studies directly address the limitations of molecular opacity databases and line profile models, quantifying their impact on exoplanet atmospheric retrievals and demonstrating that these limitations induce significant biases and uncertainties in derived atmospheric properties. The premise that current opacity data and line profile models limit the accuracy of exoplanet atmosphere modeling is strongly supported by these works, which also propose paths forward but confirm the core limitations and their effects.
- [2022NatAs...6.1287N] This paper directly quantifies the limitations of current opacity models, showing they impose an 'accuracy wall' on atmospheric retrievals and induce significant biases in derived parameters.
- [2024AAS...24331403D] This work extends the analysis to JWST data, confirming that opacity model limitations propagate into substantial uncertainties and biases in atmospheric composition retrievals, but also notes some cases where retrievals are robust.
- [2022FrASS...8..218T] This review discusses the trade-offs between completeness and accuracy in molecular line lists, highlighting how these limitations affect exoplanet atmosphere modeling.
- [2021ApJS..254...34G] This study demonstrates that differences in line lists and opacity data can lead to significant variations in modeled spectra and atmospheric properties.
- [2021isms.confEWF04G] This abstract notes that incomplete line lists and pressure broadening data introduce biases and uncertainties in atmospheric retrievals, affecting key parameters like C/O ratio.

### rank 94 — q_094: partially_addressed (premise: supported)

**How do updates to chemical reaction networks, such as methanol chemistry, alter the predicted atmospheric compositions of warm Neptunes and brown dwarfs, and what are the observational consequences?**

- rationale: Recent literature has made substantial progress by updating chemical reaction networks (including methanol and complex hydrocarbons), applying them to warm Neptunes and brown dwarfs, and directly assessing the impact on predicted atmospheric compositions and observable spectra. However, while these studies demonstrate significant advances and show that network updates can alter both composition and spectral predictions, the full range of observational consequences and the detailed interplay for all relevant species (e.g., methanol specifically) remain areas of ongoing research, leaving the core question not fully resolved.
- [2024A&A...682A..52V] This work presents an updated and validated C/H/O/N chemical network for hot exoplanet atmospheres, compares predictions for warm Neptunes, and examines the impact on abundance profiles and transmission spectra.
- [2024ApJ...966..189Y] This study introduces automated chemical reaction network generation for exoplanet atmospheres, demonstrating improved modeling of atmospheric composition and observational spectra for warm Neptunes.
- [2026ApJ..1003L..16Y] This paper uses a comprehensive carbon reaction network to model hydrocarbon and aerosol formation in sub-Neptunes, linking chemical network updates to observable spectral trends.

### rank 95 — q_095: partially_addressed (premise: supported)

**What are the key factors that determine the presence and detectability of temperature inversions in irradiated brown dwarfs and ultra-hot Jupiters, and how do UV-dominated irradiation and atmospheric composition contribute?**

- rationale: Post-cutoff literature has made substantial progress in identifying key factors—such as UV irradiation, the presence of shortwave absorbers (e.g., TiO, VO), and atmospheric dynamics like cold-trapping—that determine the presence and detectability of temperature inversions in irradiated brown dwarfs and ultra-hot Jupiters. However, while these studies provide strong evidence for the roles of irradiation and composition, the full interplay of all factors and their quantitative contributions remain areas of active research, leaving the core question not fully resolved.
- [2021csss.confE..94L] This work models highly irradiated brown dwarfs, showing that intense UV irradiation can induce temperature inversions, directly addressing the role of irradiation and atmospheric composition.
- [2022eas..conf.1361P] This study detects titanium oxide and other metals in an ultra-hot Jupiter, supporting the role of specific atmospheric absorbers in causing temperature inversions.
- [2022A&A...658A..42P] This paper discusses the importance of visible absorbers like TiO and VO in producing temperature inversions in hot and ultra-hot Jupiters, and highlights the impact of atmospheric composition and irradiation.
- [2026ASTCS..1130004S] This survey finds that nightside cold-trapping of refractory species affects dayside thermal inversions, linking atmospheric composition and irradiation to inversion detectability.

### rank 96 — q_096: partially_addressed (premise: supported)

**How can machine learning and advanced retrieval techniques (e.g., Bayesian neural networks, nested sampling) be validated and optimized for robust atmospheric parameter inference from exoplanet spectra?**

- rationale: Recent literature has made substantial progress in benchmarking, validating, and optimizing machine learning and advanced retrieval techniques for exoplanet atmospheric parameter inference, including uncertainty quantification and real-data validation. However, while these studies demonstrate robust performance and validation, the field continues to develop, and no single approach has been universally established as optimal, leaving the core question partially open.
- [2025arXiv250804982F] This work systematically benchmarks multiple machine learning regression techniques for exoplanet atmospheric retrieval, quantifies uncertainties, and validates the best-performing model on real JWST data, directly addressing validation and optimization.
- [2023DPS....5522303F] This abstract compares supervised and semi-supervised machine learning methods for atmospheric retrieval, benchmarking accuracy, precision, efficiency, and computational cost, and quantifies uncertainties.
- [2022PSJ.....3...91H] This study presents a forward ML surrogate model for radiative transfer, enabling fast Bayesian retrievals and demonstrating good agreement with traditional Bayesian methods, thus validating ML approaches.

### rank 97 — q_097: partially_addressed (premise: supported)

**How do the C/O and metallicity ratios of directly imaged exoplanets compare to their host stars, and what does this imply about their formation mechanisms?**

- rationale: The post-cutoff literature has made substantial progress in measuring and comparing C/O and metallicity ratios in directly imaged exoplanets and their host stars, and has begun to link these measurements to planet formation mechanisms. However, while several studies directly compare host star and planet abundances and discuss implications for formation, the field still lacks a comprehensive, statistically robust resolution of how these abundance ratios map onto specific formation pathways, leaving the core question open but significantly advanced.
- [2026AJ....171...21B] Directly compares C/O ratios of host stars and their directly imaged companions, finding diversity and some superstellar C/O in companions, which is relevant to formation mechanisms.
- [2025AJ....169...55B] Measures C/O and metallicity in host stars of directly imaged planets, and discusses implications for planet formation, but does not always provide direct planet-star comparisons.
- [2023AJ....166...85H] Analyzes C/O ratios in directly imaged planets, finds a trend with companion mass, and discusses implications for formation mechanisms.
- [2024ApJ...969L..21B] Synthesizes disk and planet C/O ratios, compares them, and discusses implications for core accretion versus gravitational instability formation scenarios.
- [2026AAS...24735004L] Standardizes metallicity and C/O measurements across exoplanet populations, revealing population-level trends relevant to formation, but not always direct planet-host star comparisons.

### rank 98 — q_098: partially_addressed (premise: supported)

**What are the observational signatures and physical mechanisms of star-planet interactions (SPI) in systems with hot Jupiters, and how do these affect stellar activity and planetary atmospheric loss?**

- rationale: Post-cutoff literature has made substantial progress in modeling and characterizing the physical mechanisms of star-planet interactions in hot Jupiter systems, particularly regarding planetary wind interactions with stellar coronae and magnetic fields, and their potential to produce observable stellar activity enhancements. However, while these studies provide strong theoretical and some observational support for SPI-induced activity and atmospheric loss, the core question of the definitive observational signatures and the full causal chain between SPI, stellar activity, and planetary atmospheric loss remains open and under active investigation.
- [2022AN....34310096C] This work uses 3D MHD simulations to show that planetary winds from hot Jupiters can interact with the stellar corona, producing observable signatures such as enhanced stellar activity at certain orbital phases.
- [2022csss.confE.163C] This study models the interaction of hot Jupiter winds with stellar magnetic fields, finding that planetary outflows can perturb the stellar field and potentially generate observable activity signatures via shocks and magnetic reconnection.
- [2021csss.confE..95C] This abstract discusses modeling the interaction between planetary winds and the stellar corona, aiming to determine if such interactions enhance stellar activity.
- [2025arXiv250213262S] This review summarizes observational and theoretical advances in magnetic star-planet interactions, including their signatures (activity enhancements) and implications for atmospheric erosion.
- [2025AAS...24634206D] This work simulates atmospheric mass loss in hot Jupiters due to stellar irradiation, contributing to understanding planetary atmospheric escape but not directly linking it to stellar activity signatures.

### rank 99 — q_099: partially_addressed (premise: supported)

**How can ground-based high-resolution spectroscopy and novel instrument concepts (e.g., Oxyometer, crossfaded EDI) be leveraged to detect biosignature gases and atmospheric features in exoplanets, overcoming telluric and instrumental limitations?**

- rationale: Post-cutoff literature has made substantial progress in developing and demonstrating novel ground-based high-resolution spectroscopic instruments and data analysis methods to detect biosignature gases in exoplanet atmospheres, with specific attention to overcoming telluric and instrumental challenges. However, while these works advance the field and demonstrate feasibility, the core challenge of robustly detecting biosignatures from the ground remains open, so the question is only partially addressed and the premise is supported by ongoing technical progress.
- [2024NatSR..1427356R] Reviews recent developments in ground-based high-resolution spectroscopic instruments for exoplanet atmospheres, including progress toward detecting biosignature gases and overcoming telluric and instrumental limitations.
- [2023A&A...678A.114R] Demonstrates a novel Fabry-Perot instrument prototype for ultra-high-resolution ground-based spectroscopy aimed at detecting O2 in exoplanet atmospheres, specifically addressing telluric disentanglement.
- [2021EPSC...15..700P] Introduces a new ground-based spectrophotometric method using Gaussian Processes to overcome telluric and instrumental systematics in exoplanet atmospheric observations.

### rank 100 — q_100: partially_addressed (premise: supported)

**What are the effects of stellar high-energy radiation (X-ray, EUV, FUV) on the atmospheric evolution, photochemistry, and potential habitability of exoplanets orbiting M-dwarfs?**

- rationale: Multiple post-cutoff studies directly model or review the effects of M-dwarf high-energy radiation (X-ray, EUV, FUV) on exoplanet atmospheric evolution, photochemistry, and habitability, providing substantial progress and new insights. However, the literature acknowledges significant remaining uncertainties and knowledge gaps, especially regarding the long-term outcomes and comprehensive theoretical frameworks, so the core question remains open.
- [2023MNRAS.518.2472R] This study uses 3D modeling to directly examine the impact of stellar flares on the atmospheric composition and habitability of terrestrial exoplanets orbiting M-dwarfs, finding significant photochemical changes and implications for surface UV shielding.
- [2021cosp...43E1949A] This work models the impact of M-dwarf flares and high-energy radiation on atmospheric escape and surface radiation dose, directly addressing atmospheric evolution and habitability.
- [2026ASTCS..1150202C] This review summarizes observational evidence linking stellar high-energy radiation to atmospheric escape and habitability for exoplanets, highlighting the importance of X-ray and UV irradiation.
- [2022cosp...44..593G] This abstract discusses how energetic radiation from M-dwarfs erodes planetary atmospheres and controls upper atmospheric chemistry, emphasizing the need for further theoretical and observational work.
- [2021AGUFM.P55D1974R] This study presents 3D simulations of the impact of M-dwarf stellar flares on the atmospheric chemistry and surface habitability of Earth-like exoplanets.

### rank 101 — q_101: partially_addressed (premise: supported)

**How do the histories of stellar XUV irradiation, rather than present-day XUV flux, affect the atmospheric mass loss and current atmospheric composition of short-period exoplanets, and can accurate reconstructions of individual stars' XUV histories robustly test the photoevaporation hypothesis for the sub-Jovian desert and radius gap?**

- rationale: Multiple post-cutoff works directly address the importance of stellar XUV irradiation histories (not just present-day flux) for atmospheric mass loss and the evolution of short-period exoplanet atmospheres, with several studies modeling or empirically investigating the time-dependent effects of XUV on atmospheric escape. However, while these works advance understanding and highlight the complexity and necessity of considering XUV history, they do not yet provide robust, systematic reconstructions for individual stars that definitively test the photoevaporation hypothesis for the sub-Jovian desert and radius gap, leaving the core question open but substantially progressed.
- [2021MNRAS.501L..28K] This paper demonstrates that stellar EUV irradiation declines more slowly than previously assumed, emphasizing the importance of long-term XUV history for atmospheric escape and complicating the use of stellar age to distinguish photoevaporation effects.
- [2022AN....34310077K] This study explores how the diversity of stellar rotation and XUV histories affects atmospheric mass loss predictions and the resulting exoplanet population, directly engaging with the impact of XUV history.
- [2024eas..conf.1699M] This work presents time-dependent photoevaporation modeling of exoplanets, explicitly considering the evolution of stellar high-energy irradiation and its impact on atmospheric mass loss.
- [2022csss.confE.160M] This abstract describes case studies of exoplanets irradiated by young stars, focusing on the effects of evolving XUV emission on atmospheric escape.
- [2024AAS...24321904F] This summary discusses the importance of reconstructing XUV emission histories for interpreting exoplanet atmospheric evolution and habitability.

### rank 102 — q_102: partially_addressed (premise: supported)

**What are the dominant sources of uncertainty and potential systematic biases in atmospheric retrievals from Spitzer/IRAC transit lightcurves, and how do Gaussian process models alter previous inferences of atmospheric composition and thermal structure (e.g., water absorption, temperature inversions) for benchmark exoplanets like HD209458b?**

- rationale: Recent literature has made substantial progress in identifying and quantifying sources of uncertainty and systematic bias in atmospheric retrievals from Spitzer/IRAC transit lightcurves, particularly for HD 209458b, by applying ensemble modeling and explicitly accounting for model uncertainty (e.g., clouds, hazes). While Gaussian process models have been shown to reduce bias and better capture uncertainties in retrievals, their direct application to Spitzer/HD 209458b is not fully demonstrated, leaving some aspects of the original question open.
- [2024ApJ...966..156N] Directly analyzes the HST+Spitzer transmission spectrum of HD 209458b, showing that accounting for model uncertainty (e.g., clouds/hazes) increases the reported uncertainties in retrieved atmospheric parameters, thus addressing systematic biases in retrievals.
- [2024AAS...24341506N] Demonstrates ensemble methods for model uncertainty on HD 209458b's HST+Spitzer spectrum, finding that previous retrievals likely underestimated uncertainties due to unaccounted model assumptions.
- [2024ESS.....562704N] Presents a case study on HD 209458b, resolving discrepancies in water abundance retrievals by incorporating model uncertainty, highlighting the impact of systematic biases.
- [2025ApJ...989..201R] Introduces Gaussian process-aided retrievals, showing that GPs reduce bias and broaden uncertainty in atmospheric parameters, though applied to JWST and WASP-96b rather than Spitzer/HD 209458b.
- [2021EPSC...15....5P] Discusses geometric and modeling biases in transmission spectra retrievals for hot Jupiters, emphasizing the limitations of 1D models and the need for more realistic 3D approaches.

### rank 103 — q_103: partially_addressed (premise: still_plausible)

**To what extent do non-hydrostatic density profiles (e.g., due to atmospheric escape or exogenic sources) in close-in gas giant exoplanets affect the observed sodium and potassium doublet transit spectra, and can current high-resolution observations distinguish between hydrostatic and non-hydrostatic atmospheric models?**

- rationale: Post-cutoff literature has made substantial progress in modeling and interpreting non-hydrostatic and exogenic contributions to sodium and potassium transit spectra, including time-dependent and spatially complex atmospheric structures. However, while these works demonstrate that such effects are relevant and can be modeled, and some use model comparison to test atmospheric architectures, the literature has not yet fully resolved the extent to which current high-resolution observations can unambiguously distinguish hydrostatic from non-hydrostatic models in a general sense.
- [2021EPSC...15..726L] This abstract discusses fitting models of increasing atmospheric complexity, including non-hydrostatic features, to high-resolution sodium transmission spectra and using model comparison to select the best explanation for observed data.
- [2022BAAS...54e2802O] This work models time-dependent, non-hydrostatic sodium and potassium clouds in exoplanet exospheres, comparing transient and sustained alkali absorption features to test interpretations involving exogenic sources.
- [2022FrASS...901873S] This abstract considers the effects of radiation pressure and exospheric processes on alkali line absorption, including the possibility of non-hydrostatic, exogenic sources affecting observed Doppler shifts in potassium lines.
- [2021AJ....162..132M] This study presents high-resolution sodium transit spectra but focuses on detection and line contrast, without explicit modeling of non-hydrostatic versus hydrostatic profiles.

### rank 104 — q_104: answered (premise: supported)

**How do disequilibrium chemical processes, such as quenching, alter the transmission and emission spectra of exoplanet atmospheres compared to equilibrium models, and under what atmospheric conditions is it necessary to include disequilibrium chemistry in retrievals?**

- rationale: Multiple post-cutoff studies directly address how disequilibrium chemistry (including quenching and photochemistry) alters exoplanet spectra and retrieval outcomes, and systematically identify the temperature and planetary regimes where its inclusion is necessary. These works confirm that disequilibrium processes can significantly affect spectral interpretation and atmospheric parameter inference, especially for planets in the 1200-1800 K range, thus substantially resolving the original question and supporting its premise.
- [2021AJ....162...37R] This study analyzes 62 HST exoplanet spectra and finds that disequilibrium chemistry is preferred in about half the atmospheres, especially in the 1200-1800 K range, and equilibrium is favored above 1800 K, directly addressing when disequilibrium chemistry must be included in retrievals.
- [2021A&A...656A..90K] This work implements disequilibrium chemistry in retrievals and finds significant spectral differences (e.g., NH3 features) for specific planets, showing that neglecting disequilibrium can misinterpret key atmospheric parameters.
- [2025A&A...699A.342B] This re-analysis of ten hot Jupiters with disequilibrium chemistry retrievals demonstrates that including disequilibrium processes significantly alters retrieved metallicity and C/O ratios compared to equilibrium models.
- [2025epsc.conf.1042P] This study explores the detectability and impact of disequilibrium chemistry on retrievals for five exoplanets, showing that such processes can significantly affect observed spectra and inferred atmospheric properties.
- [2025A&A...699A.306A] This modeling work finds that disequilibrium chemistry can alter atmospheric composition and temperature structure, but for irradiated gas giants, temperature corrections are modest, further refining the conditions under which disequilibrium must be considered.

### rank 105 — q_105: partially_addressed (premise: supported)

**What are the physical mechanisms responsible for the observed diversity in heat redistribution efficiency among hot Jupiters, given that recent phase curve observations show inconsistencies with theoretical predictions of a temperature-correlation?**

- rationale: Post-cutoff literature has made substantial progress in identifying and modeling physical mechanisms—such as cloud properties, atmospheric composition, nonlinear flow regimes, and planetary parameters—that contribute to the diversity in heat redistribution among hot Jupiters. However, while these studies support the premise and provide new mechanistic insights, they also acknowledge that the diversity is not yet fully explained and that current models cannot account for all observed trends, leaving the core question open.
- [2021MNRAS.501...78P] This study uses advanced GCMs with realistic opacities and clouds to show that nightside clouds and their properties can explain the diversity in phase curves and heat redistribution, directly addressing physical mechanisms behind observed diversity.
- [2024MNRAS.531.1056R] A large grid of GCMs demonstrates that planetary parameters and the presence of TiO/VO lead to diverse heat transport efficiencies, and that phase curve amplitude and hotspot offset are not necessarily correlated, supporting the premise and providing mechanistic insight.
- [2025ApJ...995...84D] Anelastic models reveal that nonlinear flow regimes, pressure, and the interplay of advective and radiative processes drive diversity in heat redistribution and phase curve properties, offering new physical explanations.
- [2024MNRAS.528.1016T] Non-grey GCMs show that intrinsic planetary properties and rotation rates contribute to the observed scatter in heat redistribution, but models still struggle to match all observations, indicating incomplete resolution.
- [2025AJ....169...32D] A comprehensive analysis of Spitzer phase curves confirms the diversity in heat redistribution and highlights that current models and data are insufficient to fully confirm dynamical theories, keeping the core question open.

### rank 106 — q_106: partially_addressed (premise: supported)

**How do clouds and hazes in super-Earth and sub-Neptune atmospheres, particularly those with high metallicity or photochemical hazes, affect the detectability of molecular features in transmission, emission, and reflected light spectra, and can reflected light observations robustly distinguish between cloudy and hazy atmospheres?**

- rationale: Post-cutoff literature robustly supports the premise that clouds and hazes in super-Earth and sub-Neptune atmospheres, especially those with high metallicity or photochemical hazes, strongly attenuate or flatten molecular features in transmission and emission spectra. There is substantial progress on how these aerosols affect detectability and some work (e.g., phase curve and secondary eclipse combinations) on distinguishing hazy from clear atmospheres, but the ability of reflected light observations alone to robustly distinguish between cloudy and hazy atmospheres remains incompletely resolved.
- [2024ApJ...961L..23B] This study finds that clouds and hazes, especially in high-metallicity Neptune-size exoplanets, significantly attenuate molecular features in transmission spectra, supporting the premise that aerosols obscure spectral features.
- [2026ApJ..1002..221P] This work demonstrates that hydrolyzed photochemical hazes in water-rich sub-Neptunes can almost completely flatten spectral features, confirming the strong impact of hazes on detectability in transmission and emission spectra.
- [2025ApJ...985...98S] This paper shows that photochemical hazes affect phase curves and emission spectra, and suggests that combining phase-curve and secondary eclipse observations can help distinguish between hazy and clear atmospheres.
- [2022eas..conf..512D] This study uses high-resolution spectroscopy to detect molecular species above cloud decks, directly addressing the challenge of molecular detectability in cloudy/hazy atmospheres.

### rank 107 — q_107: not_addressed (premise: still_plausible)

**What are the limitations of the massless planet approximation in transit light curve models, and in which parameter regimes does this approximation introduce significant errors in the inferred planetary and stellar parameters?**

- rationale: None of the provided post-cutoff abstracts substantively engage with the limitations of the massless planet approximation in transit light curve models or identify parameter regimes where it introduces significant errors. The literature addresses other sources of bias and systematic error in transit modeling, but not the specific question of the massless planet assumption.

### rank 108 — q_108: partially_addressed (premise: supported)

**How does the presence and structure of clouds (e.g., number of layers, particle size, composition) in directly imaged exoplanet atmospheres affect the retrieval of methane abundance and other atmospheric properties from reflected light spectra?**

- rationale: Multiple post-cutoff studies directly address how cloud structure, particle size, and composition affect the retrieval of atmospheric properties (including molecular abundances) from reflected light spectra, using both simulations and Earth as an exoplanet analog. However, while these works demonstrate the importance and quantify some effects, they do not fully resolve all aspects of the question, such as providing a universal solution for robust methane retrievals across all cloud scenarios, leaving the core challenge open.
- [2021ApJ...910..158M] Directly investigates how different cloud parameterizations (structure, complexity) affect retrievals of atmospheric composition, including molecular abundances, from reflected light spectra.
- [2021ApJ...907...30S] Demonstrates that inaccurate representation of cloud particle size and scattering properties leads to significant errors in retrievals of atmospheric parameters from reflected light and polarimetric data.
- [2025PSJ.....6...87K] Quantifies the impact of cloud variability (coverage, vertical position) on the detectability of atmospheric constituents in direct imaging spectra.
- [2023AGUFM.P21B3006G] Develops and tests retrieval algorithms for multi-layer cloud structures using reflected sunlight spectra, showing sensitivity to cloud structure and optical depth.

### rank 109 — q_109: partially_addressed (premise: supported)

**Can the forward-scattering of starlight by large haze particles in extended exoplanet atmospheres be robustly detected in optical phase curves, and how should current phase curve interpretations be revised to account for this effect?**

- rationale: Post-cutoff literature has made substantial progress in modeling and measuring the forward-scattering of starlight by haze particles in exoplanet atmospheres, including the development of models that can robustly simulate phase curves for arbitrary particle sizes and laboratory measurements of relevant phase functions. However, robust detection of forward-scattering by large haze particles in actual exoplanet phase curve data and a systematic revision of phase curve interpretations to account for this effect remain open, as most observational inferences still favor smaller particle sizes and do not yet demonstrate unambiguous detection of strong forward-scattering signatures.
- [2024AAS...24317801C] This work presents a model capable of calculating phase curves for arbitrary scattering functions, including Mie scattering by haze and cloud particles, and discusses potential observables for various atmospheric compositions.
- [2024A&A...685A.104M] This study uses optical phase curves to infer scattering properties and particle sizes in exoplanet atmospheres, but finds best-fit particle radii in the sub-micron range (0.01-0.1 µm), smaller than the 'large' haze particles relevant for strong forward-scattering.
- [2021DPS....5330503H] This abstract describes laboratory measurements of phase curves for micron-sized haze particles, directly probing their forward-scattering properties relevant to exoplanet atmospheres.

### rank 110 — q_110: partially_addressed (premise: supported)

**What are the key sources of spectral line broadening in exoplanetary atmospheres with haze, and how do interactions between radiators and haze particles modify the absorption and emission spectral shapes compared to clear atmospheres?**

- rationale: Post-cutoff literature has made substantial progress in identifying and modeling the contributions of haze particles to spectral line broadening, including scattering, absorption, and collisional effects, and has begun to quantify their impact on observed spectra. However, while these studies advance understanding and modeling, they do not fully resolve the detailed mechanisms by which haze-radiator interactions modify absorption and emission line shapes compared to clear atmospheres, leaving the core question open.
- [2023APS..DMPN01013V] This abstract discusses the relative contributions of scattering, absorption, and collisional broadening by haze particles to spectral line shaping in exoplanetary atmospheres.
- [2026arXiv260619056L] This work models the formation, distribution, and radiative feedback of haze particles, showing their impact on transmission spectra and temperature-pressure structures.

### rank 111 — q_111: partially_addressed (premise: supported)

**How do the physical and chemical properties of brown dwarf atmospheres, as revealed by large statistical studies, inform our understanding and modeling of exoplanet atmospheres at the boundary between stars and planets?**

- rationale: Multiple post-cutoff studies have conducted large statistical and systematic analyses of brown dwarf atmospheres, directly comparing them to exoplanets and using the results to inform and refine atmospheric models at the boundary between stars and planets. These works have made substantial progress in identifying population-level trends, model shortcomings, and compositional diagnostics, but the core challenge of fully resolving the complexities of exoplanet atmosphere modeling using brown dwarf analogs remains open.
- [2023nsbp.confE..68B] This study uses a large dataset of brown dwarfs and giant planets to analyze population-level trends in cloud formation and evolution, directly addressing how brown dwarf atmospheric properties inform exoplanet modeling.
- [2021csss.confE..99Z] This work conducts a systematic, large-sample spectroscopic analysis of brown dwarfs to identify trends and model shortcomings, with implications for ultracool atmosphere modeling relevant to exoplanets.
- [2021EPSC...15..818Z] This abstract describes a systematic analysis of spectra from both brown dwarfs and directly imaged exoplanets, aiming to improve model predictions and understand atmospheric properties at the star-planet boundary.
- [2026ASTCS..1110201F] This talk discusses how brown dwarf atmospheric discoveries, especially from JWST, are redefining our understanding of the diversity and overlap between brown dwarf and exoplanet atmospheres.
- [2025AAS...24531905P] This work presents retrieval analyses of brown dwarfs and planetary-mass analogs, exploring fundamental atmospheric properties and their implications for formation and modeling at the star-planet boundary.

### rank 112 — q_112: answered (premise: supported)

**What are the effects of stellar flares, particularly those with hot FUV continuum temperatures, on the photochemistry and atmospheric escape rates of exoplanets orbiting active M dwarfs?**

- rationale: Multiple post-cutoff studies directly model and quantify the effects of M-dwarf stellar flares—including those with strong FUV and XUV emission—on both the photochemistry and atmospheric escape rates of exoplanets. These works demonstrate that flares can significantly alter atmospheric composition and increase escape rates, thus substantially resolving the question and supporting its premise.
- [2022A&A...667A..15K] Directly models the impact of M dwarf stellar flares on exoplanet atmospheric photochemistry, showing significant changes in molecular abundances and transmission spectra.
- [2022ApJ...928...12D] Quantifies the contribution of M-dwarf flares to atmospheric escape rates of Earth-like exoplanets, finding that flares can substantially increase water and atmospheric loss.
- [2025A&A...702A.112C] Assesses the cumulative impact of M-dwarf flares on atmospheric evaporation, finding the effect is modest but quantifiable for sub-Neptunes and Earth-sized planets.
- [2023MNRAS.518.2472R] Uses 3D modeling to show that stellar flares alter atmospheric composition and UV shielding on terrestrial exoplanets orbiting M dwarfs.

### rank 113 — q_113: partially_addressed (premise: supported)

**How does the obliquity of tidally locked exoplanets around M dwarfs affect their climate, cloud cover, and the boundaries of the habitable zone, and what are the key differences in warming mechanisms compared to planets around Sun-like stars?**

- rationale: Post-cutoff literature has made substantial progress in modeling the effects of obliquity, atmospheric circulation, and cloud cover on the climate and habitability of tidally locked exoplanets around M dwarfs. However, while key mechanisms and climate impacts have been elucidated, a comprehensive resolution of how obliquity specifically shifts habitable zone boundaries and the full set of differences in warming mechanisms compared to Sun-like stars remains open.
- [2026NewA..12302483W] This study directly investigates the effect of obliquity on the climate and cloud cover of water-covered exoplanets, finding that obliquity induces hemispheric climate and cloud asymmetries relevant to habitability.
- [2026ApJ..1001...50C] This work explores climate mechanisms on tidally locked rocky planets around M dwarfs, focusing on atmospheric circulation, cloud feedbacks, and warming mechanisms, though it emphasizes topography rather than obliquity.
- [2026absc.conf18074K] This abstract discusses cloud cover and climate variability on tidally locked rocky exoplanets around M dwarfs, including the impact of atmospheric circulation and cloud feedbacks on habitability.

### rank 114 — q_114: partially_addressed (premise: supported)

**What are the dominant drivers of atmospheric escape in close-in exoplanets, and how do the relative contributions of stellar XUV/EUV flux and stellar wind-magnetosphere interactions scale with planetary and stellar properties?**

- rationale: The post-cutoff literature directly engages the question by reviewing and modeling the roles of stellar XUV/EUV flux and stellar wind-magnetosphere interactions in driving atmospheric escape, and by quantifying how these processes scale with planetary and stellar properties. However, while substantial progress is made in identifying and modeling the key drivers and their dependencies, the literature indicates that the core question of the relative contributions and their scaling remains open, with several aspects still under investigation.
- [2025RvMPP...9...18H] This review discusses both stellar XUV/EUV flux and stellar wind/magnetosphere interactions as major drivers of atmospheric escape, and how their effects depend on planetary and stellar properties.
- [2023ApJ...951..136L] This study quantifies the influence of stellar wind parameters and planetary properties on nonthermal ion escape, showing the importance of stellar wind-magnetosphere interactions.
- [2023IAUS..370..155M] This work classifies hydrodynamic escape regimes in close-in planets, focusing on EUV-driven escape and the conditions under which it dominates.
- [2024EPSC...17..198M] This abstract provides analytic formulae for EUV-driven escape and discusses how planetary and stellar parameters affect mass-loss rates.
- [2024EGUGA..26.2004D] This abstract reviews ion escape processes, including the role of magnetospheric energization, but notes that several questions remain open regarding the relative contributions of different drivers.

### rank 115 — q_115: not_addressed (premise: still_plausible)

**How can the detection of the 6.4 μm O2-X collision-induced absorption feature in exoplanet transmission spectra be optimized, and under what atmospheric and observational conditions is this the most detectable O2 signature for JWST and future missions?**

- rationale: None of the provided abstracts directly address the detectability or optimization of the 6.4 μm O2-X collision-induced absorption feature in exoplanet transmission spectra. The premise that this feature could be a detectable O2 signature remains plausible, but has not been directly tested or discussed in the post-cutoff literature provided.

### rank 116 — q_116: partially_addressed (premise: supported)

**What are the effects of cosmic ray-induced ionization, including secondary particle cascades, on the chemistry and ionization structure of thick planetary atmospheres, and how do these processes influence atmospheric evolution and habitability?**

- rationale: Multiple recent studies directly model the effects of cosmic ray and high-energy particle-induced ionization, including secondary cascades, on the chemistry and ionization structure of thick planetary atmospheres. These works quantify ionization rates, demonstrate significant chemical impacts, and motivate further research into atmospheric evolution and habitability, but do not yet fully resolve the long-term evolutionary or habitability consequences, leaving the core question open.
- [2024arXiv240907274R] Directly models cosmic ray and stellar energetic particle-induced ionization in thick, hydrogen-dominated exoplanet atmospheres, quantifying ionization rates and motivating further chemical modeling.
- [2026IAUS..388..243R] Repeats and extends the above study, again focusing on energetic particle transport and ionization in thick exoplanet atmospheres, with implications for chemistry and habitability.
- [2024eas..conf.1577H] Reviews how high-energy particles, including cosmic rays, drive complex chemistry in exoplanet atmospheres, affecting molecular formation and potentially cloud formation.
- [2024arXiv240204688L] Models X-ray and secondary electron cascade-driven chemistry in giant planet atmospheres, showing out-of-equilibrium molecular signatures due to high-energy ionization.
- [2024PSJ.....5...58L] Parallel to the above, demonstrates that secondary electron cascades from high-energy radiation alter the chemical and ionization structure of thick planetary atmospheres.

### rank 117 — q_117: partially_addressed (premise: supported)

**How do giant impacts after gas disk dissipation contribute to the observed diversity in bulk densities and atmospheric gas fractions of super-Earths, and can this mechanism explain the properties of tightly-packed multi-planet systems?**

- rationale: Post-cutoff literature has made substantial progress in modeling how giant impacts after gas disk dissipation can erode planetary atmospheres and alter system architectures, directly addressing the mechanisms behind the observed diversity in super-Earth densities and atmospheric fractions. However, while these studies provide strong constraints and demonstrate the plausibility of giant impacts as a key factor, they do not fully resolve whether this mechanism alone can explain all properties of tightly-packed multi-planet systems, leaving the core question partially open.
- [2023ApJ...954..196K] Directly simulates giant impacts on super-Earths and quantifies atmospheric loss, supporting the idea that such impacts contribute to the diversity in atmospheric gas fractions and bulk densities.
- [2023AJ....165..174W] Explores the dynamical evolution of tightly-packed multi-planet systems subject to atmospheric mass loss from giant impacts, showing that such events can destabilize compact systems and affect their architecture.
- [2024ESS.....560803W] Models the formation and evolution of multiple planetary systems with atmospheric mass loss, including the effects of giant impacts, and discusses implications for observed system architectures and atmospheric retention.

### rank 118 — q_118: partially_addressed (premise: supported)

**What are the key limitations and degeneracies in current atmospheric retrieval models (e.g., BART, PLATON), especially regarding clouds, 3D effects, and disequilibrium chemistry, and how can these be addressed with upcoming JWST data?**

- rationale: The post-cutoff literature makes substantial progress in identifying and characterizing the key limitations and degeneracies in atmospheric retrieval models, especially regarding clouds, 3D effects, and model assumptions, and discusses how JWST data can help address these issues. However, while new frameworks and parameterizations are proposed and some are applied to early JWST data, the core challenges—such as fully resolving degeneracies and integrating comprehensive 3D/disequilibrium chemistry—remain open, so the question is only partially addressed and the premise is supported by ongoing research.
- [2026ASTCS..1120201L] This abstract directly discusses the key limitations and degeneracies in current atmospheric retrieval models, including temperature-composition-aerosol degeneracies, model assumptions, and the need for more realistic physics, as well as future directions with JWST data.
- [2025A&A...699A.219C] This work investigates cloud and haze parameterization in retrievals using JWST data, highlighting the need for wide wavelength coverage and improved inversion techniques to address biases and degeneracies.
- [2024jwst.prop.6347N] This proposal aims to improve retrieval frameworks by integrating 3D models and enhancing computational efficiency, directly addressing the limitations of 1D models and missing physics in current retrievals.
- [2023eas..conf.1604N] This abstract discusses advances in statistical inference for JWST retrievals, including methods to handle model uncertainty and degeneracies, and applies these to early JWST data.
- [2024ESS.....562438A] This study uses JWST/NIRSpec data to explore degeneracies in atmospheric retrievals, emphasizing the impact of model assumptions and the need for robust frameworks.

### rank 119 — q_119: partially_addressed (premise: supported)

**How can rotational mapping and specular reflection (glint) techniques be combined and optimized to robustly detect and spatially map oceans on terrestrial exoplanets, while minimizing false positives from non-ocean surfaces?**

- rationale: Recent literature has made substantial progress in modeling and simulating the combined use of rotational mapping and specular reflection (glint) techniques for detecting and mapping oceans on terrestrial exoplanets, with particular attention to the confounding effects of clouds and atmospheric scattering. However, while these studies have advanced our understanding and proposed strategies to minimize false positives, a fully robust, optimized method for spatially mapping oceans that is validated on exoplanet data remains an open challenge.
- [2022A&A...664A.172T] This study explores ocean signatures in both flux and polarization spectra, identifying glint-related features that distinguish oceans from dry surfaces and suggesting observational strategies to minimize false positives.
- [2026absc.conf50202R] This work quantifies contributions from ocean glint and investigates how cloud scattering can yield false positives, directly addressing the challenge of robust ocean detection.
- [2025A&A...697A.170R] This paper presents advanced simulations of Earth-like exoplanets, showing how phase-dependent reflectance and polarization (including glint) are affected by realistic surface and cloud properties, and discusses the impact of clouds on glint detection.
- [2026absc.conf16026C] This abstract analyzes Earth's phase curves to distinguish glint from other scattering effects, focusing on the challenge of disambiguating ocean signals from atmospheric phenomena.

### rank 120 — q_120: partially_addressed (premise: supported)

**How do the atmospheric properties (e.g., metallicity, methane abundance, cloud composition) of sub-Neptune exoplanets with low metallicity and methane depletion challenge current models of planet formation and atmospheric evolution?**

- rationale: Recent literature has made substantial progress in modeling and observing the atmospheric properties (metallicity, methane abundance, cloud composition) of sub-Neptunes, including the effects of atmospheric escape, interior-atmosphere coupling, and disequilibrium chemistry. However, while these studies highlight and begin to address the challenges such properties pose to current formation and evolution models, they do not fully resolve how these observations can be reconciled with or require revisions to those models, leaving the core question open but significantly advanced.
- [2025ApJ...991..121L] This study models how atmospheric escape can lead to metal-enriched, methane-depleted atmospheres in sub-Neptunes, directly addressing how such properties arise and their implications for interpreting formation models.
- [2024ESS.....510306B] This work presents new molecular detections (including methane depletion and disequilibrium chemistry) in sub-Neptune atmospheres, highlighting challenges for current models and the need for multi-molecule constraints.
- [2026ApJ..1001...36S] This paper develops coupled thermal-chemical evolution models for sub-Neptunes, showing how formation location and interior-atmosphere interactions affect atmospheric metallicity and methane abundance.
- [2022BAAS...54e.160G] This abstract discusses the chemical diversity of sub-Neptune atmospheres, noting that high-metallicity, methane-depleted models can be inconsistent with plausible interiors, thus challenging current models.

### rank 121 — q_121: partially_addressed (premise: supported)

**What are the technical and scientific trade-offs in extending the wavelength coverage of large space telescopes (e.g., ATLAST/LUVOIR) to 5 μm or beyond for exoplanet atmosphere studies, and how does this impact the detection of key molecular features?**

- rationale: Post-cutoff literature directly addresses the scientific trade-offs of extending wavelength coverage to 5 μm for exoplanet atmosphere studies, demonstrating that such extension significantly improves molecular abundance constraints. However, while technical trade-offs are discussed (e.g., resolution vs. bandwidth), a comprehensive analysis of all technical and scientific trade-offs for large space telescopes specifically (e.g., ATLAST/LUVOIR) is not fully resolved, leaving some aspects of the core question open.
- [2021MsT..........2C] Directly compares exoplanet atmospheric retrievals for 0.5-2.5 μm vs 0.5-5 μm coverage, showing that extending to 5 μm greatly improves constraints on key molecular abundances.
- [2021MsT..........6B] Duplicates the findings of 2021MsT..........2C, reinforcing that 2.5-5 μm coverage significantly tightens abundance constraints for major molecules in exoplanet atmospheres.
- [2023A&A...675A.157L] Analyzes trade-offs between spectral resolution and wavelength coverage for exoplanet atmosphere characterization, finding that maximizing bandwidth after a certain resolution is optimal for molecule detection.

### rank 122 — q_122: answered (premise: supported)

**How can empirical high-resolution spectra of Solar System bodies be used as analogs to constrain and validate models of exoplanet atmospheres, and what are the limitations of such analogies?**

- rationale: Multiple post-cutoff works directly engage the question by applying high-resolution Solar System spectra to validate and constrain exoplanet atmospheric models, and explicitly discuss both the strengths and limitations of such analogies. The premise that Solar System spectra can be used as analogs for exoplanet model validation is supported by these studies, which demonstrate practical applications and identify specific challenges and caveats.
- [2023PSJ.....4...10R] This work directly applies atmospheric retrieval tools to high-resolution spectra of Solar System bodies as analogs for exoplanet atmospheres, demonstrating both the utility and limitations of such analogies for model validation.
- [2022LPICo2687.3009R] This abstract describes the use of Solar System analog observations to validate exoplanet atmospheric retrieval tools, specifically applying inverse models to spacecraft data for Earth and Titan.
- [2026absc.conf16059R] This work uses Solar System aerosol profiles as ground truth to validate and improve aerosol parameterizations in exoplanet atmospheric retrieval models, directly addressing the question's core.
- [2022RAA....22l2001E] This paper discusses lessons learned from planetary spectroscopy in the Solar System for exoplanetary atmospheres, including the use of synthetic spectra and the limitations of analogy.
- [2026ASTCS..1120201L] This talk addresses the limitations and challenges of atmospheric retrievals, including the difficulty of validation and the use of benchmark atmospheres, which relates to the limitations of using Solar System analogs.

### rank 123 — q_123: partially_addressed (premise: supported)

**What are the effects of planetary magnetic fields and stellar CME activity on atmospheric erosion and habitability in the habitable zones of Sun-like and M-dwarf stars, and how can planetary magnetic field strengths be constrained observationally?**

- rationale: Recent literature has made substantial progress in modeling and quantifying the effects of stellar and planetary magnetic fields, as well as CME activity, on atmospheric erosion and habitability, and has begun to address observational constraints on planetary magnetic fields (e.g., via radio emission). However, while analytic relations and simulation results have advanced understanding, the core question—especially regarding robust observational constraints on exoplanetary magnetic field strengths—remains open and is an active area of research.
- [2023ApJ...953...70G] This study uses 3D MHD simulations to quantify how stellar and planetary magnetic field strengths affect atmospheric erosion, providing analytic relations and demonstrating the importance of magnetic field interplay for habitability.
- [2024cosp...45.1064V] This work models the protection of exoplanet atmospheres by planetary magnetic fields under various stellar space weather conditions and discusses the potential of radio emission as an observational constraint on magnetic field strength.
- [2024AAS...24321903P] This review discusses recent advances in observational and theoretical characterization of stellar magnetospheric environments and their impact on exoplanetary atmospheres and habitability.

### rank 124 — q_124: partially_addressed (premise: supported)

**How do the properties of expanded ionospheres in hot Jupiters affect the generation and escape of radio emission via the cyclotron maser instability, and what are the implications for radio detection of exoplanets at different orbital distances?**

- rationale: The post-cutoff literature (2022MNRAS.512.4869E) directly examines how the properties of expanded ionospheres in hot Jupiters affect the generation and escape of radio emission via the cyclotron maser instability, finding that atmospheric compactness (linked to mass and thus ionospheric extent) is crucial for CMI operation and radio escape. However, while this work makes substantial progress by linking atmospheric properties to radio detectability and proposing a method to constrain planetary mass, it does not fully resolve the broader implications for radio detection across a range of orbital distances or provide a comprehensive answer for all hot Jupiters, leaving the core question open.
- [2022MNRAS.512.4869E] Directly investigates whether cyclotron maser instability (CMI) radio emission can be generated and escape from hot Jupiter atmospheres, focusing on the impact of atmospheric extension and plasma conditions.

### rank 125 — q_125: partially_addressed (premise: supported)

**How can the atmospheric characterization of cold, long-period Jupiter analogs (e.g., Kepler-167e) be achieved with current and upcoming facilities, and what unique challenges and opportunities do such targets present compared to hot Jupiters?**

- rationale: Recent literature has made substantial progress in modeling and observing the atmospheres of cold, long-period Jupiter analogs using JWST and advanced ground-based facilities, directly addressing the technical challenges and opportunities for such targets. However, while these works advance the field and demonstrate new capabilities, they do not yet fully resolve all unique challenges (e.g., signal-to-noise, cloud modeling, direct detection limits), leaving the core question open but significantly advanced.
- [2023xrp..prop...81M] This abstract discusses new theoretical approaches and the use of JWST to characterize cool gas giants, specifically addressing the challenges of modeling their atmospheres and leveraging analogs like Y dwarfs.
- [2026ASTCS..1120101M] This work highlights JWST's ability to observe cold, Jupiter-like exoplanets and details modeling efforts to interpret these observations, directly engaging with the atmospheric characterization of cold, long-period Jupiter analogs.
- [2024ESS.....562603Z] This abstract demonstrates the use of high-resolution ground-based spectroscopy to characterize the atmospheres of faint, directly imaged super-Jupiters, showcasing current capabilities relevant to cold Jupiter analogs.
