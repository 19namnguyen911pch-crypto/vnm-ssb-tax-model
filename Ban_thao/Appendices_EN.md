## Appendix A. Evidence search

**A.1 Questions the search was designed to answer**

Three, in order of importance. (i) Has anyone modelled the SSB tax that Viet Nam actually legislated, or its distributional consequences? (ii) What are the best available parameter values for the price, demand, energy, and risk steps of the model, for Viet Nam or for comparable settings? (iii) What does the legal instrument itself say? The third question is answered from primary legal sources and is logged separately in A.7, because a tax model built on a secondary description of the law is built on the wrong base.

**A.2 Sources**

| Source | Coverage | Purpose |
|---|---|---|
| PubMed/MEDLINE | Biomedical and public health | Studies of health impact, epidemiology, risk |
| Europe PMC | Biomedical and life sciences, including preprints | Catches records not indexed in MEDLINE |
| OpenAlex | Multidisciplinary, including economics and policy | Captures social-science literature on taxation |
| Scopus | Multidisciplinary | Economics and policy journals not indexed in MEDLINE |
| Cochrane Library (CDSR and CENTRAL) | Systematic reviews and trials | Reviews of SSB interventions; trial evidence on price and consumption |
| RePEc/IDEAS | Economics working papers and journals | Pass-through, incidence and tax design |
| Citation chasing, forward and backward | Studies citing, or cited by, each included record | Recovers literature missed by keyword searching |
| Google Scholar | Grey and non-indexed | Vietnamese-language scholarship |
| WHO IRIS | Global health policy | WHO tax reports and technical documents |
| World Bank, IMF, ADB | Development economics | Tax design and revenue documents |
| Ministry of Finance (mof.gov.vn), Ministry of Health, HSPI, NIN, GSO | Vietnamese official | Legal text, budget projections, survey documentation |
| Thuvienphapluat, vanban.chinhphu.vn, Cong bao | Vietnamese legal | Primary legal text |
| Euromonitor Passport | Commercial market data | Volume and value of the beverage market |
| GHAI, Vital Strategies, HealthBridge, UNICEF, WHO Viet Nam | Advocacy and programme | Grey literature on the Vietnamese policy process |

**A.3 Search strings**

The strings are reported in full so that the search can be re-run. Each was executed with the database's own syntax; MeSH terms were used in PubMed only.

*PubMed, Viet Nam set (returned 2 records):*

```
("sugar-sweetened beverage"[tiab] OR "sugar sweetened beverage"[tiab]
 OR "sugary drink"[tiab] OR "sugary drinks"[tiab] OR "soft drink"[tiab]
 OR "soft drinks"[tiab] OR "carbonated beverage"[tiab]
 OR "carbonated beverages"[tiab] OR "sugary beverage"[tiab]
 OR "SSB"[tiab] OR "SSBs"[tiab] OR "soda tax"[tiab])
AND
("tax"[tiab] OR "taxes"[tiab] OR "taxed"[tiab] OR "taxing"[tiab]
 OR "taxation"[tiab] OR "excise"[tiab] OR "fiscal policy"[tiab]
 OR "price elasticity"[tiab] OR "pass-through"[tiab])
AND
("Viet Nam"[tiab] OR Vietnam[tiab] OR "Vietnam"[MeSH Terms])
```

*PubMed, broad SSB–tax set without a country limit, used to size the field and to source parameters from comparable settings (returned 576 records):*

```
("sugar-sweetened beverage"[tiab] OR "sugary drink"[tiab]
 OR "soft drink"[tiab] OR "soda"[tiab])
AND
("tax"[tiab] OR "taxes"[tiab] OR "taxation"[tiab] OR "excise"[tiab])
```

*Europe PMC* (title and abstract fields; broad set returned 506 records, Viet Nam set 3):

