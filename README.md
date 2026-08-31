# <h1 align="center">**Sea Surface Temperature Anomaly Analysis**</h1>

<p align="justify">This is my first oceanographic data analysis project, built with Python. I used a real dataset of monthly Sea Surface Temperature (SST) anomalies from 1982 to 2024 to practice data cleaning, exploratory analysis, statistics, and visualization on an actual scientific problem instead of a toy dataset. The idea was to work through a full, if simple, analytical workflow end to end — load real observational data, understand its structure, ask concrete questions of it, and back up every answer with a number rather than a guess.</p>

**Development environment:** Visual Studio Code (VS Code)

**Project status:** _Completed_ - Python analysis

**Next stage:** SQL and Power BI

## Why This Dataset

<p align="justify">I wanted a subject connected to my interest in oceanography, and SST anomaly data is a good fit: it's widely used in climate science, has a long historical record, and is simple enough to interpret with basic statistics while still requiring real handling of time-series data. Working with over four decades of monthly observations also meant I had to think about things a smaller dataset wouldn't force on me — how to spot a long-term trend underneath monthly noise, how to compare different time periods fairly, and how to summarize 500+ data points into a handful of numbers that actually mean something.</p>

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
Monthly Sea Surface Temperature anomaly observations from 1982 to 2024, sourced from the Copernicus Marine Service Ocean Climate Portal. Each record is a single global monthly mean anomaly value rather than a gridded map, which keeps the dataset small and tabular — closer to a classic time series than the gridded NetCDF files I'd work with in later projects — but still long enough (over 500 months) to support real trend and seasonality analysis.
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

<p align="justify">The workflow moves from basic cleaning through increasingly specific questions about trend, seasonality and period-to-period change, with each stage building on the columns produced by the one before it:</p>

**Data Preparation**

<p align="justify">
Loaded the dataset with Pandas, cleaned up column names, converted the date column to datetime, and extracted year and month. Checked shape, data types, and missing values before moving on to the analysis, since every later step — grouping by year, by month, comparing periods — depends on the date column being parsed correctly from the start.
</p>

**Annual Trend**

<p align="justify">
Aggregated the monthly observations into annual means, then used these values to identify the years with the highest and lowest mean anomalies and to estimate the long-term trend. Working at the annual level first made it easier to see the broad direction of change before layering in a formal statistical test.
</p>

**Trend Analysis**

<p align="justify">
Ran a linear regression on the annual mean SST anomalies using <code>scipy.stats.linregress</code>, including R² and p-value, to check whether SST anomaly is trending up over time and how strong that relationship is. The slope gives the average rate of change per year, while R² and the p-value indicate how much of the year-to-year variation that trend line actually explains versus how much is noise.
</p>

**Monthly / Seasonal Pattern**

<p align="justify">
Grouped the data by calendar month to check if certain months run consistently warmer or colder. Also classified each monthly observation by anomaly sign (positive, negative, or zero), as a simple way of asking how often the ocean has been running warmer than the baseline versus cooler.
</p>

**Rolling Mean**

<p align="justify">
Calculated a 12-month rolling mean to smooth out short-term noise and make the long-term trend easier to see. This step matters because a single warm or cold month can be driven by short-lived weather noise, while the rolling mean filters that out and leaves the slower-moving climate signal underneath.
</p>

**Period Comparison**

<p align="justify">
Split the dataset into four predefined periods and compared the mean SST anomaly and trend slope across each, as a way of checking whether warming has been roughly constant over the 42-year record or whether it has sped up in more recent decades.
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

<p align="justify">The main numbers — trend slope, R², p-value, highest and lowest annual mean anomalies, the 10 warmest and coldest years, and the mean anomaly per period — are saved in <code>sst_summary.csv</code>, so the key findings from the analysis don't just live in a notebook output but can be pulled up and reused on their own.</p>

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
Sea Surface Temperature is one of the key variables used in oceanography and climate science. An SST anomaly is the difference between the observed temperature and a reference average calculated over a baseline period, rather than the raw temperature itself — this matters because it isolates how much warmer or colder the ocean is running compared to what's "normal" for a given time of year, independent of seasonal swings. Tracking anomalies over time is a standard way to study ocean variability and climate change, since a sustained positive trend points to long-term warming rather than a single hot month or year, and it's the same basic approach used by climate agencies worldwide to report on ocean warming.
</p>

<p align="justify">
These anomalies are also tied to real-world consequences: they influence coral bleaching events, shift the strength and timing of phenomena like El Niño and La Niña, affect fish migration and fisheries, and can intensify storms and disrupt regional weather patterns. Warmer surface water holds more energy available to fuel tropical storms, and shifts in SST patterns can also alter rainfall and temperature far from the ocean itself, since the ocean and atmosphere are tightly coupled. That downstream impact on marine ecosystems, weather, and coastal communities is part of why this kind of data is worth analyzing in the first place, even at a beginner level.
</p>

<p align="justify">
This is a beginner project, though — the goal was to practice the full workflow (cleaning, analysis, visualization, export) on a real scientific dataset, not to draw conclusions about what's causing the changes, analyze their environmental impact, or propose solutions. It also works with a single global mean value per month rather than gridded spatial data, so it can't say anything about how warming differs by ocean basin or region — that kind of spatial detail is something I explored further in later projects in this series.
</p>

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

## Bibliography

- [Copernicus Marine Service — Sea Surface Temperature, Ocean Climate Portal](https://marine.copernicus.eu/ocean-climate-portal/sea-surface-temperature)
- [NOAA — Sea Surface Temperature and Climate](https://www.ncei.noaa.gov/products/climate-data-records/sea-surface-temperature-optimum-interpolation)
- [NOAA — Understanding El Niño and La Niña](https://www.climate.gov/enso)

## Author

### Mariana Gomes de Andrade Silva

Introductory project in oceanographic data analysis using Python.

<p align="center"><strong>Interests: Oceanography - Scientific Programming - Data Analysis - Environmental Data</strong></p>
