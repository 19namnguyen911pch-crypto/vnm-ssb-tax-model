# Supplementary material

Supplementary material for: Modest health gains and regressive financing from Viet Nam's sugar-sweetened beverage excise tax: a modelling study. Reference numbers in parentheses refer to the main reference list; numbers prefixed S refer to the list below.

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

The Cochrane and RePEc searches were run without a country limit because the review and trial literature on SSB taxes is thin and almost entirely non-Vietnamese; the Vietnamese subset is isolated by the country term.

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

The broad sets without a country limit returned 576 records in PubMed, 506 in Europe PMC, 2 961 in OpenAlex, 1 526 in Cochrane CENTRAL and 21 in RePEc. These were screened for parameter evidence rather than for inclusion in a review of effects, because the study needs estimates from any comparable setting. The RePEc set contained no Vietnamese study but two evaluations of European soda taxes that report pass-through, and both are cited for that parameter (Appendix B, #5). The 21 retrieved records, with the decision for each, are in `data/repec_screening.csv`.

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

*On the Vietnamese question.* The completed PubMed search returned **576 records for SSB taxation internationally and 2 for Viet Nam** — one of them a 1997 dental review of sugar consumption trends, the other the 2023 modelling study. The 2026 analysis is not indexed in PubMed and was identified through Scopus. Two modelling analyses therefore exist in total. One modelled five tax scenarios at retail price increases of 5%, 11%, and 19–20% while the statute was under discussion, and estimated effects on bodyweight and diabetes.(12) The other used the 2018 Viet Nam Household Living Standards Survey with a quality-adjusted demand system to simulate consumption and welfare effects consistent with the 2025 law, but treats non-alcoholic beverages as a single aggregate of SSBs, bottled water, and 100% juice, and does not model disease.(13) Neither models the enacted design on its statutory base, and neither reports how health benefit and tax payment are distributed across the same expenditure groups.

*On the international question.* By 2024, 64 countries had implemented SSB taxes covering 3.5 billion people; 45% were ad valorem, 44% volume-based, and 5% sugar-content-based.(6) WHO's own 2025 assessment reached consistent conclusions and noted that the tax base and the price point at which the tax is levied differ so much across countries that standardised comparison is difficult(S8) — which is precisely why an analysis anchored to the statutory base, rather than to the headline rate, is the useful unit of comparison.

*On parameters.* Elasticities, pass-through, relative risks, and costs are available from comparable settings but not from Viet Nam, apart from the diabetes cost estimate.(19,20) This is the source of the two binding constraints identified in Appendix B: the ex-factory share of retail price and the quintile-specific disease rates.

**A.9 Maintaining the log**

The screening log, the full-text exclusion reasons, the verification log in A.7, and the search dates are deposited with the protocol at https://doi.org/10.5281/zenodo.23852908. Any string modified after the protocol was deposited is recorded in Appendix C.

---

## Appendix B. Parameter evidence log

One row per parameter. "Type" distinguishes a value taken from a published source, a value derived arithmetically from published data, and an assumption with no direct empirical basis. The last column records whether the parameter can be populated from existing data (yes / partly / no); where it is *no* or *partly*, the fallback column of the note states what is done instead.

**B.1 Summary table**

| # | Parameter | Central value used | Uncertainty range | Distribution | Source | Type | Feasible |
|---|---|---|---|---|---|---|---|
| 1 | Population aged 20+, by age and quintile | 81 million, 2027 distribution held for every year | — | Fixed | UN World Population Prospects 2024 (S1) | Source | Yes |
| 2 | Baseline SSB consumption trend | +2.0% per year | 0 to +4.0% | Uniform | Euromonitor 2009–2023 CAGR (2) | Derived | Partly |
| 3 | SSB consumption by age, sex, quintile | 145 mL/person/day | 90 to 220 | Gamma | Euromonitor (2); GNS 2019–20 (S2); VHLSS (S3) | Derived | Partly |
| 4 | Ex-factory share of retail price | 0.55 | 0.40 to 0.70 | Triangular | No Vietnamese source; FMCG margin structure | Assumption | **No** |
| 5 | Pass-through rate | 0.90 | 0.50 to 1.30 | Triangular | World Bank 2020 (24); Barbados, Mexico (S4); Portugal, France (25,26) | Source (foreign) | Partly |
| 6a | Own-price elasticity | −1.20 | −0.80 to −1.80 | Lognormal on \|ε\| | Andreyeva (S5); Cabrera Escobar (S6); Colchero (14) | Source | Partly |
| 6b | Cross-price elasticity to untaxed beverages | +0.35 | +0.10 to +0.65 | Lognormal | Chile and Mexico demand systems (14) | Source | Partly |
| 6c | Quintile gradient in elasticity | Q1 = 1.4 × Q5 | 1.0 to 1.8 | — | Colchero (14) | Derived | No |
| 7a | Energy density of taxed beverages | 44 kcal/100 mL | 30 to 55 | Fixed | Vietnamese food composition table (S7) | Source | Yes |
| 7b | Energy compensation | 30% | 15% to 45% | Uniform | Assumption; no Vietnamese estimate | Assumption | No |
| 8 | BMI to disease relative risks | per 2 kg/m²: CHD 1.11; ischaemic stroke 1.12 (1.09–1.15); haemorrhagic stroke 1.08 (1.04–1.12) | see note | Lognormal | APCSC (17,18) | Source | Yes |
| 9 | Incidence, mortality, disability weights | GBD 2021, Viet Nam, by age and sex | — | Beta; gamma | GBD 2021 (23) | Source | Yes |
| 9b | Gradient in baseline disease risk by quintile (sensitivity only) | Both directions: 1.15 (Q1) falling to 0.88 (Q5), and the reverse | 0.85 to 1.20 | — | Direction not established for Viet Nam | Assumption | No |
| 10 | Health-care cost per case | Diabetes VND 8.0m per patient-year; IHD VND 84.9m per acute episode; stroke VND 10.5m per acute episode | −30% to +100% | Gamma | Le 2017 (19); Pham 2020 (20); Pham 2024 (21); Doan 2022 (22) | Source | Yes |
| 11 | Household expenditure by quintile | Mean VND 3.0 million per person-month; Q5/Q1 ratio 3.1 | — | Fixed | VHLSS 2024 (S3) | Source | Yes |
| 12 | Latency, BMI change to risk change | 2 years | 1 to 5 | Uniform | Assumption | Assumption | No |
| 13 | Discount rate | 3% | 0%; 5% | Fixed | CHEERS 2022 (27) | Source | Yes |

**B.2 Notes on parameters that are not directly measured**

**#2 Baseline consumption trend.** The counterfactual is the single largest driver of the absolute size of every result, and it is the parameter that the protocol originally left unspecified. Euromonitor retail volume for soft drinks in Viet Nam grew from 18 L to 66 L per capita between 2009 and 2023, an annual rate of about 9.7%. Extrapolating that rate to 2050 is not defensible: it would imply consumption far above any observed market. We therefore use a central trend of +2.0% per year, which is close to the forecast growth of the broader beverage market, and deliberately place the low bound at zero so that the "no further growth" counterfactual is retained. *Rationale:* a faster baseline makes the tax look more valuable, so a conservative trend biases the study against its own hypothesis. *Fallback:* none needed; this is a design choice, not a data gap, and it must be stated explicitly in the paper because reviewers will ask what the counterfactual assumes.

**#3 Volume of taxed beverages.** Revenue is computed on the adult population, because the model covers ages 20 and over; consumption per adult is therefore the relevant denominator, not per-capita consumption of the whole population. Euromonitor reports 66 L per capita in 2023 for soft drinks as a category; the extract we hold does not break that total down by sub-category, so it cannot be used directly as the volume of taxed beverages. The 145 mL per day used centrally is the volume implied by applying the assumed share of consumption above the threshold to that total, and it is carried as a parameter with a range of 90 to 220 mL per day rather than as a measured value. A product-level database would replace it.

**#11 and #3, note on the expenditure profile.** Quintile means are set so that the mean (VND 3.0 million per person-month) and the Q5/Q1 ratio (3.1) reproduce the published VHLSS 2024 tabulations exactly. The share of expenditure spent on SSB is then *derived* from volume and retail price inside the model rather than assumed separately, so that it cannot contradict the consumption assumption. That derivation gives 2.6% in Q1 and 1.5% in Q5. The Gini used for the Kakwani index is computed from quintile means alone and is therefore a lower bound, which biases the estimated regressivity towards zero; the published Gini of income is 0.372. **#3 Consumption by age, sex, and quintile.** Per-capita retail volume gives the level; it does not give the distribution. Age and sex profiles come from the General Nutrition Survey 2019–2020, which records beverage intake by group. Quintile profiles come from VHLSS 2024 beverage expenditure, scaled to the Euromonitor volume total so that the two sources are mutually consistent. The central value of 145 mL/person/day is derived as 66 L/year × 0.80 (share above the threshold) ÷ 365, not observed directly. *Fallback:* if GNS beverage categories cannot be mapped to the taxable category, apply a uniform age profile and state this as a limitation.

**#4 Ex-factory share of retail price.** No published Vietnamese estimate exists. The value determines the entire price effect: with τ = 0.10, *v* = 0.10, and κ = 0.90, a share of 0.40 gives a 4.0% retail price increase and a share of 0.70 gives 6.9% — a range that spans most of the plausible result space. We use a triangular distribution centred on 0.55, derived from the typical structure of Vietnamese fast-moving consumer goods distribution (producer selling price, wholesale and retail margins, and the 10% VAT cascade). It is an assumption and no Vietnamese estimate exists. It would be calibrated directly if the Ministry of Finance published a projected yield for the excise, since the taxable base implied by that projection is R/τ and dividing by the retail value of taxed volume net of VAT gives the share; no such projection was available for this analysis. The share enters the model only as the product with pass-through, so the two are not separately identified: the two-way grid in Appendix F.2 spans both, and the text reports the combinations rather than attributing the effect to either parameter.

**#5 Pass-through.** Evaluated pass-through has ranged from below 50% (Berkeley, Chile, the United Kingdom) to close to 100% (Philadelphia, Mexico).(24) In Barbados, a 10% excise raised SSB prices by 5.9% six months after implementation, implying pass-through of about 60%. Two further evaluations retrieved from the economics literature, of the Portuguese and French soda taxes, report near-complete pass-through to retail prices.(25,26) Because Viet Nam has no post-implementation price data at the time of writing, we centre the distribution slightly below full pass-through and allow it to exceed 100%, which is observed where firms round prices upward. *Fallback:* none; the range is the fallback.

**#6 Elasticities.** Pooled own-price elasticities for SSBs cluster between −1.0 and −1.4: −1.30 (95% CI −1.09 to −1.51) in a nine-study meta-analysis,(S6) −1.16 for SSBs in Mexico,(14) −1.37 for soft drinks in Chile, and −0.79 (range −1.24 to −0.33) for soft drinks in an earlier review.(S5) We centre on −1.20 and allow the full observed range. The quintile gradient is the weakest element: the consistent finding is that elasticities are larger among lower-income households,(14) but the magnitude for Viet Nam is unknown, so a gradient of 1.4 is applied and the result is reported as a sensitivity rather than as a finding.

**#7b Energy compensation.** Some of the energy displaced from beverages is replaced from other sources. Published estimates vary widely, and the choice materially affects the BMI pathway. We use a uniform distribution from 15% to 45%, centred at 30%, and note that this is an assumption rather than a Vietnamese estimate; no Vietnamese measurement exists and none is available from a comparable setting we could verify, so the value carries no citation.

**#8 Relative risks.** From the Asia-Pacific Cohort Studies Collaboration: each 2 kg/m² lower BMI is associated with a 12% (95% CI 9–15) lower risk of ischaemic stroke and an 8% (95% CI 4–12) lower risk of haemorrhagic stroke,(17) with a comparable estimate for coronary heart disease.(17) Each 2 kg/m² lower BMI is associated with a 27% (95% CI 23–30) lower risk of diabetes in the same collaboration.(18) Because relative risks are applied to BMI *categories* through population impact fractions, we convert the per-2-unit estimates to category-specific values using the midpoints of the standard Asian cut-offs (18.5, 23, 25, 30). *Rationale for preferring APCSC:* it is the only pooled Asian evidence base of adequate size, and using Western estimates would overstate risk at a given BMI in a lean population.

**Sugar density of taxed beverages.** The central value of 11 g per 100 mL is not an assumption: Nguyen and colleagues report 11 g per 100 mL for carbonates, 9 for ready-to-drink coffee and tea, 16 for sports and energy drinks, and 7 for juices in the Vietnamese market.(12) Carbonates dominate the taxed volume, so 11 is used centrally, and the full range across categories (7–16) is tested as a sensitivity analysis.

**#9 Baseline disease rates by quintile.** GBD 2021 provides national incidence, prevalence, and mortality for all three diseases, and STEPS 2021 provides measured diabetes prevalence. Neither is stratified by household expenditure. We therefore apply national rates to every quintile in the base case, which means that equity differences arise only from differential consumption and differential price response. The direction of the true gradient is not established for Viet Nam: quintile-specific incidence and mortality are not published, and we could not verify a source that would support a central value. We therefore run the analysis under no gradient, under risk falling with expenditure, and under risk rising with expenditure, and report the equity result as a range (Appendix F, Figure 3).

**B.3 What would most change the estimates**

In the variance decomposition the own-price elasticity accounts for 45% of the explained variance, the BMI–diabetes relative risk for 17% and the pass-through rate for 16%; the ex-factory share accounts for 6%, because it enters only through the price change and is partly absorbed by pass-through. A measured gradient in baseline disease risk (#9b) would not change the variance in DALYs at all, but it would resolve the distributional result. A product-level database of taxed beverages would replace the assumed sugar density and would allow a levy per gram of sugar to be modelled; neither exists for Viet Nam and the manuscript does not claim them.

---

## Appendix C. Deviations from the plan as originally drafted

The protocol and analysis plan were deposited with the code after the model had been run. This appendix records every departure from the plan as first written, so that a reader can see what changed and why. Five departures were made.

| # | Departure | Reason |
|---|---|---|
| C1 | The revenue-neutral levy per gram of sugar (scenario S1b) was dropped | Distributing taxed volume across sugar bands requires a product-level database that does not exist for Viet Nam; without it the scenario reduces to the same average price change as the enacted tax and cannot be distinguished from it |
| C2 | No socioeconomic gradient in baseline disease rates is assumed in the base case | Quintile-specific incidence and mortality are not available for Viet Nam, so national rates are applied to every quintile; the whole analysis is repeated with a gradient in each direction (Appendix B, #9b) and all three runs are reported in Figure 3 |
| C3 | The product audit was not undertaken | The sugar density of the taxed category is taken from (12) rather than measured, and the reformulation pool assumed for S3 is a modelling choice |
| C4 | Health-care costs for ischaemic heart disease and stroke are amortised from acute-episode studies | No Vietnamese estimate of annual cost per prevalent case exists for these two conditions |
| C5 | Latency is a two-year shift of the impact fraction, not a distributed lag | No Vietnamese evidence on the shape of the lag; a step lag is the conservative choice |

Two further points affect the reading of the equity results. The elasticity gradient across quintiles (Appendix B, #6c) is an assumption, not a measurement, and the concentration and Kakwani indices use a Gini computed from quintile means, which is a lower bound on true inequality.

## Appendix D. CHEERS 2022 checklist

| # | Item | Reported in |
|---|---|---|
| 1 | Title | Title page |
| 2 | Abstract | Abstract |
| 3 | Background and objectives | Introduction |
| 4 | Health economic analysis plan | Methods, uncertainty section; archived protocol |
| 5 | Study population | Methods, first paragraph |
| 6 | Setting and location | Methods, first paragraph |
| 7 | Comparators | Methods, scenarios; Table 1 |
| 8 | Perspective | Methods, first paragraph |
| 9 | Time horizon | Methods, first paragraph |
| 10 | Discount rate | Methods; Appendix F |
| 11 | Selection of outcomes | Introduction, final paragraph |
| 12 | Measurement of outcomes | Methods, model structure |
| 13 | Valuation of outcomes | Methods, model structure; GBD 2021 weights |
| 14 | Measurement and valuation of resources and costs | Methods; Appendix B |
| 15 | Currency, price date, and conversion | Methods, first paragraph |
| 16 | Rationale and description of model | Methods, model structure; Fig. 1 |
| 17 | Analytics and assumptions | Methods; Appendix B; Appendix F |
| 18 | Characterising heterogeneity | Methods, equity; Results, equity |
| 19 | Characterising distributional effects | Methods, equity; Fig. 3; Table 4 |
| 20 | Characterising uncertainty | Methods; Results, uncertainty; Appendix F |
| 21 | Approach to engagement with patients and others affected | Not undertaken; published qualitative evidence used (ref 38) |
| 22 | Study parameters | Appendix B |
| 23 | Summary of main results | Results; Table 3 |
| 24 | Effect of uncertainty | Results, uncertainty; Fig. 4 |
| 25 | Effect of engagement | Not applicable |
| 26 | Study findings, limitations, and interpretation | Discussion |
| 27 | Generalisability | Discussion, implications for policy |
| 28 | Source of funding, conflicts of interest, data availability | Title page; declarations; data availability |

## Appendix E. What was and was not validated

**E.1 Checks performed.** Every step of the model has a unit test with hand-calculated inputs and outputs. Population conservation is checked in every cycle: no individual leaves the population except through death, and the living plus the dead equal the starting population in every cycle. Boundary conditions are checked: a zero tax returns the baseline exactly, a zero elasticity returns the baseline exactly, and a tax large enough to remove all consumption produces neither negative quantities nor a division error.

**E.2 Baseline comparison.** The model's own prevalence at the end of the horizon was compared with the source its disease parameters come from, on the same 2027 age structure: 5.1% against 6.2% for type 2 diabetes, 0.4% against 1.6% for ischaemic heart disease, and 1.2% against 1.9% for stroke (GBD 2021). Diabetes, which carries 85% of the averted cases, is the closest. The shortfall in the cardiovascular states follows from starting in 2027 without a prevalent stock and applying a high case fatality to new cases. Initialising the stock from GBD 2021 lowers the averted gain by 8.8% and averted costs by 8.1%, so the base case is optimistic; this is recorded in the Limitations.

**E.3 Checks not performed.** Two checks were not carried out and the manuscript does not claim them. No external comparison was made with the earlier Vietnamese modelling study,(12) because that study reports different outcomes on a different model structure and the comparison would not isolate model error. The code was not reviewed by an independent programmer. The unit tests, the boundary conditions in E.1 and the baseline comparison in E.2 are the whole of the technical assurance behind the results.

## Appendix F. Sensitivity analyses performed

**F.1 Probabilistic analysis.** 5 000 Monte Carlo iterations, independent sampling from the distributions in Appendix B, fixed seed (20261101), reporting medians and 95% uncertainty intervals. The contribution of each parameter to the variance in DALYs averted was obtained from a linear model of the 5 000 draws on the sampled parameters, with squared semipartial correlations as shares of the explained variance; that model explains 93% of the variation.

**F.2 Threshold analysis.** A grid over the ex-factory share (0.30 to 0.85) and the pass-through rate (0.30 to 1.50), with the model re-run at each point, identifies the combinations at which the health gain becomes indistinguishable from zero. The grid is deposited as `output/threshold_grid.csv`.

**F.3 Elasticity grid.** Own-price elasticity from −0.3 to −2.0 in steps of 0.1, other parameters held central, to locate the point at which the health gain changes sign.

**F.4 Reformulation.** S3 is run at 25% reformulation centrally; the 10% and 50% levels are reported in the text.

**F.5 One-way structural sensitivity.** Discount rate 0% and 5%; pass-through 0.50, 0.90 and 1.30; own-price elasticity −0.80, −1.20 and −1.80; horizon 2036, 2050 and 2100; and a run that starts from the GBD 2021 prevalent stock instead of from zero. At central values the health gain is 27 824 and 12 995 DALYs at discount rates of 0% and 5%; 9 573 and 24 827 at pass-through 0.50 and 1.30; 11 484 and 25 777 at elasticity −0.80 and −1.80; 5 575, 17 209 and 36 419 over the 10-year, 2050 and 2100 horizons; and 15 696 when the prevalent stock is initialised from GBD 2021. Deposited as `output/sensitivity.csv`.

**F.6 Disease and elasticity gradients together.** Both gradients are assumptions, so they are reported jointly. The table gives the Q1/Q5 ratio of DALYs averted and the concentration index at each combination of the disease gradient (baseline risk rising with expenditure, none, falling with expenditure) and the quintile elasticity gradient (1.0, 1.39 at base, 1.8). The Kakwani index and the tax share move far less, because payments depend on consumption rather than on disease risk.

| Baseline risk | Elasticity gradient | Q1/Q5 | Concentration index | Kakwani | Tax, Q1 (%) | Tax, Q5 (%) |
|---|---|---|---|---|---|---|
| Rises with expenditure | 1.0 | 0.43 | 0.160 | −0.101 | 0.135 | 0.078 |
| Rises with expenditure | 1.39 | 0.60 | 0.096 | −0.096 | 0.133 | 0.079 |
| Rises with expenditure | 1.8 | 0.78 | 0.045 | −0.093 | 0.132 | 0.080 |
| None | 1.0 | 0.56 | 0.112 | −0.101 | 0.135 | 0.078 |
| None | 1.39 | 0.77 | 0.047 | −0.096 | 0.133 | 0.079 |
| None | 1.8 | 1.00 | −0.005 | −0.093 | 0.132 | 0.080 |
| Falls with expenditure | 1.0 | 0.71 | 0.063 | −0.101 | 0.135 | 0.078 |
| Falls with expenditure | 1.39 | 0.99 | −0.003 | −0.096 | 0.133 | 0.079 |
| Falls with expenditure | 1.8 | 1.28 | −0.054 | −0.093 | 0.132 | 0.080 |

Deposited as `output/equity_grid.csv`.

**F.7 Analyses not run.** A static weight model, a full cross of the pass-through grid with broad and narrow legal interpretations of the taxable category, and a distributed latency were considered and not carried out. None is reported.

## Appendix G. Code and reproducibility

**G.1 Environment.** R version 4.6.1, base R only, with no package dependencies. The model, the probabilistic analysis and the figures run from a clean installation of R; the DOCX files are built with Python 3 and `python-docx`.

**G.2 Repository.** `model/` holds the model (`pmslt_model.R`), the quintile profile (`vhlss.R`), the probabilistic analysis (`psa.R`, `psa_all.R`, `psa_gradient.R`) and the script that writes every number in the manuscript (`fill_results.R`). `data/` holds the parameter inputs and the screening log. `output/` holds the draw matrix, the draws, the threshold grid and the gradient run. `Ban_thao/` holds the manuscript sources, the figure script and the generated DOCX files.

**G.3 Reproduction.** The main results are reproduced in five steps, each writing its output to `output/`:

```
Rscript model/psa_all.R        # 5 000 draws, seed 20261101 -> psa_results.csv, psa_draws.csv
Rscript model/psa_gradient.R   # same draws, three disease gradients -> psa_gradient.csv
Rscript model/sensitivity.R    # one-way structural runs -> sensitivity.csv
Rscript model/fill_results.R   # every number in the manuscript -> results.json
Rscript Ban_thao/Figures/make_figures.R   # Figures 1-4
```

The seed is fixed at 20261101, and the draw matrix is published as `output/psa_draws.csv` so that the probabilistic results can be checked without re-running the sampling. The full analysis takes about 40 minutes on a laptop; the deterministic results alone take under a minute. The repository is public at https://doi.org/10.5281/zenodo.23852908 under the MIT licence.


---

## Supplementary references

S1. United Nations, Department of Economic and Social Affairs, Population Division. World Population Prospects 2024: volume I, comprehensive tables. New York: United Nations; 2024.
S2. National Institute of Nutrition, Ministry of Health of Viet Nam. General Nutrition Survey 2019–2020. Hanoi; 2021.
S3. National Statistics Office of Viet Nam. Results of the Viet Nam Household Living Standards Survey 2024. Hanoi; 2025.
S4. Hernández JCS, et al. Building upon the sugar beverage tax in Mexico. BMJ Glob Health. 2023;8(Suppl 8):e012227.
S5. Andreyeva T, Long MW, Brownell KD. The impact of food prices on consumption: a systematic review of research on the price elasticity of demand for food. Am J Public Health. 2010;100(2):216–22.
S6. Cabrera Escobar MA, Veerman JL, Tollman SM, Bertram MY, Hofman KJ. Evidence that a tax on sugar sweetened beverages reduces the obesity rate: a meta-analysis. BMC Public Health. 2013;13:1072.
S7. National Institute of Nutrition, Ministry of Health of Viet Nam. Vietnamese food composition table. Hanoi: Medical Publishing House; 2017.
S8. WHO. Global report on the use of sugar-sweetened beverage taxes, 2025. Geneva: World Health Organization; 2025.