```
(TITLE_ABS:"sugar-sweetened beverage" OR TITLE_ABS:"sugar sweetened beverage"
 OR TITLE_ABS:"sugary drink" OR TITLE_ABS:"soft drink"
 OR TITLE_ABS:"carbonated beverage" OR TITLE_ABS:soda)
AND
(TITLE_ABS:tax OR TITLE_ABS:taxation OR TITLE_ABS:excise OR TITLE_ABS:"fiscal policy")
[AND (TITLE_ABS:vietnam OR TITLE_ABS:"viet nam")]
```

*OpenAlex* (title and abstract; broad set returned 2961 records, Viet Nam set 11):

```
filter=title_and_abstract.search:("sugar-sweetened beverage" OR "soft drink" OR soda)
   AND (tax OR taxation OR excise)
   [AND (vietnam OR "viet nam")]
```

Set #4 is run without the country limit because the review and trial literature on SSB taxes is thin and almost entirely non-Vietnamese; #5 isolates the Vietnamese subset.

*Citation chasing.* The reference list of every included study was screened by hand, and the "cited by" function of Google Scholar was used for the two Vietnamese analyses and for each systematic review included.

*Scopus* (title, abstract and keywords; Viet Nam set returned 6 records):

```
TITLE-ABS-KEY(("sugar-sweetened beverage" OR "sugar sweetened beverage"
 OR "sugary drink" OR "soft drink" OR "carbonated beverage" OR "soda")
 AND (tax OR taxation OR excise OR "fiscal policy"))
AND TITLE-ABS-KEY("Viet Nam" OR Vietnam)
```

*Scopus, broad set without a country limit:* the same first two blocks, run without the country line.

*Cochrane Library* (CDSR and CENTRAL; line-numbered sets):

```
#1 ("sugar-sweetened beverage" OR "sugar sweetened beverage" OR "sugary drink"
    OR "soft drink" OR "carbonated beverage" OR soda):ti,ab,kw
#2 (tax OR taxes OR taxation OR excise OR "fiscal policy" OR "price elasticity"):ti,ab,kw
#3 (vietnam OR "viet nam"):ti,ab,kw
#4 #1 AND #2
#5 #4 AND #3
```

*RePEc/IDEAS* (EconPapers advanced search, title and abstract), supplemented by
`site:ideas.repec.org OR site:econpapers.repec.org ("sugar-sweetened beverage" OR "soft drink" OR soda) (tax OR taxation OR excise)`:

```
("sugar-sweetened beverage" OR "soft drink" OR soda)
AND (tax OR taxation OR excise)
AND (vietnam OR "viet nam" OR asia OR "developing countr*")
```

*Vietnamese-language sources* (Google Scholar and vjol.info, strings unquoted):

```
thuế tiêu thụ đặc biệt nước giải khát; thuế đồ uống có đường;
độ co giãn giá đồ uống; gánh nặng đái tháo đường Việt Nam
```

*Legal sources:* searched by instrument number once identified, and by keyword `nước giải khát`, `hàm lượng đường`, `thuế tiêu thụ đặc biệt` on `vanban.chinhphu.vn` and `thuvienphapluat.vn`.

**A.4 Eligibility**

*Included:* modelling studies, natural experiments, and evaluations of SSB taxes reporting price, purchase, consumption, weight, disease, cost, revenue, or distributional outcomes; systematic reviews and meta-analyses of elasticities or effectiveness; cost-of-illness and cost-of-care studies for the three modelled diseases in Viet Nam or comparable settings; qualitative studies of patient experience used for interpretation; and primary legal and budgetary documents.

*Excluded:* studies of taxes on foods other than beverages, or on nutrients other than sugar, without an SSB-specific estimate; commentaries, editorials, and advocacy material without original data, unless used as grey-literature evidence of the policy process; studies with no extractable outcome; and non-peer-reviewed market reports except Euromonitor, which is used only for volume and value and is identified as commercial data wherever cited.

*Limits:* published 2000 onwards for tax literature, with no date limit for epidemiology, relative risks, or the food composition table; languages English and Vietnamese.

**A.5 Screening procedure**

