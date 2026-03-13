# Project Plan: Conflict Intensity & Military Spending in the Europe and Central Asia Region

## Overview

This project looks at how military spending relates to armed conflict across Europe and Central Asia from 2018-2024. We pulled conflict event data from the Armed Conflict Location & Event Data Project (ACLED), military expenditure data from the Stockholm International Peace Research Institute (SIPRI), and military spending percentage of GDP from the World Bank to see if changes in defense budgets across varying countries line up with the frequency of conflicts occurring in the specific region, what type of events occur, and how deadly they are, both at the country level and within the specific regions themselves.

The project's main focus is on three conflict zones: the Russia-Ukraine war (2022-present), the Second Nagorno-Karabakh War between Azerbaijan and Armenia (2020), and the broader Central Asian security environment that encompasses the region. When we combine these three datasets, assess their quality and clean data to accurately build a geospatial and time-series visualizations that work as a basic open-source intelligence (OSINT) threat summary for fictional Europe and Central Area of Responsibility (AOR). The full workflow will be automated with Snakemake to keep everything reproducible and accessible to follow when directly accessed in GitHub.

---

## Our Team

| Member | Roles & Responsibilities |
|---|---|
| Connor Slattery | Acquiring Data (SIPRI, World Bank, and ACLED), data cleaning, integrating data via python, geospatial and temporal visualizations, Snakemake workflow for automation |
| Jessica Zheng | Assessing and profiling the data, its quality, statistical analysis, writing report, and the final README, metadata and data documentation of our datasets. |

