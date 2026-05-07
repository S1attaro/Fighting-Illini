# Military Spending and Conflict Intensity in Europe and Central Asia (2018–2024)

## Contributors: Conner Slattery and Jessica Zheng

---

# Summary

Our project looks at the relationship between military spending and event/conflict intensity through Europe and Central Asia between 2018 and 2024. Our motivation for this project was a uniformed interest in military spending and the changes in world conflict around this time era. And in this time frame the major geopolitical changes that occured in this period was the escalation fo the Russian-Ukrain war in 2022. This led to the increase in military expenditures among many European and NATO countries for support of the war. Governments accross the region have drastically increase the defense budget from the rising security concerns, and preparation for potential issues that this period seems most useful to examine whether military spending patterns are associated with increase of higher level of conflict activities.

We intrgrate three independent international datasets into one unified country-year dataset, consist of SIPRI military expenditure data, World Bank military spending as a percentage of Gross Domestic Product(GDP), and ACLED conflict event and fatality data. To look into our research question of: Does increased military spending predict higher conflict intensity across Europe and Central Asia? We also explored how Russian-Ukraine war influence the dynamic of the region, and looking at the assosciation of NATO's 2% GDP with higher conflict issues. From these sources we are looking to analyze if increase in military spending is associated with increase in higher conflict intensity, fatalities and regional instability.

The first dataset comes from ACLED (Armed Conflict Location & Event Data), which gives us the detailed conflict event and datality data information that range across Europe and Central Asia. Our next dataset is the SIPRI (Stockholm International Peace Research Institute), which includes annual military expenditure values measured in constant U.S. dollars and military spending as a percentage of GDP. And the last dataset comes from the World Bank and supplements military expenditure as a percentage of GDP for countries with missing observations in SIPRI, particularly for the United States and Canada.

Our project workflow consist of several stages such asL data acquisition, integrity vertification, cleaning, integration + merging, exploratory analysis, statistical modeling, visualization, and reproducibility automation. First we cleaned each of the datasets by themselves to standardize country names, filtering years, converting variables into consistent formats, handling missing values, and restructuring the datasets into a common country-year format. We then merged all the datasets together using the country and year in order to create a unified dataset that allow for better analysis in the later steps. The dataset contains 408 observations for 62 countries and 21 variables.

After the data integration part we conducted data analysis and produced multiple visualizations to identify trends and patterns. Our visualizations ranges from conflict intensity heatmaps, correlation matrices, event-type distributions, regression scatterplots, multi-country conflict trend graphs, structural break comparisons, and Ukraine-specific time series plots. We also applied statistical analysis using pooled OLS (Ordinary Least Squares) regression models with lagged military spending variables to interpreate predictive relationships between military expenditure and conflict intensity. Additionally, we used the K-Means clustering to cluster countries into groups from their average military spending, conflict events, fatalities, and military expenditure as a percentage of GDP, since these are common columns that these datasets share.

From our findings we see a pattern of strong association between military spending and conflict intensity during war tension periods. Clearly shown was Ukraine rising as a significant structural outlier after 2022 due to the sharp increase in both military expenditure and conflict events following the Russian invasion. The regression analysis shown that lagged military spending variables significantly predicted future conflict events, with stronger relationships observed after 2022. Countries who are meeting the benchmark for NATO’s 2% GDP also tended to experience greater conflict exposure on average.

Although our analysis does identify patterns of significant correlation between military spending and conflict intensity, the project cannot establish causation for it. Increased military spending could be result from conflict risk instead of directly causing conflict. Either way, our project shows how integreated international datasets(ACLED, SIPRI and world bank) can be combined using shared columns informaiton to look at regional security dynamics and provide a reproducible workflow for future geopolitical and conflict analysis research.


# Data Profile

## 1. ACLED Conflict Data

Source: https://acleddata.com/aggregated/aggregated-data-europe-and-central-asia