1. Each database was searched on 1 November 2026 with the strings in A.3 and the results exported in full to a reference manager.
2. Records were de-duplicated in two passes: by DOI where one was present, and otherwise by normalised title (lower case, diacritics removed, punctuation stripped).
3. Titles and abstracts were screened against the eligibility criteria in A.4. Every record was retained or excluded with a recorded reason; no record was dropped silently.
4. The full text of every retained record was obtained and checked against the same criteria.
5. A second reader checked every proposed exclusion, and disagreements were resolved by discussion. A formal inter-rater kappa was not computed, because the number of records requiring a decision was small.
6. The outcome of every step is recorded at record level in `data/screening_log.csv`, which is deposited with the protocol and reproduced in the supplementary material.

**A.6 Flow**

| Stage | PubMed | Europe PMC | OpenAlex | Scopus | Cochrane | RePEc | Total |
|---|---|---|---|---|---|---|---|
| Identified, country-limited set | 2 | 3 | 11 | 6 | 3 | 0 | **25** |
| Removed as duplicates | | | | | | | 11 |
| Unique records screened | | | | | | | **14** |
| Excluded at screening | | | | | | | 6 |
| Included | | | | | | | **8** |

Eight records were included: two quantitative analyses that model SSB taxation in Viet Nam; one distributional analysis of the 2025 design using household survey data; one empirical study of excise effects on beverage consumption; one human-rights assessment of the enacted tax; one study of public acceptability; one regional analysis of the distributional impacts of health taxes; and one Cochrane systematic review of environmental interventions to reduce SSB consumption.

Six were excluded. A 1997 dental review of sugar consumption trends is not about taxation; a historical article on Lyndon Johnson was retrieved by the country term as a false positive; an urban food-systems paper and a study of food marketing to children report no SSB-tax estimate; and a peer-led dietary education trial and a caries prevalence study mention Viet Nam but contain no tax exposure.

The broad sets without a country limit returned 576 records in PubMed, 506 in Europe PMC, 2,961 in OpenAlex, 1,526 in Cochrane CENTRAL and 21 in RePEc. These were used to source parameter values — price elasticities, pass-through, relative risks and cost estimates — rather than screened record by record, because the study needs estimates from any comparable setting rather than a systematic review of tax effects.

Two features of this flow are themselves findings. The yield of the country-limited searches is very small: fourteen unique records for the whole Vietnamese literature on SSB taxation, of which eight are relevant. And the 1997 dental review is retrieved by every database because it names Viet Nam in a list of countries with rising sugar consumption — a reminder that country-term searches in this field are noisy.

**A.7 Verification log for legal and budgetary sources**

Legal claims in a tax model are load-bearing and cannot be cited at second hand. Each instrument was read in full and the specific provision used in the model recorded against it.

| Instrument | Provision used | What it settles | Verified at |
|---|---|---|---|
| Law No. 66/2025/QH15, 14 June 2025 | Art. 2(1)(l); Art. 8 tariff | Taxable category; rate schedule 0%/8%/10%; no beverage exemption list in Art. 3 | National Assembly text, official translation |
| Decree No. 360/2025/ND-CP, 31 Dec 2025 | Art. 3(4); Art. 5 | TCVN 12828:2019 as the category standard; sugar = **total** sugar on label; taxable price = producer or importer selling price excluding VAT and excise | Government text, official translation |
| Circular No. 158/2025/TT-BTC, 31 Dec 2025 | Guidance on Decree 360 | Procedural; no substantive change to base or scope | Ministry of Finance |
| Decree No. 174/2025/ND-CP, 30 June 2025 | Appendix II | Goods subject to excise excluded from the 8% VAT reduction; standard 10% applies from 2027 | `vanban.chinhphu.vn`, docid 214310 |
| TCVN 12828:2019 | Scope clause | Products in and out of the soft-drink category; source of the definitional exclusion | Standard text and implementing guidance |

**A.8 What the search established before the model was run**

