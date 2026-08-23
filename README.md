# <h1 align="center">**Sea Surface Temperature Anomaly Analysis**</h1> 

<p align="justify"> This project presents a Python-based analysis of Sea Surface Temperature (SST) anomaly data from 1982 to 2024. The analysis investigates changes over time, long-term trends, seasonal patterns, and differences between the periods analyzed.</p>

<p align="justify">Developed as an introductory project in oceanographic data analysis, the study uses Python to analyze a real scientific dataset, including data preparation, exploratory analysis, statistical analysis, time-series analysis, and data visualization.</p>

**Development environment:** Visual Studio Code (VS Code)

**Project status:** _Completed_ - Python analysis

**Next stage:** SQL and Power BI

## Objective

<p align="justify">The objective of this project is to investigate how Sea Surface Temperature anomalies changed between 1982 and 2024 and apply a reproducible data analysis process to an oceanographic dataset.</p>

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
The dataset contains monthly Sea Surface Temperature anomaly observations from 1982 to 2024. The data were obtained from the Copernicus Marine Service Ocean Climate Portal.
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
    <td>Predefined time period</td>
  </tr>
</table>

## Methodology

**Data Preparation**

<p align="justify">
The original dataset was loaded with Pandas and prepared for analysis. The date variable was converted to datetime format, from which year and month were extracted. The dataset structure, data types, and missing values were also checked before the analysis.
</p>

**Annual Analysis**

<p align="justify">
Monthly observations were aggregated by year to calculate the annual mean SST anomaly. These annual values were subsequently used to identify the years with the highest and lowest mean anomalies and to estimate the long-term trend.
</p>

**Trend Analysis**

<p align="justify">
A linear regression was performed on the annual mean SST anomalies using <code>scipy.stats.linregress</code>. The regression provides the estimated trend together with R² and p-value, allowing the statistical relationship between year and SST anomaly to be evaluated.
</p>

**Monthly Analysis**

<p align="justify">
The data were grouped by calendar month to examine monthly patterns in SST anomalies. Monthly observations were also classified according to their anomaly sign as positive, negative, or zero.
</p>

**Rolling Mean**

<p align="justify">
A 12-month rolling mean was calculated to reduce short-term variability and provide a clearer representation of longer-term changes in the time series.
</p>

**Period Comparison**

<p align="justify">
The dataset was divided into four predefined periods. The mean SST anomaly was calculated for each period to facilitate comparison across different stages of the dataset.

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
Monthly SST anomaly observations from 1982 to 2024.
</p>

<p align="center">
  <img src="sst_monthly_anomaly.png" alt="Monthly SST Anomaly" width="800">
</p>

**Annual SST Trend**

<p align="justify">
Annual mean SST anomalies and the estimated linear regression trend.
</p>

<p align="center">
  <img src="sst_annual_trend.png" alt="Annual SST Trend" width="800">
</p>

**12-Month Rolling Mean**

<p align="justify">
Monthly SST anomalies together with the 12-month rolling mean.
</p>

<p align="center">
  <img src="sst_rolling_mean.png" alt="12-Month Rolling Mean" width="800">
</p>

## Results

<p align="justify">The main statistical results are stored in <code>sst_summary.csv</code>. The analysis includes the estimated long-term trend, R², p-value, highest and lowest annual mean anomalies, the 10 years with the highest and lowest annual means, and the mean anomaly for each predefined period.</p>

<p align="justify">The generated CSV files allow the results to be reused in the next stages of the project, including SQL and Power BI.</p>

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
    <td align="center">Mean anomaly by predefined period</td>
  </tr>
  <tr>
    <td align="center"><code>sst_summary.csv</code></td>
    <td align="center">Main statistical results</td>
  </tr>
</table>

## Scientific Context

<p align="justify">
Sea Surface Temperature (SST) is an important variable in oceanography and climate science. SST anomalies represent the difference between the observed temperature and a reference value and are used to identify changes in ocean conditions and climate variability.
</p>

<p align="justify">
Understanding how SST anomalies vary over time can therefore provide insight into long-term changes in ocean conditions and their potential environmental implications. This project focuses on analyzing the temporal patterns and characteristics of SST anomalies between 1982 and 2024, including their long-term trend, annual and monthly variability, and differences between selected periods.
</p>

<p align="justify">
The project aims to describe the patterns identified in the data without directly investigating their causes or their impacts on the environment.
</p>

## Technologies

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
