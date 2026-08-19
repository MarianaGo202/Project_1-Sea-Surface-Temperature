**Sea Surface Temperature Anomaly Analysis**

Oceanographic data analysis of Sea Surface Temperature (SST) anomalies from 1982 to 2024, developed in Python to investigate long-term trends, temporal variability and changes in ocean temperature anomalies.

*OVERVIEW*

This project analyzes 42 years of monthly SST anomaly data using statistical analysis and data visualization.

The analysis focuses on long-term trends, annual and monthly variability, differences between historical periods, and the distribution of positive and negative anomalies.

*DATASET*

The dataset contains monthly Sea Surface Temperature anomaly observations covering 1982–2024.

Variable          | Description  
"date"             | Date of the observation  
"sst\_anomaly"| Sea Surface Temperature anomaly (K)  
"year"            | Year extracted from the observation date  
"month"         | Month extracted from the observation date  
"rolling\_12m" | 12-month rolling mean  
"period"          | Predefined time period

*ANALYSIS*

The dataset is cleaned and prepared with Pandas before the statistical analysis. Dates are converted to datetime format, year and month are extracted, and the data structure and missing values are checked.

Descriptive statistics are calculated to identify the mean, maximum and minimum SST anomalies and their corresponding dates.

Monthly observations are aggregated by year to calculate annual mean SST anomalies. These annual values are then used to estimate the long-term trend through linear regression.

The regression uses year and annual mean SST anomaly and provides the slope in K/year, R², p-value and estimated change across the study period.

A monthly climatological analysis is also performed to compare mean anomalies between calendar months. A 12-month rolling mean is calculated to reduce short-term variability and highlight longer-term patterns.

The analysis identifies the 10 years with the highest and 10 years with the lowest annual mean SST anomalies.

For period comparison, the dataset is divided into four intervals:

Period| Years  
1| 1982–1999  
2| 2000–2009  
3| 2010–2019  
4| 2020–2024

The mean anomaly is calculated for each period, and linear regression is performed separately to compare trends between intervals.

Monthly observations are also classified as positive, negative or zero anomalies, with the proportion of each category calculated.

*VISUALIZATIONS*

Monthly SST Anomaly

Monthly SST anomaly observations from 1982 to 2024\.

**"Monthly SST Anomaly" (sst\_monthly\_anomaly.png)**

Annual SST Trend

Annual mean SST anomalies together with the estimated linear trend.

**"Annual SST Trend" (sst\_annual\_trend.png)**

12-Month Rolling Mean

Monthly SST anomalies together with the 12-month rolling mean.

**"12-Month Rolling Mean" (sst\_rolling\_mean.png)**

*KEYFINDS*

The main statistical results are available in "sst\_summary.csv".

This section will contain the main findings from the analysis, including the overall trend, R², p-value, highest and lowest anomaly years, and differences between the selected periods.

*OUTPUT FILES*

File| Description  
"annual\_sst\_anomalies.csv"| Annual mean SST anomalies  
"monthly\_sst\_anomalies.csv"| Mean anomaly by calendar month  
"period\_sst\_anomalies.csv"| Mean anomaly by predefined period  
"sst\_summary.csv"| Main statistical results

*PROJECT STRUCTURE* 

projeto-1-sst/  
│  
├── CSVExport.csv  
├── analise\_sst.py  
├── README.md  
│  
├── sst\_monthly\_anomaly.png  
├── sst\_annual\_trend.png  
├── sst\_rolling\_mean.png  
│  
├── annual\_sst\_anomalies.csv  
├── monthly\_sst\_anomalies.csv  
├── period\_sst\_anomalies.csv  
└── sst\_summary.csv

*SCIENTIFIC CONTEXT*

Sea Surface Temperature is an important variable for studying ocean–atmosphere interactions and climate variability.

SST anomalies represent deviations from a reference climatology and provide a way to investigate changes in ocean conditions over time. These changes are relevant to marine ecosystems, ocean circulation, air–sea interactions, weather and climate patterns, marine heatwaves and ocean productivity.

*TECHNOLOGIES* 

Python was used as the main programming language.

Pandas was used for data cleaning, transformation and aggregation.

Matplotlib was used for data visualization.

SciPy was used for linear regression and statistical analysis.

*FUTURE DEVELOPMENT* 

The next stage of the project will integrate SQL and Tableau into the workflow.

Future extensions may include spatial SST analysis, marine heatwave detection, comparison with atmospheric and oceanographic variables, geospatial visualization and automated data ingestion.

The objective is to expand this project into a complete Python \+ SQL \+ Tableau environmental data analysis workflow.

*SKILLS DEMONSTRATED*

Python · Pandas · Data Cleaning · Exploratory Data Analysis · Time-Series Analysis · Statistics · Linear Regression · Data Visualization · Scientific Data Analysis · Oceanographic Data

*PROJECT STATUS* 

Completed — Python analysis

Next stage: SQL integration and Tableau dashboard.

*AUTHOR*

Mariana Gomes de Andrade Silva

Oceanographic and environmental data analysis portfolio.

Interests: Oceanography · Geophysics · Climate Science · Remote Sensing · Geospatial Data · Scientific Programming · Data Analysis