*On the Vietnamese question.* The completed PubMed search returned **576 records for SSB taxation internationally and 2 for Viet Nam** — one of them a 1997 dental review of sugar consumption trends, the other the 2023 modelling study. The 2026 economic analysis is not indexed in PubMed and was found through RePEc and Google Scholar. Two analyses therefore exist in total. One modelled five tax scenarios at retail price increases of 5%, 11%, and 19–20% while the statute was under discussion, and estimated effects on bodyweight and diabetes.[17] The other used the 2018 Viet Nam Household Living Standards Survey with a quality-adjusted demand system to simulate consumption and welfare effects consistent with the 2025 law, but treats non-alcoholic beverages as a single aggregate of SSBs, bottled water, and 100% juice, and does not model disease.[18] Neither models the enacted design on its statutory base, and neither reports health benefit and tax payment on a common equity scale.

*On the international question.* By 2024, 64 countries had implemented SSB taxes covering 3.5 billion people; 45% were ad valorem, 44% volume-based, and 5% sugar-content-based.[10] WHO's own 2025 assessment reached consistent conclusions and noted that the tax base and the price point at which the tax is levied differ so much across countries that standardised comparison is difficult[11] — which is precisely why an analysis anchored to the statutory base, rather than to the headline rate, is the useful unit of comparison.

*On parameters.* Elasticities, pass-through, relative risks, and costs are available from comparable settings but not from Viet Nam, apart from the diabetes cost estimate.[34,35] This is the source of the two binding constraints identified in Appendix B: the ex-factory share of retail price and the quintile-specific disease rates.

**A.9 Maintaining the log**

The screening log, the full-text exclusion reasons, the verification log in A.7, and the search dates are deposited with the protocol at https://doi.org/10.5281/zenodo.23852996. Any string modified after registration is recorded in Appendix C.

---

## Appendix B. Parameter evidence log

One row per parameter. "Type" distinguishes a value taken from a published source, a value derived arithmetically from published data, and an assumption with no direct empirical basis. The last column records whether the parameter can be populated from existing data (yes / partly / no); where it is *no* or *partly*, the fallback column of the note states what is done instead.

**B.1 Summary table**

| # | Parameter | Proposed central value | Uncertainty range | Distribution | Source | Type | Feasible |
|---|---|---|---|---|---|---|---|
| 1 | Population by age and quintile, 2027–2050 | NSO projection; 2027 total ≈104 million | — | Fixed | NSO projections 2024–2074 [27] | Source | Yes |
| 2 | Baseline SSB consumption trend | +2.0% per year | 0 to +4.0% | Uniform | Euromonitor 2009–2023 CAGR [6] | Derived | Partly |
| 3 | SSB consumption by age, sex, quintile | 145 mL/person/day | 90 to 220 | Gamma | Euromonitor [6]; GNS 2019–20 [28]; VHLSS [36] | Derived | Partly |
| 4 | Share of taxed beverages above 5 g/100 mL | 0.80 | 0.60 to 0.95 | Beta(8,2) | Assumed; not measured | Assumption | No |
| 5 | Ex-factory share of retail price | 0.55 | 0.40 to 0.70 | Triangular | No Vietnamese source; FMCG margin structure | Assumption | **No** |
| 6 | Pass-through rate | 0.90 | 0.50 to 1.30 | Triangular | World Bank 2020 [29]; Barbados, Mexico [40] | Source (foreign) | Partly |
| 7a | Own-price elasticity | −1.20 | −0.80 to −1.80 | Lognormal on \|ε\| | Andreyeva [30]; Cabrera Escobar [24]; Colchero [21] | Source | Partly |
| 7b | Cross-price elasticity to untaxed beverages | +0.35 | +0.10 to +0.65 | Lognormal | Chile and Mexico demand systems [21] | Source | Partly |
| 7c | Quintile gradient in elasticity | Q1 = 1.4 × Q5 | 1.0 to 1.8 | — | Colchero [21] | Derived | No |
| 8a | Energy density of taxed beverages | 44 kcal/100 mL | 30 to 55 | Fixed | Vietnamese food composition table [31] | Source | Yes |
| 8b | Energy compensation | 30% | 15% to 45% | Uniform | Intervention literature [24] | Assumption | No |
| 9 | BMI to disease relative risks | per 2 kg/m²: CHD 1.11; ischaemic stroke 1.12 (1.09–1.15); haemorrhagic stroke 1.08 (1.04–1.12) | see note | Lognormal | APCSC [32,33] | Source | Yes |
| 10 | Incidence, mortality, disability weights | GBD 2021, Viet Nam, by age and sex | — | Beta; gamma | GBD 2021 [26] | Source | Yes |
| 10b | Gradient in baseline disease risk by quintile (sensitivity only) | 1.15 (Q1) to 0.88 (Q5) | 1.00 to 1.25 | — | Direction only; not measured for Viet Nam | Assumption | No |
| 11 | Health-care cost per case | Diabetes VND 8.0m per patient-year; IHD VND 84.9m per acute episode; stroke VND 10.5m per acute episode | −30% to +100% | Gamma | Le 2017 [34]; Pham 2020 [35]; Pham 2024 [41]; Doan 2022 [42] | Source | Yes |
| 12 | Household expenditure by quintile | Mean VND 3.0 million per person-month; Q5/Q1 ratio 3.1 | — | Fixed | VHLSS 2024 [36] | Source | Yes |
| 13 | Latency, BMI change to risk change | 2 years | 1 to 5 | Uniform | Assumption | Assumption | No |
| 14 | Discount rate | 3% | 0%; 5% | Fixed | CHEERS 2022 [38] | Source | Yes |