Description: The ACLED (Armed Conflict Location & Event Data) dataset contains conflict-related observations for Europe and Central Asia. The dataset includes weekly event-level information documenting protests, battles, violence against civilians, riots, and other forms of political violence. One issue with this dataset is it has a license that does not allow sharing of the dataset from the website, so this link will only go to access denied page. We have a downloaded of this data in our folder included in the final project commit. This dataset also includes annual country-level observations aggregated.

Repository Location - data/Europe-Central-Asia_aggregated_data_up_to_week_of-2026-03-28.xlsx

The before cleaning dataset includes weekly observations aggregated by country and administrative region. Some important variables that we used in this project are: EVENTS(The total number of conflict events recorded), DATALITIES(The number of fatalities associated with events), EVENT_TYPE(What type of conflict events it is), POPULATION_EXPOSURE(The estimated amount of population that was affected from the conflict), COUNTRY, YEAR, ADMIN1.

Some data characteristics are that the dataset covers multiple countries and range across years. Having both numeric + categorical variables and also some missing values in some administrative and exposure-related fields. Because ACLED data are reported observed conflict events, there may be bias and issue of underreporting or not all conflicts are reported in areas with limited resource for reporting, or not accessible from active war zones. 

Some of the Ethical and Legal Considerations are that ACLED data is on a restricted-use license. There is a limit for redistribution permission and for ethical usage we need to comply with ACLED's term of use. Conflict datasets may also contain politically sensitive information and should be interpreted carefully to avoid misleading conclusions or oversimplifying geopolitical conflicts.

This dataset provides the primary measures of conflict intensity used throughout the project, including event counts and fatalities. These variables are essential for evaluating whether increased military spending is associated with higher levels of instability and violence.

## 2. SIPRI Military Expenditure Dataset

Source: https://doi.org/10.55163/CQGC9685

Description: The dataset include military spending all the way to 2024, having military spending shown as percentage of GDP, and country-level observations on a annual level.SIPRI is widely considered one of the most authoritative sources for international military expenditure statistics.

This dataset originally has a wide formate where years are represented as columns. Some of the important variables we use are milex_constant_usd_m(Military expenditure in constant million USD), milex_share_gdp(Military expenditure as a percentage of GDP), Country, Year.

Some of the characteristics of this dataset is that this data spans multiple decades and includes annual observations for nearly all sovereign states. Some missing values exist for smaller countries or territories, and country naming conventions occasionally differ from other datasets.

Our ethical and legal considerations for this dataset isn't that much since SIPRI data is publicly accessible for academic and research use. Proper citation is required. Since military expenditure data can influence political interpretations, users should avoid drawing unsupported causal conclusions.

This dataset is relevant for our research question since it provides the primary independent variables used in the regression models and clustering analysis. Military expenditure trends are central to evaluating how defense spending relates to conflict intensity.

## 3. World Bank Military Expenditure (% GDP)

Source: https://data.worldbank.org/indicator/MS.MIL.XPND.GD.ZS

Description: This dataset includes military spending as percentage of GDP, this dataset was used primarily to supplement missing SIPRI observations, and include the USA/Canada observations that SIPRI dataset lacks.

The repositort for this dataset is data/API_MS.MIL.XPND.GD.ZS_DS2_en_csv_v2_211.csv

The structure of the original dataset has yearly values in wide format. Some of the important variables are Country Name, Country Code, Year, and wb_milex_pct_gdp.

Some characteristics of this dataset is that it is highly structured and standardized but required reshaping into long format for integration. Missing observations occur in some years and countries.

There is not much ethical and legal considerations we worry about this dataset because World Bank data is open access and intended for public research and policy analysis. Users should still provide appropriate citation and attribution.

For our research question this dataset improved data completeness and ensured that military spending as a percentage of GDP could be consistently analyzed across all countries in the final integrated dataset.

# Data Quality

