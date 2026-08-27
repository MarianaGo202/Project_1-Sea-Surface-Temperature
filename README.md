# <h1 align="center">**Sea Surface Temperature Anomaly Analysis**</h1>

<p align="justify">This is my first oceanographic data analysis project, built with Python. I used a real dataset of monthly Sea Surface Temperature (SST) anomalies from 1982 to 2024 to practice data cleaning, exploratory analysis, statistics, and visualization on an actual scientific problem instead of a toy dataset.</p>

**Development environment:** Visual Studio Code (VS Code)

**Project status:** _Completed_ - Python analysis

**Next stage:** SQL and Power BI

## Why This Dataset

<p align="justify">I wanted a subject connected to my interest in oceanography, and SST anomaly data is a good fit: it's widely used in climate science, has a long historical record, and is simple enough to interpret with basic statistics while still requiring real handling of time-series data.</p>

The analysis addresses the following questions:

<table align="center">
  <tr>
    <th>Question</th>
    <th>Approach</th>
  </tr>
  <tr>
    <td>How have SST anomalies varied between 1982 and 2024?</td>
    <td>Analysis of the monthly time series</td>
  </tr>
  <tr>
    <td>Is there an overall long-term trend?</td>
    <td>Linear regression applied to annual mean anomalies</td>
  </tr>
  <tr>
    <td>Which years presented the highest and lowest annual mean anomalies?</td>
    <td>Ranking of annual mean values</td>
  </tr>
  <tr>
    <td>How do anomalies vary by calendar month?</td>
    <td>Grouping observations by month</td>
  </tr>
  <tr>
    <td>How do different periods compare?</td>
    <td>Calculation and comparison of mean anomalies</td>
  </tr>
  <tr>
    <td>How does the long-term pattern change when short-term variability is reduced?</td>
    <td>12-month rolling mean</td>
  </tr>
  <tr>
    <td>How frequently do positive and negative anomalies occur?</td>
    <td>Classification of monthly observations</td>
  </tr>
</table>

## Dataset

<p align="justify">
Monthly Sea Surface Temperature anomaly observations from 1982 to 2024, sourced from the Copernicus Marine Service Ocean Climate Portal.
</p>