**B.2 Notes on parameters that are not directly measured**

**#2 Baseline consumption trend.** The counterfactual is the single largest driver of the absolute size of every result, and it is the parameter that the protocol originally left unspecified. Euromonitor retail volume for soft drinks in Viet Nam grew from 18 L to 66 L per capita between 2009 and 2023, an annual rate of about 9.7%. Extrapolating that rate to 2050 is not defensible: it would imply consumption far above any observed market. We therefore use a central trend of +2.0% per year, which is close to the forecast growth of the broader beverage market, and deliberately place the low bound at zero so that the "no further growth" counterfactual is retained. *Rationale:* a faster baseline makes the tax look more valuable, so a conservative trend biases the study against its own hypothesis. *Fallback:* none needed; this is a design choice, not a data gap, and it must be stated explicitly in the paper because reviewers will ask what the counterfactual assumes.

**#12 and #3, note on the expenditure profile.** Quintile means are set so that the mean (VND 3.0 million per person-month) and the Q5/Q1 ratio (3.1) reproduce the published VHLSS 2024 tabulations exactly. The share of expenditure spent on SSB is then *derived* from volume and retail price inside the model rather than assumed separately, so that it cannot contradict the consumption assumption. That derivation gives 2.6% in Q1 and 1.5% in Q5. The Gini used for the Kakwani index is computed from quintile means alone and is therefore a lower bound, which biases the estimated regressivity towards zero; the published Gini of income is 0.372. **#3 Consumption by age, sex, and quintile.** Per-capita retail volume gives the level; it does not give the distribution. Age and sex profiles come from the General Nutrition Survey 2019–2020, which records beverage intake by group. Quintile profiles come from VHLSS 2024 beverage expenditure, scaled to the Euromonitor volume total so that the two sources are mutually consistent. The central value of 145 mL/person/day is derived as 66 L/year × 0.80 (share above the threshold) ÷ 365, not observed directly. *Fallback:* if GNS beverage categories cannot be mapped to the taxable category, apply a uniform age profile and state this as a limitation.