We conducted a comprehensive data quality assessment across all three datasets (ACLED, SIPRI, and World Bank) prior to integration. The goal of this assessment was to ensure that the final merged dataset would be reliable, internally consistent, and suitable for statistical analysis and machine learning tasks. Our evaluation focused on the standard dimensions of data quality: completeness, consistency, validity, uniqueness, accuracy, and structural compatibility across sources. In addition, we explicitly considered domain-specific challenges such as geopolitical reporting bias, differences in temporal resolution, and inconsistencies in country definitions across datasets.

## ACLED Data Quality Assessment

The ACLED dataset presented the most significant data quality challenges due to its granular, event-based structure and its reliance on conflict reporting systems. One of the primary issues identified was missing data in key variables, particularly POPULATION_EXPOSURE and ADMIN1. These missing values are not uniformly distributed across countries or time periods, which introduces potential bias.

Another major concern was variability in reporting intensity across countries and time. ACLED records are based on reported conflict events, which means that observed differences may reflect differences in reporting capacity rather than true differences in conflict levels. This introduces a form of measurement bias that affects comparability across countries. For instance, countries with strong media coverage and institutional reporting systems may appear to have higher conflict intensity than similarly affected regions with weaker reporting systems.

A particularly important issue was the presence of extreme outliers, most notably Ukraine after 2022. Following the escalation of the Russia–Ukraine war, Ukraine exhibits a dramatic increase in both conflict events and fatalities. While this is a valid reflection of real-world conditions, it creates statistical challenges such as skewing distributions, influencing regression coefficients disproportionately, and affecting clustering stability. We retained these observations because they are substantively meaningful, but we acknowledge their strong influence on downstream analysis.

Additionally, ACLED data required careful inspection for structural consistency, particularly in event categorization. Event types were not always uniformly coded across all observations, requiring standardization before aggregation. After cleaning, we aggregated weekly event-level data into country-year summaries to align with the temporal structure of the other datasets.

## SIPRI Data Quality Assessment

The SIPRI military expenditure dataset is generally considered a high-quality and authoritative source; however, it still required substantial preprocessing. One key issue was inconsistent country naming conventions, which differed from both ACLED and World Bank datasets. 

Another major issue was the presence of non-country aggregate rows, such as regional or global totals (e.g., “Europe,” “World”). These rows had to be removed because they do not represent valid observational units for country-level analysis. Failure to remove these entries would have introduced duplication and aggregation bias in the final dataset.

We also identified missing values and placeholders in military expenditure variables, particularly in earlier years or for smaller states. In some cases, values were recorded as blanks or nonnumeric symbols, requiring conversion to proper missing value indicators (NaN) before analysis.

The dataset also required structural transformation, as it was originally formatted in a wide structure with years as separate columns. This format is not suitable for panel data analysis or integration with other datasets, so we reshaped it into a long format with explicit country-year observations.

Despite these issues, SIPRI remains highly reliable in terms of measurement validity, as military expenditure estimates are carefully constructed using standardized international methodologies. The primary challenges were therefore structural rather than conceptual.

## World Bank Data Quality Assessment

The World Bank dataset on military expenditure as a percentage of GDP was generally the cleanest of the three datasets. It demonstrated strong consistency and standardization, with clearly defined variables and uniform formatting across countries. However, it still required preprocessing to align with the structure of the integrated dataset.

The most significant issue was the dataset’s original wide format structure, where each year was represented as a separate column. This required transformation into a long format to enable merging with SIPRI and ACLED data. During this process, we ensured that no data was lost or misaligned.

Another limitation was missing observations for certain countries and years, particularly for smaller or less economically developed states. While these missing values were relatively limited compared to ACLED, they still contributed to uneven coverage across the final dataset.

We also verified that country identifiers were consistent with the other datasets. While World Bank country naming conventions are generally standardized, minor differences still required harmonization during the integration process.

## Cross-Dataset Quality Assessment

A major component of our data quality assessment involved evaluating cross-dataset compatibility. Because the project relies on integrating three independent sources, ensuring consistency across them was critical.

