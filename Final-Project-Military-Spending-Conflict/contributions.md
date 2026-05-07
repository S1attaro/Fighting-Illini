## Connor Slattery

For the final project I handled all data gathering, cleaning, integration, analysis, and documentation.

### Data Cleaning & Integration

I loaded all three raw datasets and built a cleaning process for each:

- **ACLED** — filtered to 2018-2024, dealt with missing values in `POPULATION_EXPOSURE` and `ADMIN1`, standardized country names across sources, and combined weekly event records into yearly totals per country with event types split into their own columns
- **SIPRI** — wrote a custom parser to handle the multi-sheet Excel layout, automatically find the header row, convert from wide to long format, drop summary rows for whole regions, and replace special missing value codes with `NaN`
- **World Bank** — reformatted and filtered down to the Europe and Central Asia country list

From there I merged all three into `integrated_data.csv` on a shared country and year key, manually adding USA and Canada to the country list where they were missing. I also added new columns for `gdp_pct`, `nato_2pct_threshold`, and `conflict_zone`, and checked the results against known values for countries like Ukraine.

### Analysis (Section 7)

I wrote all the modeling code:

- **Pooled OLS** with one-year lagged spending and GDP share predicting conflict events (R² = 0.665, n = 256), plus a follow-up check dropping Ukraine (R² = 0.494)
- **Fatalities model** strong overall (R² = 0.730) but heavily Ukraine-driven, dropping to 0.086 without it
- **Spending growth regression** using year-over-year percent change as the predictor (R² = 0.318)
- **Pre/post-2022 structural break** split the sample at 2022 and compared model fit (pre R² = 0.212, post R² = 0.711), showing the war roughly tripled predictive power across the region
- **K-Means clustering** with `StandardScaler` and four clusters across average spending, GDP share, conflict events, and fatalities, with a scatter plot with key countries labeled
- Log-scale regression scatter plot colored by conflict zone

### Documentation

Wrote `data_dictionary.md` covering all four output files and 21 variables, `metadata.json`, `requirements.txt`, `run_all.py`, `check_integrity.py`, `checksums.md`, and `LICENSE`. Also wrote the majority of the status report.