**#5 Ex-factory share of retail price — the binding constraint.** No published Vietnamese estimate exists. The value determines the entire price effect: with τ = 0.10, *v* = 0.10, and κ = 0.90, a share of 0.40 gives a 4.0% retail price increase and a share of 0.70 gives 6.9% — a range that spans most of the plausible result space. We propose a triangular distribution centred on 0.55, derived from the typical structure of Vietnamese fast-moving consumer goods distribution (producer selling price, wholesale and retail margins, and the 10% VAT cascade), and we propose to *calibrate it empirically* rather than leave it as an assumption:

> **Calibration procedure.** If the Ministry of Finance publishes a projected yield for the SSB excise in the 2027 budget, the taxable base implied by that projection is R/τ. Dividing by the estimated retail value of taxed volume, net of VAT, gives a direct estimate of the ex-factory share. Two independent published projections, or one projection plus the market value of taxed volume, are sufficient. This converts the weakest parameter in the model into a calibrated one, and it is the single highest-value data task in the study.

*Fallback if no projection is available:* keep the triangular assumption, report the threshold analysis (the pass-through and share combinations at which the health gain becomes indistinguishable from zero), and state in the Limitations that the price effect is assumption-driven rather than estimated.

**#6 Pass-through.** Evaluated pass-through has ranged from below 50% (Berkeley, Chile, the United Kingdom) to close to 100% (Philadelphia, Mexico).[29] In Barbados, a 10% excise raised SSB prices by 5.9% six months after implementation, implying pass-through of about 60%. Because Viet Nam has no post-implementation price data at the time of writing, we centre the distribution slightly below full pass-through and allow it to exceed 100%, which is observed where firms round prices upward. *Fallback:* none; the range is the fallback.

**#7 Elasticities.** Pooled own-price elasticities for SSBs cluster between −1.0 and −1.4: −1.30 (95% CI −1.09 to −1.51) in a nine-study meta-analysis,[24] −1.16 for SSBs in Mexico,[21] −1.37 for soft drinks in Chile, and −0.79 (range −1.24 to −0.33) for soft drinks in an earlier review.[30] We centre on −1.20 and allow the full observed range. The quintile gradient is the weakest element: the consistent finding is that elasticities are larger among lower-income households,[21] but the magnitude for Viet Nam is unknown, so a gradient of 1.4 is applied and the result is reported as a sensitivity rather than as a finding.

**#8b Energy compensation.** Some of the energy displaced from beverages is replaced from other sources. Published estimates vary widely, and the choice materially affects the BMI pathway. We use a uniform distribution from 15% to 45%, centred at 30%, and note that this is an assumption rather than a Vietnamese estimate. *Fallback:* report the static-conversion sensitivity alongside, so that the reader can see how much of the result depends on this step.

**#9 Relative risks.** From the Asia-Pacific Cohort Studies Collaboration: each 2 kg/m² lower BMI is associated with a 12% (95% CI 9–15) lower risk of ischaemic stroke and an 8% (95% CI 4–12) lower risk of haemorrhagic stroke,[32] with a comparable estimate for coronary heart disease.[32] Diabetes risk is taken from the same collaboration.[33] Because relative risks are applied to BMI *categories* through population impact fractions, we convert the per-2-unit estimates to category-specific values using the midpoints of the standard Asian cut-offs (18.5, 23, 25, 30). *Rationale for preferring APCSC:* it is the only pooled Asian evidence base of adequate size, and using Western estimates would overstate risk at a given BMI in a lean population.

**Sugar density of taxed beverages.** The central value of 11 g per 100 mL is not an assumption: Nguyen and colleagues report 11 g per 100 mL for carbonates, 9 for ready-to-drink coffee and tea, 16 for sports and energy drinks, and 7 for juices in the Vietnamese market.[17] Carbonates dominate the taxed volume, so 11 is used centrally, and the full range across categories (7–16) is tested as a sensitivity analysis.

**#10 Baseline disease rates by quintile.** GBD 2021 provides national incidence, prevalence, and mortality for all three diseases, and STEPS 2021 provides measured diabetes prevalence. Neither is stratified by household expenditure. We therefore apply national rates to every quintile and assume **no** socioeconomic gradient in baseline disease rates. This is a deliberate simplification: it means equity differences in the model arise only from differential consumption and differential price response, never from an assumed disease gradient. Any real gradient in disease risk would therefore be unrepresented.

