# Bản đăng ký OSF — nội dung dán trực tiếp

> Nộp **trước khi chạy mô hình chính**. Loại đăng ký gợi ý: *Pre-registration* (OSF) hoặc *Registered Report* nếu tạp chí hỗ trợ.
> **Viết bằng tiếng Anh** vì đăng ký này là tài liệu công khai và sẽ được trích dẫn trong bài (mục Phương pháp: "registered on OSF, ⟦ID⟧, on ⟦date⟧"). Có thể kèm bản tiếng Việt như tệp đính kèm.
> Chỗ `⟦...⟧` phải điền trước khi nộp. Đừng để trống ô nào — OSF cho phép sửa sau nhưng mọi sửa đổi phải ghi vào Phụ lục D.

---

## 1. Title

Health and distributional impacts of Viet Nam's enacted sugar-sweetened beverage excise tax: an ex-ante modelling study

## 2. Description

This is a pre-registration of an ex-ante policy modelling study. We will estimate the health, health-care cost, revenue, and distributional consequences of the excise tax on sugar-sweetened beverages legislated by Viet Nam in Law No. 66/2025/QH15 of 14 June 2025, which applies a rate of 0% in 2026, 8% from 1 January 2027, and 10% from 1 January 2028 to beverages containing more than 5 g of total sugar per 100 mL.

The study is a proportional multi-state life-table model of the Vietnamese population aged 20 years and older, stratified by single year of age, sex, and household expenditure quintile. It does not collect new human data. It is reported in accordance with CHEERS 2022.

The analysis is pre-specified because the study is intended to inform a statutory review scheduled for 2028, and because the choice of counterfactual and of price pass-through can materially change the conclusion. Registering these choices in advance prevents post-hoc selection among defensible alternatives.

## 3. Research questions and outcomes

**Primary question.** Compared with no tax, how many disability-adjusted life-years (DALYs) does the tax as enacted avert in Viet Nam between 2027 and 2050, and how are those DALYs distributed across household expenditure quintiles?

**Secondary questions.** (i) How does the enacted design compare, in health gain and in revenue, with a 20% increase in retail price as recommended by WHO? (ii) What is the return in DALYs per unit of revenue of the enacted design? (iii) What proportion of household expenditure does the tax absorb in each quintile?

**Primary outcome.** Cumulative DALYs averted, whole population, 2027–2050, discounted at 3% per year.

**Co-primary equity outcome.** Absolute difference in DALYs averted per 1,000 population between the poorest (Q1) and richest (Q5) quintile, reported with the concentration index of DALYs averted.

**Secondary outcomes.** Change in consumption (mL/person/day); change in BMI; cases and deaths averted for type 2 diabetes, ischaemic heart disease, and stroke; health-care costs saved; revenue raised; tax paid as a percentage of household expenditure by quintile; Kakwani index; equivalent-relative and equivalent-absolute health from the Atkinson index at inequality aversion of 1, 3, and 10.

## 4. Design and scope

**Population.** Vietnamese population 2027–2050, single year of age from 20, by sex, by expenditure quintile.

**Perspective.** Health system for costs; household for distributional analysis; government for revenue.

**Time horizon.** 2027–2050 and lifetime, with reporting at 10 years as well.

**Discount rate.** 3%, with 0% and 5% in sensitivity analysis.

**Currency.** 2026 Vietnamese dong, converted to US dollars at the rate in force in ⟦month/year⟧.

**Diseases modelled.** Type 2 diabetes, ischaemic heart disease, stroke.

**Explicitly not modelled in the main analysis.** Dental caries; ages under 20; direct effects of sugar independent of BMI. These are stated as limitations in the manuscript and are reserved for an extension.

## 5. Policy scenarios

| Code | Scenario | Specification |
|---|---|---|
| S0 | No tax | Counterfactual; baseline consumption trend |
| S1 | Tax as enacted | 8% (2027), 10% (2028+); >5 g/100 mL; ex-factory base; VAT cascade; statutory exclusions |
| S2 | WHO benchmark | 20% retail price increase from 2027 |
| S3 | Enacted tax + reformulation | 10%, 25%, 50% of near-threshold products reformulate below 5 g/100 mL |

Tax pass-through is treated as a sensitivity parameter, not a scenario, and is varied at 50%, 100%, and 150%.

## 6. Model structure

