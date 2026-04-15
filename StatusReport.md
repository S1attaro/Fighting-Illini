# Status Report: Conflict Intensity & Military Spending in Europe and Central Asia

**IS 477 - Data Management, Curation, and Reproducibility**  
**Team:** Connor Slattery & Jessica Zheng  
**Repository:** [S1attaro/Fighting-Illini](https://github.com/S1attaro/Fighting-Illini)  
**Report Date:** April 14, 2025

---

## Task Updates

### 1. Team Setup
**Status: Completed**

We set up the GitHub repo and the Canvas group in February. Both of us have access to the repo and have been committing our work throughout the project.

---

### 2. Project Plan
**Status: Completed**

We submitted the project plan on March 12. It has our research questions, dataset descriptions, roles, and original timeline. Nothing major has changed from it.

---

### 3. Data Acquisition
**Status: Completed**

All three datasets are downloaded and stored in the repo:

- **ACLED** - conflict event data for Europe and Central Asia, updated through March 28, 2026. About 118,000 rows and 61 countries. Requires a free account to download from their website.
- **SIPRI** - military spending data from 2017 to 2025 in an Excel file with multiple sheets. Free to download, no account needed.
- **World Bank** - military spending as a percent of GDP from 1960 to 2024. Comes as a ZIP file with a few CSVs inside.

---

### 4. Storage Setup (requirements.txt)
**Status: In Progress**

We have not committed a requirements.txt file yet. The notebook uses pandas, numpy, matplotlib, seaborn, and openpyxl. We are going to get this done before we start the Snakemake workflow so the project can run on any machine.

---

### 5. Data Profiling
**Status: Completed**

We went through all three datasets before doing any cleaning to see what we were working with.

For ACLED, most columns looked fine. The `POPULATION_EXPOSURE` column had about 15,000 missing values and a few rows were missing their region label. The most common event type is Protests, then Strategic Developments, then Explosions/Remote Violence. Ukraine has way more events than any other country in the dataset.

For SIPRI, we noticed that the Excel file has extra rows for whole regions like "Eastern Europe" mixed in with the actual countries. Missing values were also written as `...` or `xxx` instead of just being blank cells.

For the World Bank data, each year is its own column, so we knew we would have to reshape it before we could merge it with anything.

---

### 6. Data Cleaning
**Status: Completed**

All three datasets are cleaned. All the code for this is in [`Cleaned_Merged.ipynb`](https://github.com/S1attaro/Fighting-Illini/blob/main/Cleaned%2BMerged.ipynb).

**ACLED:** We filtered to just 2018 to 2024, which cut the dataset from about 118,000 rows down to about 95,000. We filled in the missing `POPULATION_EXPOSURE` values with 0 and the missing region labels with "Unknown." We also had to fix some country names to match the other datasets. For example ACLED says "Russia" but SIPRI says "Russian Federation," so we updated those. Then we grouped everything by country and year so each row is one country for one year, with totals for events, deaths, and each event type. This was saved as `acled_clean.csv`.

**SIPRI:** The header row in the Excel file is not at the top. There are a few rows of notes above the actual data. We wrote a function that finds where the real header is, reads the file from there, removes the regional rows, and reshapes it from wide to long format. We did this for both the constant USD sheet and the percent of GDP sheet and then merged them together. This was saved as `sipri_clean.csv`.

**World Bank:** We reshaped it from wide to long format, filtered to 2018 to 2024, and renamed the value column. Saved as `wb_clean.csv`.

---

### 7. Data Merging / Integration
**Status: Completed**

After cleaning all three datasets we merged them into one file called `integrated_data.csv` inside the `processed` folder.

We used SIPRI as the base and joined the World Bank and ACLED data onto it using country and year. We added flags so we can see which country-years have data from all three sources. We made a combined `gdp_pct` column that uses the SIPRI percent of GDP value when it is available and falls back to the World Bank number when it is not.

We also added two extra columns. One is a flag for whether a country is at or above NATO's 2% of GDP spending threshold. The other is a `conflict_zone` label that marks each row as Russia-Ukraine War, Nagorno-Karabakh, Central Asia, or Other.

To double check the output we looked at Ukraine's numbers. Military spending goes from about 6.9 billion dollars in 2021 to 41.2 billion in 2022, and total conflict events go from about 8,500 to 44,600 in that same jump. That matches what we would expect so the pipeline seems to be working right.

---

### 8. Analysis & Visualizations
**Status: In Progress**

We have not finished any visualizations yet but we are working on them. We are planning to make time-series charts of military spending vs conflict events by country, a map of conflict intensity using the coordinates in ACLED, event type breakdowns for the main conflict zones, and a comparison of countries above and below the NATO 2% threshold. We want to have these done by April 21.

---

### 9. Snakemake Workflow
**Status: Not Started**

We have not started the Snakemake pipeline yet. It will automate the whole process from downloading the raw data all the way to producing the final visualizations. We are aiming to have it done by April 25.

---

### 10. Metadata and Documentation
**Status: Not Started**

The README and metadata files have not been written yet. We are planning to finish these by April 27.

---

## Updated Timeline

| Task | Original Due Date | Status | Updated Due Date |
|---|---|---|---|
| Team Setup | Feb. 17 | Completed | - |
| Project Plan | Mar. 12 | Completed | - |
| Data Acquisition | Mar. 12 | Completed | - |
| Storage Setup (requirements.txt) | Mar. 17 | In Progress | Apr. 18 |
| Data Profiling | Mar. 22 | Completed | - |
| Data Cleaning | Mar. 25 | Completed | - |
| Data Merging / Integration | Mar. 27 | Completed | - |
| Status Report | Mar. 31 | Completed | Apr. 14 |
| Analysis & Visualizations | Apr. 14 | In Progress | Apr. 21 |
| Snakemake Workflow | Apr. 21 | Not Started | Apr. 25 |
| Metadata and Documentation | Apr. 25 | Not Started | Apr. 27 |
| Final Report | Apr. 30 | Not Started | Apr. 30 |
| Final Submission | May 3 | Not Started | May 3 |

---

## Changes to the Project Plan

The main goals and research questions have not changed. A few smaller things did though.

We updated the ACLED file to the March 28, 2026 version instead of the February 21 one we originally had. It adds a little more data but does not change anything for our 2018 to 2024 window.

SIPRI's Excel format turned out to be more complicated than we expected. We had to write extra code to handle the weird header and filter out the regional rows. It was not a huge problem but it did take more time than we planned for.

We also ran into four country name mismatches between ACLED and the other datasets that we did not catch ahead of time. We fixed them during the cleaning step.

The status report ended up being submitted later than the March 31 deadline mostly because the SIPRI cleaning took longer. Because of that the visualization and Snakemake tasks got pushed back about a week.

---

## Challenges

**SIPRI's Excel file was hard to read in**
The data does not start on row 1 and region rows like "Eastern Europe" were mixed in with the country rows. We wrote a function that finds the real header row and removes the regional rows automatically.

**Country names did not match between datasets**
ACLED, SIPRI, and the World Bank all write some country names differently. For example ACLED says "Russia" but SIPRI says "Russian Federation." We compared the country lists, found the mismatches, and fixed them with replacements in the cleaning step.

**Missing values in POPULATION_EXPOSURE**
About 15,000 rows in ACLED were missing this value. We filled them with 0 so we could still aggregate the column, but we are not using it as a main variable in our analysis.

**SIPRI uses strange codes for missing data**
SIPRI writes `...` or `xxx` instead of leaving cells blank. We replaced all of those with NaN before converting the columns to numbers.

---

## Individual Contributions

### Connor Slattery

For this milestone I did all of the data work in `Cleaned_Merged.ipynb`. That includes loading and profiling all three raw datasets, writing the ACLED cleaning code to filter the years, fix the nulls, standardize country names, and group everything by country and year, building the SIPRI parsing function to deal with the Excel format problems, reshaping and cleaning the World Bank file, and doing the full three-way merge into `integrated_data.csv`. I also added the `gdp_pct`, `nato_2pct_threshold`, and `conflict_zone` columns and checked the output on countries like Ukraine to make sure the numbers made sense. I committed everything to the repo and wrote most of this status report.

### Jessica Zheng

*(Jessica will add and commit her own contribution summary directly to this file in the shared GitHub repo.)*

---

*StatusReport.md - IS 477 Milestone 3*