We performed systematic comparisons of country coverage and identified discrepancies where certain countries appeared in one dataset but not others. These discrepancies were resolved through standardization, filtering, and, when necessary, exclusion of non-overlapping entities.

We also ensured temporal alignment, confirming that all datasets covered a consistent time range (2018–2024). While ACLED provided weekly granularity and SIPRI/World Bank provided annual data, we harmonized all datasets to the country-year level to ensure comparability.

A key challenge was ensuring uniqueness of observations after integration. We validated that each country-year combination appeared only once in the final dataset, preventing duplication errors that could bias statistical results.

Additionally, we conducted statistical validation checks, including summary statistics, correlation analysis, and outlier detection. These checks helped identify anomalies such as extreme values, unexpected zeros, or inconsistent scaling between variables.

## Overall Assessment and Limitations

Overall, the datasets were of sufficient quality for integration and analysis after appropriate cleaning and standardization. However, several important limitations remain. First, conflict data such as ACLED is inherently subject to reporting bias, meaning observed patterns may reflect differences in reporting systems rather than true underlying conflict levels. Second, military expenditure data may be influenced by differences in national accounting practices and estimation methodologies. Third, extreme geopolitical events—particularly the Russia–Ukraine war—introduce structural breaks that can dominate statistical relationships.

Despite these limitations, the combined dataset provides a robust foundation for exploratory analysis and modeling. The integration process successfully aligned three heterogeneous datasets into a coherent panel structure, enabling meaningful analysis of the relationship between military spending and conflict intensity across Europe and Central Asia.


## Data Cleaning

We did a lot fo cleaning operation for all the datasets to standardize all the columns, values and variables to improve consistency, reduce errors, and prepare the data for integration and analysis.

### ACLED

For the ACLED dataset, we filtered the observations to 2018-2024, cleaned and filled missing values in POPULATION_EXPOSURE, and ADMIN1 from imputation and standarization procedures. Weekly observations were aggregated into country-year summaries using grouped totals for events and fatalities. Event types were pivoted into separate columns to support later visualization and clustering analysis.

### SIPRI

Converted the data from wide-formate to long format, removed the regional aggregate rows, standardize the names for the countries, and converted the military spending variables to numeric.

### World Bank

Filered the data for only Europe and Central Asia, made yearly values to long format, we retained only variables necessary for military expenditure percentage calculations. Missing observations were preserved when appropriate to avoid introducing artificial estimates.

### Integration Cleaning
We merged data using country and year. We created unified country-year spine, added in the missing USA and Canada data, made derived variables: gdp_pct, nato_2pct_threshold, and conlict_zone. We validated the integrated dataset by checking row counts, duplicates, missingness, and datatype consistency. Final outputs were exported as cleaned CSV files to the /processed directory.

# Findings

Across the integrated dataset, several consistent patterns emerge that help describe how military expenditure and conflict intensity interact in Europe and Central Asia between 2018 and 2024. While the relationships we observe are not strictly causal, the results do show clear associations that become especially pronounced during periods of geopolitical instability.

The most striking feature in the data is the role of Ukraine after 2022. Following the escalation of the Russia–Ukraine war, Ukraine shifts from being an ordinary observation within the dataset to a major structural outlier. Both military expenditure and conflict indicators increase sharply and simultaneously. This is visible across multiple visualizations, where spikes in conflict events and fatalities align closely with substantial increases in defense spending. This co-movement is important because it suggests that large-scale conflicts can rapidly reshape both sides of the relationship: spending increases in response to conflict, while conflict intensity is simultaneously captured through reported events and fatalities.

The regression analysis provides additional structure to these patterns. Using pooled OLS models with lagged military spending variables, we find that military expenditure is a statistically significant predictor of future conflict events. In the main specification, both military spending in constant USD and military spending as a percentage of GDP are significant, and the model achieves an R² of 0.665. This suggests that a meaningful portion of variation in conflict intensity can be explained by past levels of military spending, although the direction of influence is not straightforward. It is more likely that military spending reflects underlying security conditions rather than directly driving conflict outcomes.

