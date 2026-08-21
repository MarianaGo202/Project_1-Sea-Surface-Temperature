# Import Pandas for data analysis
import pandas as pd

# Import Matplotlib for creating graphs
import matplotlib.pyplot as plt

# Import linear regression from SciPy
from scipy.stats import linregress

# Load the SST anomaly data from the CSV file
df = pd.read_csv("CSVExport.csv")

# Remove extra spaces from column names
df.columns = df.columns.str.strip()

# Rename the data column to a simple and clear name
df = df.rename(columns={"- values": "sst_anomaly"})

# Convert the date column from text to datetime
df["date"] = pd.to_datetime(df["date"])

# Extract the year from each date
df["year"] = df["date"].dt.year

# Show the number of rows and columns
print("Dataset size:")
print(df.shape)

# Show the column names
print("\nColumns:")
print(df.columns)

# Show the first five rows
print("\nFirst five rows:")
print(df.head())

# Show the data types
print("\nData types:")
print(df.dtypes)

# Check for missing values
print("\nMissing values:")
print(df.isnull().sum())

# Calculate the mean SST anomaly
mean_anomaly = df["sst_anomaly"].mean()

# Find the maximum SST anomaly
max_anomaly = df["sst_anomaly"].max()

# Find the minimum SST anomaly
min_anomaly = df["sst_anomaly"].min()

# Print the statistics
print("\nSST anomaly statistics:")

print("Mean anomaly:", mean_anomaly, "K")

print("Maximum anomaly:", max_anomaly, "K")

print("Minimum anomaly:", min_anomaly, "K")

# Find the row with the highest SST anomaly
highest_anomaly = df.loc[df["sst_anomaly"].idxmax()]

# Find the row with the lowest SST anomaly
lowest_anomaly = df.loc[df["sst_anomaly"].idxmin()]

# Print the highest anomaly
print("\nHighest SST anomaly:")
print(highest_anomaly)

# Print the lowest anomaly
print("\nLowest SST anomaly:")
print(lowest_anomaly)

# Calculate the mean SST anomaly for each year
annual_mean = df.groupby("year")["sst_anomaly"].mean()

# Print the annual means
print("\nAnnual mean SST anomalies:")
print(annual_mean)

# Calculate a linear regression using year and annual anomaly
trend = linregress(
    annual_mean.index,
    annual_mean.values
)

# Calculate the total change across the study period
total_change = (
    trend.slope *
    (annual_mean.index.max() - annual_mean.index.min())
)

# Print the trend results
print("\nLinear trend:")

print("Slope:", trend.slope, "K/year")

print("R-squared:", trend.rvalue ** 2)

print("P-value:", trend.pvalue)

print("Estimated change:", total_change, "K")

# Create a figure
plt.figure(figsize=(12, 6))

# Plot the monthly SST anomaly
plt.plot(
    df["date"],
    df["sst_anomaly"],
    label="Monthly SST anomaly"
)

# Add a horizontal line at zero
plt.axhline(
    0,
    linestyle="--",
    label="Zero anomaly"
)

# Add the x-axis label
plt.xlabel("Date")

# Add the y-axis label
plt.ylabel("SST Anomaly (K)")

# Add the graph title
plt.title(
    "Sea Surface Temperature Anomaly (1982–2024)"
)

# Add a legend
plt.legend()

# Add a grid
plt.grid(True)

# Save the graph as a high-resolution PNG
plt.savefig(
    "sst_monthly_anomaly.png",
    dpi=300,
    bbox_inches="tight"
)

# Display the graph
plt.show()

# Create a new figure
plt.figure(figsize=(12, 6))

# Plot the annual mean SST anomaly
plt.plot(
    annual_mean.index,
    annual_mean.values,
    label="Annual mean anomaly"
)

# Calculate the values predicted by the linear trend
trend_line = (
    trend.intercept
    + trend.slope * annual_mean.index
)

# Plot the linear trend
plt.plot(
    annual_mean.index,
    trend_line,
    linestyle="--",
    label="Linear trend"
)

# Add a horizontal zero reference line
plt.axhline(
    0,
    linestyle="--",
    label="Zero anomaly"
)

# Add the x-axis label
plt.xlabel("Year")

# Add the y-axis label
plt.ylabel("Mean SST Anomaly (K)")

# Add the graph title
plt.title(
    "Annual Mean Sea Surface Temperature Anomaly"
)

# Add a legend
plt.legend()

# Add a grid
plt.grid(True)

# Save the graph
plt.savefig(
    "sst_annual_trend.png",
    dpi=300,
    bbox_inches="tight"
)

# Display the graph
plt.show()

