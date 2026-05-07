# Military Spending and Conflict Intensity in Europe and Central Asia (2018–2024)

## Authors: Conner Slattery and Jessica Zheng

---

# Project Overview

Our project looks at the relationship between military spending and event/conflict intensity through Europe and Central Asia between 2018 and 2024. We intrgrate three independent international datasets into one unified country-year dataset, consist of SIPRI military expenditure data, World Bank military spending as a percentage of Gross Domestic Product(GDP), and ACLED conflict event and fatality data.

From these sources we are looking to analyze if increase in military spending is associated with increase in higher conflict intensity, fatalities and regional instability.

In this project our process is first read in all the data, clean them, merge them, then visualizations, and analysis. We have Data acquisition/cleaning, data integration, exploratory data analysis, statistical modeling, regression model, k-means clustering and other visualizations with interpretation.

# Research Question

Does increased military spending predict higher conflict intensity across Europe and Central Asia?

We also explored how Russian-Ukraine war influence the dynamic of the region, and looking at the assosciation of NATO's 2% GDP with higher conflict issues.

# Dataset

## 1. ACLED Conflict Data

Source: https://acleddata.com/aggregated/aggregated-data-europe-and-central-asia


Description: One issue with this dataset is it has a license that does not allow sharing of the dataset from the website, so this link will only go to access denied page. We have a downloaded of this data in our folder included in the final project commit. This dataset includes weekly conflict events/fatalities, and annual country-level observations aggregated.

Variables that we use are EVENTS, FATALITIES, EVENT_TYPE, and POPULATION_EXPOSURE.

## 2. SIPRI Military Expenditure Dataset

Source: https://doi.org/10.55163/CQGC9685

Description: The dataset include military spending all the way to 2024, having military spending shown as percentage of GDP, and country-level observations on a annual level.

Variables that we use are milex_constant_usd_m, and milex_share_gdp.

## 3. World Bank Military Expenditure (% GDP)

Source: https://data.worldbank.org/indicator/MS.MIL.XPND.GD.ZS

Description: This dataset includes military spending as percentage of GDP, this data is used to supplement the missing SIPRI observations, and include the USA/Canada observations that SIPRI dataset lacks.

The variables we used is wb_milex_pct_gdp.

# Our final project folder structure

Fighting-Illini
├── Final-Project-Military-Spending-Conflict
|
│   ├── data/
|       |── API_MS.MIL.XPND.GD.ZS_DS2_en_csv_v2_211.csv
|       |── Europe-Central-Asia_aggregated_data_up_to_week_of-2026-03-28.xlsx
|       |── SIPRI-Milex-data-2017-2025.xlsx
|
│   ├── figures/
|       |── correlation_matrix.png
|       |── event_type_breakdown.png
|       |── heatmap_conflict.png
|       |── kmeans_clusters.png
|       |── multi_country_conflict_trends.png
|       |── regression_scatter.png
|       |── structural_break.png
|       |── ukraine_time_series.png
|
|  |── processed/
│       ├── acled_clean.csv
│       ├── sipri_clean.csv
│       ├── worldbank_clean.csv
│       |── integrated_data.csv
│
├── check_integrity.txt
├── data_dictionary.md
├── IS477_Final_Project.ipynb
├── LICENSE
├── metadata.json
├── README.md
├── requirements.txt
└── run_all.py

# Methods

## Data Cleaning

### ACLED
Filtered the observations to 2018-2024, cleaned and filled missing values in POPULATION_EXPOSURE, and ADMIN1. Aggregated weekly conflict observation to country-year. And put event types in their seperate columns.

### SIPRI
Converted the data from wide-formate to long format, removed the regional aggregate rows, standardize the names for the countries, and converted the military spending variables to numeric.

### World Bank
Filered the data for only Europe and Central Asia, made yearly values to long format, helped supplement the missing GDP-share values.

# Data Integration
We merged data using country and year. We created unified country-year spine, added in the missing USA and Canada data, made derived variables: gdp_pct, nato_2pct_threshold, and conlict_zone.

Our final dataset consists of 408 observations for 62 countries and 21 variables.

# Visualization

The visualizations we have are:Ukraine military spending vs conflict events, multi-country conflict trends, event type breakdown by conflict zone, correlation matrix, conflict intensity heatmap, lagged regression scatterplot, k-Means clustering visualization, structural break comparison before/after 2022. All figures are also in figures/ folder.

# Statistical Analysis

We estimate pooled OLS regressions using lagged military spending variables. In our main model we have total conflict event (Dependent Variable), and lagged military spend + lagged military spending as % GDP for predictors, and extra models of fatalities regression, spending growth regression, pre and post 2022 structural break analysis.

# Machine Learning

We used K-Means clustering and group coutnries into four clusters using average military spending, average GDP spending share, average conflict events, and average fatalities. The clusters we identified were low spending low conflict, mid spending with elevated conflict, high spending with moderate conflict, and in Ukraine's case extreme conflict.

# Key Findings

Throughout the whole project it is clearly shown with Ukraine as the noticeable country or structural outlier. Because Ukraine has the highest spike in both military spending and conflict intensity after 2022 highly likely due to the Russian-Ukraine war. Our lagged regression model shows that military spending does significantly predict future conflict events(R² = 0.665, p < 0.001 for both predictors). The Russian-Ukraine War influenced regional dynamics showing the strengthened relationship between spending and conflict after 2022(pre-2022 model R² = 0.212, post-2022 model R² = 0.711). There is a pattern that NATO 2% countries does experience higher conflict exposure, these countries that are on the benchmark experience higher conflict intensity and increase their military spending with it. 

# Reproducibility

Run the IS477_Final_Project_ipynb

# Requirements

In the requirements.txt it includes all the versions we have for the libraries: pandas, numpy, matplotlib, seaborn,statsmodels, scikit-learn, openpyxl, jupyter.

# Limitations

Of course we only have correlations and that does not imply causation. There is likely to exist possible reverse casualties. Our regression model might be heavily influenced by the Ukraine data, and ACLED stores reported events which means there might not include all real-world conflict events.

# Future Improvements

We could add in more extensions with per-capita military spending normalization, looking more into NATO memberships, having geospatial visualizations and seeing if we can forcast conflict instensity using the time-series method.

# License

This project use is for IS 477.