When the data is split into pre-2022 and post-2022 periods, the relationship becomes noticeably stronger in the latter period. Before 2022, the model explains relatively little variation in conflict intensity. After 2022, however, explanatory power increases substantially, and coefficients become more stable and significant. This structural break highlights how sensitive the relationship is to major geopolitical shocks, particularly the Russia–Ukraine war, which reshaped both regional security dynamics and defense budgets.

The clustering analysis further supports these patterns by grouping countries based on average military spending, GDP share of military expenditure, conflict events, and fatalities. Most countries fall into relatively stable clusters characterized by low or moderate spending and low conflict exposure. A smaller group of countries shows elevated conflict and higher spending levels, often reflecting regional tensions or security concerns. Ukraine, however, consistently forms its own cluster due to extreme values across all conflict-related variables, reinforcing its role as a distinct case within the dataset.

We also examined NATO’s 2% GDP spending benchmark as a reference point for comparing countries. Countries meeting or exceeding this threshold tend to show higher average conflict exposure, but this pattern should be interpreted carefully. Rather than indicating that higher military spending leads to conflict, it is more plausible that countries facing greater perceived threats increase their defense budgets in response.

Overall, the findings suggest a strong association between military spending and conflict intensity, but the relationship is heavily shaped by external shocks and reactive policy behavior rather than simple linear causation. The combination of regression analysis, clustering, and visualization consistently points to the importance of context, particularly the post-2022 geopolitical environment, in shaping both spending patterns and conflict outcomes.

# Future Work

There are a number of ways this project could be improved and extended. Right now, the analysis gives a useful overview of how military spending and conflict intensity are related across Europe and Central Asia, but it mainly shows patterns and correlations. It doesn’t fully explain cause-and-effect, and it also leaves out a lot of real-world factors that could make the results more complete.

One important next step would be to improve how we handle causality. In the current project, we use regression with lagged military spending, which helps a bit with timing, but it still doesn’t solve the bigger issue that conflict and military spending influence each other. Countries often increase military budgets because conflict is already happening or expected. A better approach in the future would be to use methods like fixed-effects models, which would let us control for things that are unique to each country but don’t change much over time. Another option would be difference-in-differences analysis, especially to study big events like the Russia–Ukraine war and compare countries that were directly affected to those that were not.

Another improvement would be to use more detailed time data. In this project, everything was simplified to yearly data so that all three datasets could be combined. This makes the analysis easier, but it also hides short-term changes. Conflict data, especially from ACLED, is available at a much more detailed level (like weekly or monthly). If future work kept that detail, it could show how quickly changes in military spending respond to rising conflict, or wether conflict spikes come before or after spending increases in a more precise way.

We could also improve the project by adding more variables. Right now, we mainly focus on military spending and conflict events, but real-world conflict is influenced by many other factors. Adding things like political stability, government type, sanctions, refugee flows, or economic conditions like inflation and energy dependence would give a fuller picture. It would also help explain why some countries spend more on defense without necessarily having more conflict, or why others experience conflict without major changes in spending.

Another direction would be to look more at geography. In the current version, each country is treated separately, but in reality, conflict often spreads across borders or affects nearby countries. For example, instability in one region can cause neighboring countries to increase military spending. Future work could use maps or spatial models to better show these regional effects and how countries influence each other.
On the machine learning side, the clustering we used (K-Means) was mainly for grouping countries in a simple way. It worked well for getting a general picture, but it doesn’t capture changes over time. A next step could be using models that actually try to predict conflict levels, not just group countries. Time-series models or basic prediction models could help estimate future conflict risk based on past spending and events.

Another area for improvement is adding more data sources. While ACLED, SIPRI, and the World Bank are strong datasets, they don’t capture everything. Adding data on arms imports, sanctions, refugee movements, or military alliances could help explain the patterns we see more clearly. It would also make the dataset more complete and reduce the chance that we are missing important outside influences.

