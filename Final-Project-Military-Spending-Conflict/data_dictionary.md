# Data Dictionary

## integrated_data.csv

Primary output file produced by integrating SIPRI, World Bank, and ACLED datasets. Each row represents one country for one year (2018-2024).

| Column | Type | Description |
|--------|------|-------------|
| country | string | Country name |
| year | integer | Year of observation (2018-2024) |
| milex_constant_usd_m | float | Military expenditure in constant 2024 USD millions (SIPRI) |
| milex_share_gdp | float | Military expenditure as a share of GDP in percent, e.g. 0.835 means 0.835% (SIPRI) |
| sipri_available | integer | 1 if SIPRI data is available for this country-year, 0 otherwise |
| country_code | float | ISO 3166-1 alpha-3 country code (World Bank); NaN where World Bank data is unavailable |
| wb_milex_pct_gdp | float | Military expenditure as a share of GDP in percent, e.g. 1.16 means 1.16% (World Bank) |
| worldbank_available | integer | 1 if World Bank data is available for this country-year, 0 otherwise |
| total_events | float | Total number of conflict events recorded (ACLED); NaN where ACLED data is unavailable |
| total_fatalities | float | Total number of fatalities from conflict events (ACLED); NaN where ACLED data is unavailable |
| total_pop_exposure | float | Total population exposed to conflict events (ACLED); NaN where ACLED data is unavailable |
| battles | float | Number of battle events (ACLED) |
| explosions_remote_violence | float | Number of explosion and remote violence events (ACLED) |
| protests | float | Number of protest events (ACLED) |
| riots | float | Number of riot events (ACLED) |
| strategic_developments | float | Number of strategic development events (ACLED) |
| violence_against_civilians | float | Number of violence against civilians events (ACLED) |
| acled_available | integer | 1 if ACLED data is available for this country-year, 0 otherwise |
| gdp_pct | float | Combined GDP percent in same units as milex_share_gdp. SIPRI value, filled with World Bank where missing |
| nato_2pct_threshold | integer | 1 if gdp_pct is at or above 2.0, 0 otherwise |
| conflict_zone | string | Conflict classification assigned during integration: Other, Russia-Ukraine War, Nagorno-Karabakh, Central Asia |

---

## acled_clean.csv

Cleaned and aggregated ACLED conflict event data. Each row represents one country for one year.

| Column | Type | Description |
|--------|------|-------------|
| country | string | Country name |
| year | integer | Year of observation (2018-2024) |
| total_events | integer | Total conflict events recorded |
| total_fatalities | integer | Total fatalities from conflict events |
| total_pop_exposure | float | Total population exposed to conflict events |
| battles | integer | Number of battle events |
| explosions_remote_violence | integer | Number of explosion and remote violence events |
| protests | integer | Number of protest events |
| riots | integer | Number of riot events |
| strategic_developments | integer | Number of strategic development events |
| violence_against_civilians | integer | Number of violence against civilians events |

---

## sipri_clean.csv

Cleaned SIPRI military expenditure data. Each row represents one country for one year.

| Column | Type | Description |
|--------|------|-------------|
| country | string | Country name |
| year | integer | Year of observation (2018-2024) |
| milex_constant_usd_m | float | Military expenditure in constant 2024 USD millions |
| milex_share_gdp | float | Military expenditure as a share of GDP in percent, e.g. 0.835 means 0.835% |

---

## worldbank_clean.csv

Cleaned World Bank military expenditure data. Each row represents one country for one year.

| Column | Type | Description |
|--------|------|-------------|
| country_name | string | Country name |
| country_code | string | ISO 3166-1 alpha-3 country code |
| year | integer | Year of observation (2018-2024) |
| wb_milex_pct_gdp | float | Military expenditure as a share of GDP in percent, e.g. 1.16 means 1.16% |