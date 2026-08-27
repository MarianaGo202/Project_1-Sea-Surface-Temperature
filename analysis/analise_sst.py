import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load and clean data
df = pd.read_csv("CSVExport.csv")
df.columns = df.columns.str.strip()
df = df.rename(columns={"- values": "sst_anomaly"})
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month

print("Dataset size:", df.shape)
print("\nColumns:", df.columns)
print("\nFirst five rows:\n", df.head())
print("\nData types:\n", df.dtypes)
print("\nMissing values:\n", df.isnull().sum())

# Basic statistics
mean_anomaly = df["sst_anomaly"].mean()
max_anomaly = df["sst_anomaly"].max()
min_anomaly = df["sst_anomaly"].min()

print("\nSST anomaly statistics:")
print("Mean anomaly:", mean_anomaly, "K")
print("Maximum anomaly:", max_anomaly, "K")
print("Minimum anomaly:", min_anomaly, "K")

highest_anomaly = df.loc[df["sst_anomaly"].idxmax()]
lowest_anomaly = df.loc[df["sst_anomaly"].idxmin()]

print("\nHighest SST anomaly:\n", highest_anomaly)
print("\nLowest SST anomaly:\n", lowest_anomaly)

# Annual trend
# Average the monthly values into one number per year, then fit a linear regression to see whether SST anomaly is rising over time.
annual_mean = df.groupby("year")["sst_anomaly"].mean()

print("\nAnnual mean SST anomalies:\n", annual_mean)

trend = linregress(annual_mean.index, annual_mean.values)
total_change = trend.slope * (annual_mean.index.max() - annual_mean.index.min())

print("\nLinear trend:")
print("Slope:", trend.slope, "K/year")
print("R-squared:", trend.rvalue ** 2)
print("P-value:", trend.pvalue)
print("Estimated change:", total_change, "K")

# Plot 1: monthly anomaly over time
plt.figure(figsize=(12, 6))
plt.plot(df["date"], df["sst_anomaly"], label="Monthly SST anomaly")
plt.axhline(0, linestyle="--", label="Zero anomaly")
plt.xlabel("Date")
plt.ylabel("SST Anomaly (K)")
plt.title("Sea Surface Temperature Anomaly (1982–2024)")
plt.legend()
plt.grid(True)
plt.savefig("sst_monthly_anomaly.png", dpi=300, bbox_inches="tight")
plt.show()

# Plot 2: annual mean with trend line
plt.figure(figsize=(12, 6))
plt.plot(annual_mean.index, annual_mean.values, label="Annual mean anomaly")

trend_line = trend.intercept + trend.slope * annual_mean.index
plt.plot(annual_mean.index, trend_line, linestyle="--", label="Linear trend")
plt.axhline(0, linestyle="--", label="Zero anomaly")
plt.xlabel("Year")
plt.ylabel("Mean SST Anomaly (K)")
plt.title("Annual Mean Sea Surface Temperature Anomaly")
plt.legend()
plt.grid(True)
plt.savefig("sst_annual_trend.png", dpi=300, bbox_inches="tight")
plt.show()

# Seasonal pattern (mean anomaly per calendar month)
monthly_mean = df.groupby("month")["sst_anomaly"].mean()

print("\nMonthly mean SST anomalies:\n", monthly_mean)

warmest_month = monthly_mean.idxmax()
coldest_month = monthly_mean.idxmin()

print("\nMonth with the highest mean anomaly:", warmest_month)
print("Month with the lowest mean anomaly:", coldest_month)

# Plot 3: monthly anomaly with 12-month rolling mean
# Smooths out month-to-month noise so the long-term trend is easier to see
df["rolling_12m"] = df["sst_anomaly"].rolling(window=12).mean()

plt.figure(figsize=(12, 6))
plt.plot(df["date"], df["sst_anomaly"], label="Monthly SST anomaly", alpha=0.4)
plt.plot(df["date"], df["rolling_12m"], label="12-month rolling mean")
plt.axhline(0, linestyle="--", label="Zero anomaly")
plt.xlabel("Date")
plt.ylabel("SST Anomaly (K)")
plt.title("SST Anomaly and 12-Month Rolling Mean")
plt.legend()
plt.grid(True)
plt.savefig("sst_rolling_mean.png", dpi=300, bbox_inches="tight")
plt.show()

# Warmest/coldest years
warmest_years = annual_mean.sort_values(ascending=False).head(10)
coldest_years = annual_mean.sort_values(ascending=True).head(10)

print("\nTop 10 warmest years:\n", warmest_years)
print("\nTop 10 coldest years:\n", coldest_years)


# Period comparison
# Splits the dataset into decade-ish blocks so we can compare warming behavior across different eras
def classify_period(year):
    if year <= 1999:
        return "1982-1999"
    elif year <= 2009:
        return "2000-2009"
    elif year <= 2019:
        return "2010-2019"
    else:
        return "2020-2024"


df["period"] = df["year"].apply(classify_period)
period_mean = df.groupby("period")["sst_anomaly"].mean()

print("\nMean SST anomaly by period:\n", period_mean)

# Positive vs negative anomaly months
positive_months = (df["sst_anomaly"] > 0).sum()
negative_months = (df["sst_anomaly"] < 0).sum()
zero_months = (df["sst_anomaly"] == 0).sum()

print("\nAnomaly classification:")
print("Positive anomaly months:", positive_months)
print("Negative anomaly months:", negative_months)
print("Zero anomaly months:", zero_months)

positive_percentage = positive_months / len(df) * 100
negative_percentage = negative_months / len(df) * 100

print("\nPercentage of positive anomalies:", positive_percentage, "%")
print("Percentage of negative anomalies:", negative_percentage, "%")

# Trend within each period
# Fits a separate regression per period to check if warming has accelerated or slowed compared to other eras
period_trends = {}
for period in df["period"].unique():
    period_data = df[df["period"] == period]
    regression = linregress(period_data["year"], period_data["sst_anomaly"])
    period_trends[period] = regression.slope

print("\nSST anomaly trend by period:")
for period, slope in period_trends.items():
    print(period, ":", slope, "K/year")

# Summary table
summary = pd.DataFrame({
    "Statistic": [
        "Mean anomaly",
        "Maximum anomaly",
        "Minimum anomaly",
        "Trend",
        "R-squared",
        "P-value"
    ],
    "Value": [
        mean_anomaly,
        max_anomaly,
        min_anomaly,
        trend.slope,
        trend.rvalue ** 2,
        trend.pvalue
    ]
})

print("\nSummary of the SST analysis:\n", summary)

# Export results
annual_mean.to_csv("annual_sst_anomalies.csv")
monthly_mean.to_csv("monthly_sst_anomalies.csv")
period_mean.to_csv("period_sst_anomalies.csv")
summary.to_csv("sst_summary.csv", index=False)

print("\nAnalysis results exported successfully.")