Both members are responsible for the project plan, status report and the final README file. Each member will make contributions and will be responsible for submitting it via Git commit to repo at: [S1attaro/Fighting-Illini: Course Project for IS 477.](https://github.com/S1attaro/Fighting-Illini) If anything changes from roles to responsibilities, the changes will be approved by both team members mutually to fulfill the project's goals.

---

## Research Questions

**Primary Goal:** Do the changes in military spending in Europe and Central Asian countries correlate with changes in the frequency or lethality of armed conflicts and events at the country given years between 2018-2024?

**Secondary:** Which conflict event types such as: battles, explosion/missiles, or violence against civilians are the most prevalent during periods of increased military spending, and does this pattern differ between the Russia-Ukraine conflict and broader region?

**Third:** Do countries that cross NATO's required 2% GDP defense spending threshold show any measurable changes in their posture towards conflicts and activity in their immediate geographic proximity to their neighboring countries?

**Ideal Exploratory Goal:** Are there any identifiable differences between geographic clusters within Ukraine where conflict intensity is at its peak or highest? Additionally, how do those clusters shift and change over time from 2018 to 2025? Can the rise of air technology and/or drone strikes compared to formal ground battles be quantified and tracked over the course of this conflict?

Our questions are directly answered by merging ACLED weekly conflict event data and aggregate to the country year level with the SIPRI's annual military expenditure figures and World Bank percentage of GDP data, using standardized country names and year as shared identifiers. Ideally trying to find some correlation between these factors.

---

## Datasets

### Dataset 1: ACLED - Europe and Central Asia Aggregated Dataset
- **Source:** https://acleddata.com/aggregated/aggregated-data-europe-and-central-asia
- **File Name:** Europe-Central-Asia_aggregated_data_up_to-2026-02-21
- **Access Method:** Direct download of regional data files via the ACLED website after free account registration. The data is also easily accessible through their official ACLED REST API with authentication, to provide an additional access method.
- **Format:** Excel (.xlsx), converted to CSV for processing
- **Size:** 117,001 rows & 13 columns
- **Coverage:** 61 countries across Europe and Central Asia; weekly aggregated records from Dec. 2017 - Feb. 21, 2026

### Dataset 2: SIPRI Military Expenditure Database
- **Source:** https://milex.sipri.org/sipri
- **File Name:** SIPRI-Milex-data-2017-2025
- **Access Method:** Direct Excel download from the SIPRI's website. No account or verification required to download.
- **Format:** Excel (.xlsx) with multiple sheets: Constant (2024) US$, Current US$, Share of GDP, Per Capita, Share of Government spending
- **Size:** 61 rows and 11 columns
- **Coverage:** Global; personally filtered to Europe and Central Asia countries from 2017 to 2024.

### Dataset 3: World Bank - Military Expenditure (% of GDP)
- **Source:** https://data.worldbank.org/indicator/MS.MIL.XPND.GD.ZS
- **File Name:** API_MS.MIL.XPND.GD.ZS_DS2_en_csv_v2_211
- **Access Method:** Data is distributed as a ZIP containing 3 CSV files. No account is required to access this dataset. Uses a distinct format (CSV), with a distinct originating organization, and distinct license from both ACELD and SIPRI.
- **Format:** CSV (one row per country, one column per year from 1960 to 2024), distributed with two metadata CSV files:
  - Metadata_Country_API_MS.MIL.XPND.GD.ZS_DS2_en_csv_v2_211
  - Metadata_Indicator_ API_MS.MIL.XPND.GD.ZS_DS2_en_csv_v2_211

---

## Timeline

| Task | Description | Due Date | Status |
|---|---|---|---|
| Team Setup | GitHub repo created and Canvas group formed. | Feb. 17 | Completed |
| Project Plan | Drafted and Submitted | Mar. 12 | Completed |
| Data Acquisition | ACLED, SIPRI, and World Bank files downloaded and uploaded to GitHub repo. | Mar. 12 | Completed |
| Storage setup | Create a detailed requirements.txt document | Mar 17 | Pending |
| Data Profiling | Look at the distribution of data and see any missing values in the three datasets. Flag anything that could affect the results. | Mar. 22 | Pending |
| Data Cleaning | Standardize by country names and then parse ACLED WEEK to extract YEAR; and handle any missing POPULATION_EXPOSURE; and drop any unnecessary regional subtotal rows. Reshape the World Bank CSV from wide to long. Things might change depending on overall goals. | Mar. 25 | Pending |
| Data Merging/Integration | Aggregate ACLED to country-year, left join all three datasets on country_iso + year; add sipri_available and world_bankavailable flags and then save it as a cleaned_csv file | Mar. 27 | Pending |
| Report our Project Status | Draft and submit the Status_Report.md with updated tasks or changes. Update the timeline and description of any challenges we have encountered. | March 31 | Pending |
| Analysis & Visualizations | Creating visualizations for statistical comparison and analysis. | Apr 14 | Pending |
| Snakemake workflow | Develop a pipeline for data acquisition, cleaning, data merging, and visualization so that the workflow can be reproduced automatically. | Apr 21 | Pending |
| Metadata and Documentation | Write the metadata, documentation, README, and describe the datasets and workflow used in the project. | Apr 25 | Pending |
| Final Report | Complete the paper with all steps, start to finish-introduction, research question, analysis, methods, and conclusion. | April 30 | Pending |
| Final Submission | Submit everything to the GitHub repository and check with the rubric. | May 3 | Pending |

## Constraints

It could be difficult to integrate these datasets in different formats, with information potentially collected at different times (weekly vs yearly), and it might not be easy to join by countries due to looking at different regions. These datasets, ACLED, SIPRI, and World Bank, all collect and organize data differently. We are unsure whether media or government limitations exist in the dataset that constrain the amount of data/information reported. During data downloading, we found that you have to sign into the website to get the data. ALCED has a policy on no redistribution of the raw data. Also there is nothing that explains alliance aids from different countries that contribute to those spending or not.

## Gaps

The datasets might not all use the same method of naming countries and their codes/IDs, so some cleaning/preprocessing might be needed in order to join them together. We are unsure if there is any missing data involved. The events or circumstances that led to the difference in military spending will need to be found through a manual process such as analysis.