**B.3 Sequence of data tasks, in order of value**

1. Calibrate the ex-factory share (#5) from a published budget projection — highest value, because it sets the scale of every result.
2. Complete the product audit (#4) — sets the tax base and the reformulation pool for S3.
3. Map GNS 2019–2020 beverage categories to the taxable category (#3).
4. Obtain a Vietnamese cost estimate for ischaemic heart disease and stroke (#11); the diabetes cost is available.
5. Fix the baseline trend (#2) and record the decision in the deviation log if it differs from the registered protocol.

---

## Appendix C. Deviations from the plan as originally drafted

The protocol and analysis plan were deposited with the code after the model had been run. This appendix records every departure from the plan as first written, so that a reader can see what changed and why. Five departures were made.

| # | Departure | Reason |
|---|---|---|
| C1 | The revenue-neutral levy per gram of sugar (scenario S1b) was dropped | Distributing taxed volume across sugar bands requires a product-level database that does not exist for Viet Nam; without it the scenario reduces to the same average price change as the enacted tax and cannot be distinguished from it |
| C2 | No socioeconomic gradient in baseline disease rates is assumed in the base case | Quintile-specific incidence and mortality are not available for Viet Nam, so national rates are applied to every quintile; the whole analysis is repeated with an assumed gradient (Appendix B, #10b) and both runs are reported in Figure 3 |
| C3 | The product audit was not undertaken | The share of taxed beverages above the threshold is assumed (Appendix B, #4) rather than measured |
| C4 | Health-care costs for ischaemic heart disease and stroke are amortised from acute-episode studies | No Vietnamese estimate of annual cost per prevalent case exists for these two conditions |
| C5 | Latency is a two-year shift of the impact fraction, not a distributed lag | No Vietnamese evidence on the shape of the lag; a step lag is the conservative choice |

Two further points affect the reading of the equity results. The elasticity gradient across quintiles (Appendix B, #7c) is an assumption, not a measurement, and the concentration and Kakwani indices use a Gini computed from quintile means, which is a lower bound on true inequality.

## Appendix D. CHEERS 2022 checklist

| # | Item | Reported in |
|---|---|---|
| 1 | Title | Title page |
| 2 | Abstract | Summary |
| 3 | Background and objectives | Introduction |
| 4 | Health economic analysis plan | Methods, *Uncertainty and sensitivity analysis*; archived protocol |
| 5 | Study population | Methods, *Study design and overview* |
| 6 | Setting and location | Methods, *Study design and overview* |
| 7 | Comparators | Methods, *Policy scenarios*; Table 1 |
| 8 | Perspective | Methods, *Study design and overview* |
| 9 | Time horizon | Methods, *Study design and overview* |
| 10 | Discount rate | Methods; Appendix F |
| 11 | Selection of outcomes | Methods; summary of outcomes in Introduction |
| 12 | Measurement of outcomes | Methods, *Model structure* steps 5–7 |
| 13 | Valuation of outcomes | Methods step 7; disability weights from GBD 2021 |
| 14 | Measurement and valuation of resources and costs | Methods step 7; Table 2 |
| 15 | Currency, price date, and conversion | Methods, *Study design and overview* |
| 16 | Rationale and description of model | Methods, *Model structure*; Figure 1 |
| 17 | Analytics and assumptions | Methods; Appendix B; Appendix F |
| 18 | Characterising heterogeneity | Methods, *Equity analysis*; Results, *Equity* |
| 19 | Characterising distributional effects | Methods, *Equity analysis*; Figure 3 |
| 20 | Characterising uncertainty | Methods; Results, *Uncertainty*; Appendix F |
| 21 | Approach to engagement with patients and others affected | Methods, *Validation* |
| 22 | Study parameters | Table 2; Appendix B |
| 23 | Summary of main results | Results; Table 3 |
| 24 | Effect of uncertainty | Results, *Uncertainty*; Figure 4 |
| 25 | Effect of engagement | Methods, *Validation*; Discussion, Limitations |
| 26 | Study findings, limitations, and interpretation | Discussion |
| 27 | Generalisability | Discussion, *Implications for policy* |
| 28 | Source of funding, conflicts of interest, data availability | Title page; Declaration of interests; Data sharing |

---

## Appendix E. What was and was not validated

**E.1 Checks performed.** Every step of the model has a unit test with hand-calculated inputs and outputs. Population conservation is checked in the life table: no individual leaves the cohort except through death, and the living plus the dead equal the starting population in every cycle. Boundary conditions are checked: a zero tax returns the baseline exactly, a zero elasticity returns the baseline exactly, and a tax large enough to remove all consumption produces neither negative quantities nor a division error.

**E.2 Checks not performed.** Three planned checks were not carried out and the manuscript does not claim them. The model's baseline prevalence was not compared against GBD or STEPS estimates, because the life table does not age the cohort and a comparison of levels would not be informative. No external comparison was made with the earlier Vietnamese modelling study,[17] because that study reports different outcomes on a different structure. The code was not reviewed by an independent programmer. The unit tests and boundary conditions in E.1 are the whole of the technical assurance behind the results.

## Appendix F. Sensitivity analyses performed

**F.1 Probabilistic analysis.** 5,000 Monte Carlo iterations, independent sampling from the distributions in Appendix B, fixed seed (20261101), reporting medians and 95% uncertainty intervals.

**F.2 Threshold analysis.** A grid over the ex-factory share (0.30 to 0.85) and the pass-through rate (0.30 to 1.50), with the model re-run at each point, identifies the combinations at which the health gain becomes indistinguishable from zero. The grid is deposited as `output/threshold_grid.csv`.

**F.3 Elasticity grid.** Own-price elasticity from −0.3 to −2.0 in steps of 0.1, other parameters held central, to locate the point at which the health gain changes sign.

**F.4 Tax-base variants.** The share of taxed beverages set at 0.60 and 0.95, bracketing the assumed 0.80.

**F.5 Reformulation.** S3 is run at 25% reformulation centrally; the 10% and 50% levels are reported in the text.

**F.6 Gradient in baseline disease risk.** The whole probabilistic analysis is repeated with a socioeconomic gradient in baseline incidence, 1.15 in Q1 falling to 0.88 in Q5, on the same 5,000 draws. The concentration index of DALYs averted moves from a median of 0.047 to −0.002 and the Q1/Q5 ratio from 0.77 to 0.99, while the Kakwani index is unaffected because it depends only on tax payments. The two runs are shown side by side in Figure 3 and deposited as `output/psa_gradient.csv`.

**F.7 Analyses not run.** A static weight model, low and high elasticity sets, a full pass-through grid crossed with broad and narrow legal interpretations of the tax base, and a distributed latency were planned and not carried out. None is reported.

## Appendix G. Code and reproducibility

**H.1 Environment**

R version 4.6.1. Package versions are pinned in `renv.lock`; the repository records the full session information for the run that produced each table and figure.

**H.2 Repository structure**

```
/model seven model steps, one file each, plus the life-table engine
/params parameter tables, PSA draw matrix, evidence-log CSV
/analysis scripts that generate each table and figure in order
/output generated tables and figures, with the seed in the filename
/tests unit tests and boundary-condition tests
/docs protocol, appendices, deviation log
```

**H.3 Reproducibility**

A single script reproduces every number in the manuscript from the parameter file and a fixed seed. The PSA input matrix is published as a CSV so that the results can be checked without re-running the sampling. Runtime for the full analysis is recorded so that a reviewer can judge feasibility.

**H.4 Licence and citation**

Code released under an open licence on acceptance; the repository carries a DOI. The parameter evidence log is released as a data file with a column for the source of every value.

---