# Extract the month number from each date
df["month"] = df["date"].dt.month

# Calculate the mean anomaly for each calendar month
monthly_mean = df.groupby("month")["sst_anomaly"].mean()

# Print the monthly means
print("\nMonthly mean SST anomalies:")
print(monthly_mean)

# Find the month with the highest mean anomaly
warmest_month = monthly_mean.idxmax()

# Find the month with the lowest mean anomaly
coldest_month = monthly_mean.idxmin()

print("\nMonth with the highest mean anomaly:")
print(warmest_month)

print("\nMonth with the lowest mean anomaly:")
print(coldest_month)

# Calculate a 12-month rolling mean
df["rolling_12m"] = (
    df["sst_anomaly"]
    .rolling(window=12)
    .mean()
)

# Create a new figure
plt.figure(figsize=(12, 6))

# Plot the original monthly anomalies
plt.plot(
    df["date"],
    df["sst_anomaly"],
    label="Monthly SST anomaly",
    alpha=0.4
)

# Plot the 12-month rolling mean
plt.plot(
    df["date"],
    df["rolling_12m"],
    label="12-month rolling mean"
)

# Add the zero reference line
plt.axhline(
    0,
    linestyle="--",
    label="Zero anomaly"
)

# Add labels
plt.xlabel("Date")
plt.ylabel("SST Anomaly (K)")

# Add title
plt.title(
    "SST Anomaly and 12-Month Rolling Mean"
)

# Add legend
plt.legend()

# Add grid
plt.grid(True)

# Save the figure
plt.savefig(
    "sst_rolling_mean.png",
    dpi=300,
    bbox_inches="tight"
)

# Display the graph
plt.show()

# Sort annual means from highest to lowest
warmest_years = annual_mean.sort_values(
    ascending=False
).head(10)

# Sort annual means from lowest to highest
coldest_years = annual_mean.sort_values(
    ascending=True
).head(10)

# Print the 10 warmest years
print("\nTop 10 warmest years:")
print(warmest_years)

# Print the 10 coldest years
print("\nTop 10 coldest years:")
print(coldest_years)

# Create a function to classify each year into a period
def classify_period(year):

    if year <= 1999:
        return "1982-1999"

    elif year <= 2009:
        return "2000-2009"

    elif year <= 2019:
        return "2010-2019"

    else:
        return "2020-2024"


# Create a new period column
df["period"] = df["year"].apply(classify_period)

# Calculate the mean anomaly for each period
period_mean = df.groupby("period")["sst_anomaly"].mean()

print("\nMean SST anomaly by period:")
print(period_mean)

# Count months with positive anomalies
positive_months = (
    df["sst_anomaly"] > 0
).sum()

# Count months with negative anomalies
negative_months = (
    df["sst_anomaly"] < 0
).sum()

# Count months with exactly zero anomaly
zero_months = (
    df["sst_anomaly"] == 0
).sum()

print("\nAnomaly classification:")

print(
    "Positive anomaly months:",
    positive_months
)

print(
    "Negative anomaly months:",
    negative_months
)

print(
    "Zero anomaly months:",
    zero_months
)

# Calculate the percentage of positive anomalies
positive_percentage = (
    positive_months / len(df) * 100
)

# Calculate the percentage of negative anomalies
negative_percentage = (
    negative_months / len(df) * 100
)

print(
    "\nPercentage of positive anomalies:",
    positive_percentage,
    "%"
)

print(
    "Percentage of negative anomalies:",
    negative_percentage,
    "%"
)

# Create an empty dictionary to store the results
period_trends = {}

# Loop through each period
for period in df["period"].unique():

    # Select the data for this period
    period_data = df[
        df["period"] == period
    ]

    # Calculate the linear regression
    regression = linregress(
        period_data["year"],
        period_data["sst_anomaly"]
    )

    # Store the slope
    period_trends[period] = regression.slope

print("\nSST anomaly trend by period:")

for period, slope in period_trends.items():

    print(
        period,
        ":",
        slope,
        "K/year"
    )

# Create a summary table with important statistics
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

# Print the summary table
print("\nSummary of the SST analysis:")
print(summary)

# Save the annual mean anomalies
annual_mean.to_csv(
    "annual_sst_anomalies.csv"
)

# Save the monthly mean anomalies
monthly_mean.to_csv(
    "monthly_sst_anomalies.csv"
)

# Save the period means
period_mean.to_csv(
    "period_sst_anomalies.csv"
)

# Save the summary table
summary.to_csv(
    "sst_summary.csv",
    index=False
)

# Print confirmation
print("\nAnalysis results exported successfully.")

