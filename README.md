# Viet Nam SSB excise tax — modelling code and parameters

<!-- DOI badge -->
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23852908.svg)](https://doi.org/10.5281/zenodo.23852908)

Reproducibility package for:

> **The excise base, not the headline rate, drives the health gain from Viet Nam's
> sugar-sweetened beverage tax: an ex-ante modelling study**
> Nguyen Thanh Nam, Khanh Linh Lam Ngoc
> Faculty of Public Health, University of Medicine and Pharmacy at Ho Chi Minh City

## What this repository contains

A proportional multi-state life-table model of the Vietnamese population aged 20+,
used to estimate the health, cost, revenue and distributional consequences of the
excise tax legislated by Law No. 66/2025/QH15.

| Path | Contents |
|---|---|
| `model/pmslt_model.R` | Core model: seven steps, life table, equity metrics |
| `model/psa.R` | Probabilistic sensitivity analysis |
| `model/psa_all.R` | 5,000-draw PSA for S1, S2 and S3 |
| `model/psa_gradient.R` | The same draws with a socioeconomic gradient in disease risk |
| `model/vhlss.R` | Expenditure quintile profile (published VHLSS tabulations) |
| `model/fill_results.R` | Produces every number in the manuscript |
| `Ban_thao/Figures/make_figures.R` | Figures 1-4 |
| `model/run_all.R` | Driver |
| `data/` | Parameters, with sources |
| `output/` | Generated results |

## Running

Requires R ≥ 4.6. No package dependencies beyond base R.

```bash
Rscript model/psa_all.R                    # 5,000 draws -> output/psa_results.csv
Rscript model/psa_gradient.R               # same draws, three disease gradients
Rscript model/sensitivity.R                # one-way structural runs
Rscript model/fill_results.R               # every number in the paper
Rscript Ban_thao/Figures/make_figures.R    # Figures 1-4
```

Seed 20261101. Runtime for the full analysis: about 40 minutes on a laptop;
the deterministic results alone take under a minute.

## Data sources

| Input | Source | Licence |
|---|---|---|
| Age structure | UN World Population Prospects 2024, medium variant | Open |
| Disease parameters | GBD 2021, Viet Nam (IHME) | Free for non-commercial use, attribution required |
| Health-care costs | Le 2017; Pham 2024; Doan 2022 | Published values |
| Expenditure quintiles | VHLSS 2024 published tabulations (NSO) | Public statistics |

`data/gbd_vnm/vnm_gbd_params_long.csv` is a **derived** table: incidence, prevalence,
mortality and disability weights extracted from the GBD Results Tool and transformed
for the model. The raw extraction is not redistributed; obtain it from
<https://ghdx.healthdata.org/gbd-results-tool> under IHME's terms of use.

## Licence

Code: MIT. Derived data tables: CC BY 4.0. Manuscript text: all rights reserved
pending publication.

## Citation

See `CITATION.cff`. Archived at Zenodo under the concept DOI **10.5281/zenodo.23852908**, which always resolves to the latest released version.