Finally, the project could be made easier to reproduce and run by others. While the current setup works, using tools like Docker or workflow systems would make it more automatic and less dependent on manual steps. This would help ensure that anyone running the project gets the same results without needing to fix environment or file issues.

Overall, the future work mostly comes down to making the analysis more detailed, more realistic, and more focused on real-world complexity. The current project gives a solid starting point, but there is a lot of room to build on it and make the results more accurate and useful.

# Challenges

This project came with a number of practical and analytical challenges, most of which came from working with real-world datasets that were not originally designed to be combined. While each dataset (ACLED, SIPRI, and the World Bank) is strong on its own, putting them together into a single consistent structure required a lot of cleaning, reshaping, and checking for errors.

One of the first challenges was data integration across very different formats. ACLED is event-level and very detailed, SIPRI is annual and focused on financial military spending, and the World Bank dataset focuses on macroeconomic indicators like military spending as a share of GDP. Because of these differences, there was no shared structure at the start. We had to convert everything into a common country-year format, which meant aggregating ACLED data, reshaping SIPRI from wide to long format, and standardizing World Bank data. This step took more time than expected because each dataset required a different approach.

A related issue was inconsistent country naming and structure. Across the three datasets, countries were not always labeled the same way. Some used slightly different spellings, some used older political names, and others included regional aggregates instead of actual countries. These inconsistencies caused problems during merging, such as missing matches or duplicated entries. We had to manually inspect and standardize country names to ensure that all datasets aligned correctly.

Another major challenge was missing and uneven data coverage. Not all countries had complete information across all years or all datasets. In some cases, SIPRI data was missing military spending values for certain countries, and in other cases ACLED had missing fields like population exposure or administrative region data. The World Bank dataset helped fill some gaps, but not all missing values could be fully resolved. We had to make decisions about whether to drop incomplete rows or retain them, depending on how important they were for the final analysis.

A particularly important challenge came from outliers and extreme values, especially Ukraine after 2022. Once the Russia–Ukraine war began, Ukraine’s conflict events, fatalities, and military spending all increased dramatically compared to every other country in the dataset. While this is a real and important part of the data, it created problems for statistical analysis. It heavily influenced regression results and made some visualizations harder to interpret because it stretched scales and dominated patterns. We had to be careful when interpreting results so that Ukraine did not distort the overall conclusions for the rest of the region.

Another challenge was ensuring reproducibility of the full workflow. The project includes multiple steps: data cleaning, integration, analysis, and visualization. Keeping all of these steps organized and making sure they run in the correct order was not always straightforward. File paths, dependencies, and execution order all had to be carefully managed. Even small issues, like missing packages or incorrect file locations, could break the pipeline. We tested the workflow multiple times to ensure it could be reproduced from start to finish without manual fixes.

Finally, there was a broader challenge around interpreting results responsibly. While the models showed clear statistical relationships between military spending and conflict intensity, these relationships are not simple or one-directional. In reality, conflict can lead to higher military spending just as much as military spending can reflect rising conflict risk. Because of this, we had to be careful not to overstate causal claims and instead focus on describing patterns and associations supported by the data.

Overall, the main difficulties came from working with messy, heterogeneous datasets and making sure the final analysis was consistent, reproducible, and correctly interpreted.

# Reproducibility

Step by step below:
1. Clone the GitHub repository.
2. Ensure that the datasets are in /data folder.
3. Install the dependencies using: pip install -r requirements.txt
4. Run the workflow script: python run_all.py
5. Open and run: IS477_Final_Project.ipynb
6. The processed dataset will be saved in /processed directory.
7. All figures and visualizations are automatically saved into /figures directory.

# References
ACLED. Aggregated Conflict Data for Europe and Central Asia. https://acleddata.com
SIPRI Military Expenditure Database. https://doi.org/10.55163/CQGC9685
World Bank Military Expenditure (% GDP). https://data.worldbank.org/indicator/MS.MIL.XPND.GD.ZS