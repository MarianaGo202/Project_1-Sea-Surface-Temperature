# **Sea Surface Temperature Anomaly Analysis**

A Python project using Sea Surface Temperature (SST) anomaly data from 1982 to 2024.

The goal is to explore how SST anomalies vary over time, investigate long-term trends, and analyze patterns within an oceanographic dataset.

## Overview

This project was developed as an introduction to oceanographic data analysis with Python. Monthly SST anomaly data were processed using Pandas, Matplotlib and SciPy for data preparation, statistical analysis, visualization and trend estimation.

## Dataset

The dataset contains monthly Sea Surface Temperature anomaly observations from 1982 to 2024. The data were obtained from the Copernicus Marine Service Ocean Climate Portal.

[Source: Copernicus Marine Service — Sea Surface Temperature](https://marine.copernicus.eu/ocean-climate-portal/sea-surface-temperature)

| Variable | Description |
|---|---|
| `date` | Date of the observation |
| `sst_anomaly` | Sea Surface Temperature anomaly (K) |
| `year` | Year extracted from the date |
| `month` | Month extracted from the date |
| `rolling_12m` | 12-month rolling mean |
| `period` | Predefined time period |

## Analysis

The first step was to prepare the dataset using Pandas. Dates were converted to datetime format, and year and month were extracted from the original date column.
Basic statistics were calculated to obtain the mean, maximum and minimum SST anomalies. The monthly data were grouped by year to calculate the annual mean anomaly. These values were then used in a linear regression to estimate the overall trend from 1982 to 2024.

The analysis also includes a monthly comparison, a 12-month rolling mean, and a comparison between different periods. The 10 years with the highest and lowest annual mean anomalies were also identified.

For the period comparison, the dataset was divided into:

| Period | Years |
|:---:|:---:|
| 1 | 1982–1999 |
| 2 | 2000–2009 |
| 3 | 2010–2019 |
| 4 | 2020–2024 |

Monthly observations were also classified as positive, negative or zero anomalies.

## Visualisations

### Monthly SST Anomaly

Monthly SST anomaly observations from 1982 to 2024.

<p align="center">
  <img src="sst_monthly_anomaly.png" alt="Monthly SST Anomaly" width="800">
</p>

### Annual SST Trend

Annual mean SST anomalies and the estimated linear trend.

<p align="center">
  <img src="sst_annual_trend.png" alt="Annual SST Trend" width="800">
</p>

### 12-Month Rolling Mean

Monthly SST anomalies together with the 12-month rolling mean.

<p align="center">
  <img src="sst_rolling_mean.png" alt="12-Month Rolling Mean" width="800">
</p>

## Key Findings

The main results are stored in `sst_summary.csv`. This section will be updated with the main findings from the analysis, including the overall trend, R², p-value, highest and lowest anomaly years, and differences between the selected periods.

## Output Files

| File | Description |
|---|---|
| `annual_sst_anomalies.csv` | Annual mean SST anomalies |
| `monthly_sst_anomalies.csv` | Mean anomaly by calendar month |
| `period_sst_anomalies.csv` | Mean anomaly by predefined period |
| `sst_summary.csv` | Main statistical results |

## Scientific Context

Sea Surface Temperature is an important variable in oceanography and climate studies. SST anomalies show how observed sea surface temperatures differ from a reference climatology. Studying these anomalies can help investigate changes in ocean conditions and their relationship with marine ecosystems, ocean circulation, climate variability and marine heatwaves.

## Technologies

_Python_ was used as the main programming language.

_Pandas_ was used for data cleaning, transformation and organization.

_Matplotlib_ was used to create the visualizations.

_SciPy_ was used for linear regression and statistical analysis.

## Skills Demonstrated

Python · Pandas · Data Cleaning · Exploratory Data Analysis · Time-Series Analysis · Statistics · Linear Regression · Data Visualisation · Scientific Data Analysis · Oceanographic Data

## Project Status

_Completed_ — Python analysis

Next stage: SQL integration and Tableau dashboard.

## Author

### **Mariana Gomes de Andrade Silva**

Oceanographic and environmental data analysis portfolio.

**Interests: Oceanography · Geophysics · Climate Science · Remote Sensing · Geospatial Data · Scientific Programming · Data Analysis**