Seven linked steps: (1) statutory rate to retail price, accounting for the ex-factory tax base and the value-added tax levied on the excise-inclusive price; (2) price to demand through own- and cross-price elasticities; (3) demand to energy intake, net of compensation; (4) energy to BMI through a dynamic weight-change model; (5) BMI to disease incidence through population impact fractions with a latency period; (6) two parallel multi-state life tables; (7) costs, revenue, and DALYs.

## 7. Parameters and sources

Parameters will be selected by a pre-specified four-step hierarchy: nationally representative Vietnamese data from the past 10 years; meta-analyses for low- and middle-income countries or for Asia; comparable neighbouring countries with widened uncertainty; and documented expert assumptions with wide sensitivity ranges. Every parameter, its source, its uncertainty range, its distribution, and the rationale for the choice will be recorded in an evidence log published with the study.

Two parameters are pre-identified as binding constraints and the handling is specified in advance:

- **Ex-factory share of retail price** (no Vietnamese estimate exists). A triangular distribution centred on 0.55 with range 0.40–0.70 will be used, and the value will be calibrated if a published Ministry of Finance revenue projection for the 2027 excise yield becomes available, by dividing the implied tax base by the estimated retail value of taxed volume.
- **Quintile-specific baseline disease rates** (not available for Viet Nam). National rates will be applied to all quintiles in the base case, with a gradient derived from STEPS 2021 applied in sensitivity analysis only.

## 8. Analysis plan

**Probabilistic analysis.** 5,000 Monte Carlo iterations, independent sampling from the specified distributions, fixed seed, reporting medians with 95% uncertainty intervals. The probability that S1 yields a positive health gain and the probability that S2 exceeds S1 will be reported.

**One-way analysis.** Tornado diagram for the ten parameters contributing most to variance.

**Structural scenarios.** Static versus dynamic weight model; low and high elasticity sets; pass-through 50/100/150%; taxed share 0.60 and 0.95; the three reformulation levels of S3; broad versus narrow legal interpretation of the taxable category (nectars, juice-containing drinks, coconut water, non-caloric-sweetened products).

**Threshold analysis.** A grid over pass-through (0.3–1.5) and ex-factory share (0.30–0.85) will identify the boundary at which the health gain becomes indistinguishable from zero. This boundary, not the point estimate, will be reported as the study's most robust statement.

**Equity analysis.** The model is run separately for each quintile. Where quintile-specific epidemiological parameters are unavailable, this is stated for each parameter. Atkinson-based measures are reported as within-quintile approximations.

**Validation.** Baseline reproduction against published Vietnamese incidence, prevalence, and mortality (acceptance within ±15% for disease rates, ±5% for all-cause mortality, ±1% for population totals); external comparison with the 2023 Vietnamese modelling study at a comparable 20% price change, with differences decomposed by source.

## 9. Deviations

Any change to the scenarios, the parameter set, the elasticity set, the latency, the discount rate, the primary outcome, or the method for computing equivalent health will be recorded in a dated deviation log and reported in the manuscript.

## 10. Ethics and data

The study uses published parameters and secondary data only, involves no human participants, and accesses no individual-level records other than de-identified household survey data under the provider's access conditions. Ethical approval is not required. The analytic code, the parameter evidence log, and the probabilistic sensitivity analysis input matrix will be made publicly available at publication.

## 11. Registration metadata

| Field | Value |
|---|---|
| Registration type | Pre-registration |
| Date of registration | ⟦date⟧ — **must precede the main model runs** |
| Contributors | ⟦names and ORCID⟧ |
| Funding | ⟦funder, grant number, or "none"⟧ |
| Conflicts of interest | ⟦statement⟧ |
| Associated manuscript | ⟦none at registration⟧ |

---

## Việc phải làm trước khi bấm nộp

1. Chốt **xu hướng tiêu thụ nền** (+2,0%/năm; nếu khác, ghi vào đây, đừng để trống).
2. Chốt **bộ độ co giãn** sẽ dùng làm trung tâm (−1,20).
3. Chốt **độ trễ** (2 năm).
4. Điền **tên, ORCID, tài trợ, COI**.
5. Tạo tệp đính kèm: protocol đầy đủ + Phụ lục A–H.
6. **Chỉ sau đó** mới chạy mô hình chính. Nếu chạy trước, đăng ký mất giá trị và phải khai trong Phụ lục D.
