# Viet Nam SSB excise tax — modelling code and parameters

<!-- DOI badge -->
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23852996.svg)](https://doi.org/10.5281/zenodo.23852996)

Reproducibility package for:

> **Modest health gains and a regressive financing burden from Viet Nam's enacted
> sugar-sweetened beverage excise tax: an ex-ante modelling study**
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
| `model/vhlss.R` | Expenditure quintile profile (published VHLSS tabulations) |
| `model/audit.R` | Product-audit loader (for the protocol in the paper) |
| `model/fill_results.R` | Produces every number in the manuscript |
| `model/run_all.R` | Driver |
| `data/` | Parameters, with sources |
| `output/` | Generated results |

## Running

Requires R ≥ 4.6. No package dependencies beyond base R.

```bash
Rscript model/run_all.R            # PSA with 200 draws
PSA_N=5000 Rscript model/run_all.R # full analysis
```

Runtime for 5,000 draws: approximately 30 minutes on a laptop.

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

See `CITATION.cff`. Archived at Zenodo: **10.5281/zenodo.23852996** (concept DOI 10.5281/zenodo.23852908, which resolves to the latest version).