[Source: Copernicus Marine Service — Sea Surface Temperature](https://marine.copernicus.eu/ocean-climate-portal/sea-surface-temperature)

<table align="center">
  <tr>
    <th>Variable</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>date</code></td>
    <td>Date of the observation</td>
  </tr>
  <tr>
    <td><code>sst_anomaly</code></td>
    <td>Sea Surface Temperature anomaly (K)</td>
  </tr>
  <tr>
    <td><code>year</code></td>
    <td>Year extracted from the date</td>
  </tr>
  <tr>
    <td><code>month</code></td>
    <td>Month extracted from the date</td>
  </tr>
  <tr>
    <td><code>rolling_12m</code></td>
    <td>12-month rolling mean</td>
  </tr>
  <tr>
    <td><code>period</code></td>
    <td>Time period bucket</td>
  </tr>
</table>

## What I Did

**Data Preparation**

<p align="justify">
Loaded the dataset with Pandas, cleaned up column names, converted the date column to datetime, and extracted year and month. Checked shape, data types, and missing values before moving on to the analysis.
</p>

**Annual Trend**

<p align="justify">
Aggregated the monthly observations into annual means, then used these values to identify the years with the highest and lowest mean anomalies and to estimate the long-term trend.
</p>

**Trend Analysis**

<p align="justify">
Ran a linear regression on the annual mean SST anomalies using <code>scipy.stats.linregress</code>, including R² and p-value, to check whether SST anomaly is trending up over time and how strong that relationship is.
</p>

**Monthly / Seasonal Pattern**

<p align="justify">
Grouped the data by calendar month to check if certain months run consistently warmer or colder. Also classified each monthly observation by anomaly sign (positive, negative, or zero).
</p>

**Rolling Mean**

<p align="justify">
Calculated a 12-month rolling mean to smooth out short-term noise and make the long-term trend easier to see.
</p>

**Period Comparison**

<p align="justify">
Split the dataset into four predefined periods and compared the mean SST anomaly and trend slope across each.
</p>

<table align="center">
  <tr>
    <th>Period</th>
    <th>Years</th>
  </tr>
  <tr>
    <td>1</td>
    <td>1982–1999</td>
  </tr>
  <tr>
    <td>2</td>
    <td>2000–2009</td>
  </tr>
  <tr>
    <td>3</td>
    <td>2010–2019</td>
  </tr>
  <tr>
    <td>4</td>
    <td>2020–2024</td>
  </tr>
</table>

## Visualisations

**Monthly SST Anomaly**

<p align="justify">
Full monthly SST anomaly time series, 1982 to 2024.
</p>

<p align="center">
  <img src="results/png/sst_monthly_anomaly.png" alt="Monthly SST Anomaly" width="800">
</p>

**Annual SST Trend**

<p align="justify">
Annual mean SST anomalies plotted against the fitted linear regression trend.
</p>

<p align="center">
  <img src="results/png/sst_annual_trend.png" alt="Annual SST Trend" width="800">
</p>

**12-Month Rolling Mean**

<p align="justify">
Raw monthly SST anomalies together with the 12-month rolling mean.
</p>

<p align="center">
  <img src="results/png/sst_rolling_mean.png" alt="12-Month Rolling Mean" width="800">
</p>

## Results

<p align="justify">The main numbers — trend slope, R², p-value, highest and lowest annual mean anomalies, the 10 warmest and coldest years, and the mean anomaly per period — are saved in <code>sst_summary.csv</code>.</p>

<p align="justify">All generated CSV files are meant to be reused in the next stage of this project, when I move parts of the analysis into SQL and Power BI.</p>

## Output Files

<table align="center">
  <tr>
    <th align="center">File</th>
    <th align="center">Description</th>
  </tr>
  <tr>
    <td align="center"><code>annual_sst_anomalies.csv</code></td>
    <td align="center">Annual mean SST anomalies</td>
  </tr>
  <tr>
    <td align="center"><code>monthly_sst_anomalies.csv</code></td>
    <td align="center">Mean anomaly by calendar month</td>
  </tr>
  <tr>
    <td align="center"><code>period_sst_anomalies.csv</code></td>
    <td align="center">Mean anomaly by period</td>
  </tr>
  <tr>
    <td align="center"><code>sst_summary.csv</code></td>
    <td align="center">Main statistical results</td>
  </tr>
</table>

## Notes

<p align="justify">
Sea Surface Temperature is one of the key variables used in oceanography and climate science. An SST anomaly is the difference between the observed temperature and a reference average, and tracking it over time is a common way to study changes in ocean conditions and climate variability. Monitoring these anomalies matters because they're linked to broader effects on marine ecosystems, weather patterns, and coastal communities, which is part of why this kind of data is worth analyzing in the first place.
</p>

<p align="justify">
This is a beginner project, though — the goal was to practice the full workflow (cleaning, analysis, visualization, export) on a real scientific dataset, not to draw conclusions about what's causing the changes, analyze their environmental impact, or propose solutions.</p>

## Tools

**Programming and Development**
- Python
- Visual Studio Code (VS Code)

**Python Libraries**
- Pandas
- Matplotlib
- SciPy

## Skills Demonstrated

<p align="center"><i>Python - Pandas - Data Cleaning - Exploratory Data Analysis - Time-Series Analysis - Statistics - Linear Regression - Data Visualisation - Scientific Data Analysis - Oceanographic Data</i></p>

## Author

### Mariana Gomes de Andrade Silva

Introductory project in oceanographic data analysis using Python.

<p align="center"><strong>Interests: Oceanography - Scientific Programming - Data Analysis - Environmental Data</strong></p>
