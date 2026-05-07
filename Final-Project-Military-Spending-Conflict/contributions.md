## Connor Slattery

For the final project I handled all data gathering, cleaning, integration, analysis, and documentation.

### Data Cleaning & Integration

I loaded all three raw datasets and built a cleaning process for each:

- **ACLED** filtered to 2018-2024, dealt with missing values in `POPULATION_EXPOSURE` and `ADMIN1`, standardized country names across sources, and combined weekly event records into yearly totals per country with event types split into their own columns
- **SIPRI** wrote a custom parser to handle the multi-sheet Excel layout, automatically find the header row, convert from wide to long format, drop summary rows for whole regions, and replace special missing value codes with `NaN`
- **World Bank** reformatted and filtered down to the Europe and Central Asia country list

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

## Jessica Zheng

For the final project I focused mainly on creating visualizations, helping interpret results, and supporting the analysis and write-up.

### Visualizations

I worked with the cleaned and integrated dataset to create and refine the project’s visual outputs. My main contribution was turning the analysis results into clear figures that help explain the patterns in military spending and conflict intensity.

- **Correlation matrix heatmap** showing relationships between key variables like military spending, GDP share, conflict events, and fatalities  
- **Event type breakdown plots** visualizing how different types of conflict events vary across countries and regions  
- **Multi-country time series plots** showing how conflict intensity changes over time across selected countries  
- **Ukraine time series plot** highlighting the sharp increase in conflict events, fatalities, and spending after 2022  
- **Conflict intensity heatmaps** showing variation across countries and years in a structured visual format  
- **Regression scatter plots** (including log-scale versions) showing relationships between military spending and conflict outcomes  
- **Structural break visualizations** comparing pre-2022 vs post-2022 trends in both spending and conflict  
- **K-Means clustering plot** showing how countries group together based on spending, GDP share, conflict events, and fatalities  

After generating the plots, I refined them to improve readability and clarity. This included adjusting axis labels, fixing scaling issues (especially for extreme values like Ukraine), improving color choices, and making sure each figure clearly matched the part of the analysis it supported.

### Results Interpretation

I helped interpret the visual results and connect them to the statistical findings. This included identifying key patterns such as the strong spike in conflict intensity after 2022, the clear outlier behavior of Ukraine, and general differences between high- and low-conflict countries.

For the clustering results, I helped review how countries were grouped and supported labeling the clusters in a way that made them easier to understand (for example, low conflict/low spending vs high conflict/high spending groups). I also helped ensure that the visual patterns matched what was found in the regression analysis so the results were consistent across methods.

### Analysis Support

While I did not build the main modeling pipeline, I supported the analysis by reviewing outputs and making sure the results were correctly reflected in the visualizations. I also helped check that figures matched the correct variables, time periods, and model outputs, especially for comparisons like pre-2022 vs post-2022 analysis.

### Documentation Support

I contributed to writing and editing parts of the final report, especially the sections explaining the visualizations and findings. I helped improve clarity, make the narrative easier to follow, and ensure that the written explanations matched what was shown in the figures.

### Overall Contribution

Overall, my contribution focused on turning the analysis into clear, interpretable visuals and helping connect those visuals back to the statistical results. I made sure the figures were readable, consistent, and useful for explaining the main findings of the project.

## Jessica Zheng

For the final project I was responsible for creating all visualizations, contributing to parts of the analysis, and writing the majority of the README/report.

### Visualizations

I created all of the project’s visualizations using the cleaned and integrated dataset. My focus was on turning the analysis outputs into clear and interpretable figures that directly support the research questions and findings.

- Correlation matrix heatmap showing relationships between key variables such as military spending, GDP share, conflict events, and fatalities  
- Event type breakdown plots showing differences in conflict event categories across countries and regions  
- Multi-country time series plots showing how conflict intensity changes over time  
- Ukraine-focused time series plot highlighting the sharp post-2022 increases in conflict events, fatalities, and military spending  
- Conflict intensity heatmaps showing variation across countries and years  
- Structural break visualizations comparing pre-2022 and post-2022 trends  

For all figures, I refined formatting and presentation to improve readability, including adjusting labels, fixing scaling issues (especially for extreme values like Ukraine), and improving overall consistency across plots.

### Analysis Support

I contributed to parts of the analysis by helping interpret outputs and supporting the connection between results and visualizations. While I did not implement the regression models or K-Means clustering, I helped review outputs and ensured that key patterns were correctly reflected in the figures and written explanations.

This included helping validate that trends observed in the data matched the statistical outputs, and making sure the interpretation of results (especially the post-2022 structural changes) was consistent across all sections.

### Documentation (README / Report)

I wrote the majority of the final README/report, including structuring the document, writing the narrative sections, and connecting the data, analysis, and visualizations into a coherent story.

This included:
- Organizing the overall report structure (summary, data profile, methods, findings, etc.)  
- Writing and refining explanations of datasets and preprocessing steps  
- Describing key findings and linking them to visual and statistical results  
- Ensuring consistency in tone, formatting, and terminology across sections  
- Editing and polishing content to improve clarity and readability  

I also helped ensure that the report clearly explained the workflow from raw data to final results, so that the project is reproducible and easy to follow.

### Overall Contribution

Overall, my main contributions were creating all project visualizations and writing the majority of the README/report. I also supported analysis interpretation and helped ensure that results were clearly communicated and consistently presented across the full project.