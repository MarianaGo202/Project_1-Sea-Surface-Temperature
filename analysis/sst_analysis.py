import os
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Paths
INPUT_CSV = "sst_anomaly_1982_2024.csv"
FIGURES_DIR = "outputs/figures"
TABLES_DIR = "outputs/tables"

# Period boundaries for the period comparison
PERIODS = {
    1999: "1982-1999",
    2009: "2000-2009",
    2019: "2010-2019",
}
DEFAULT_PERIOD = "2020-2024"

def load_and_clean_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
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

    return df

def basic_statistics(df: pd.DataFrame) -> dict:
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

    return {"mean": mean_anomaly, "max": max_anomaly, "min": min_anomaly}

def compute_annual_trend(df: pd.DataFrame):
    annual_mean = df.groupby("year")["sst_anomaly"].mean()
    print("\nAnnual mean SST anomalies:\n", annual_mean)

    trend = linregress(annual_mean.index, annual_mean.values)
    total_change = trend.slope * (annual_mean.index.max() - annual_mean.index.min())

    print("\nLinear trend:")
    print("Slope:", trend.slope, "K/year")
    print("R-squared:", trend.rvalue ** 2)
    print("P-value:", trend.pvalue)
    print("Estimated change:", total_change, "K")

    return annual_mean, trend

def plot_monthly_anomaly(df: pd.DataFrame) -> None:
    plt.figure(figsize=(12, 6))
    plt.plot(df["date"], df["sst_anomaly"], label="Monthly SST anomaly")
    plt.axhline(0, linestyle="--", label="Zero anomaly")
    plt.xlabel("Date")
    plt.ylabel("SST Anomaly (K)")
    plt.title("Sea Surface Temperature Anomaly (1982-2024)")
    plt.legend()
    plt.grid(True)
    plt.savefig(f"{FIGURES_DIR}/sst_monthly_anomaly.png", dpi=300, bbox_inches="tight")
    plt.show()

def plot_annual_trend(annual_mean: pd.Series, trend) -> None:
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
    plt.savefig(f"{FIGURES_DIR}/sst_annual_trend.png", dpi=300, bbox_inches="tight")
    plt.show()

def analyze_seasonal_pattern(df: pd.DataFrame) -> pd.Series:
    monthly_mean = df.groupby("month")["sst_anomaly"].mean()
    print("\nMonthly mean SST anomalies:\n", monthly_mean)

    warmest_month = monthly_mean.idxmax()
    coldest_month = monthly_mean.idxmin()
    print("\nMonth with the highest mean anomaly:", warmest_month)
    print("Month with the lowest mean anomaly:", coldest_month)

    return monthly_mean

def plot_rolling_mean(df: pd.DataFrame) -> None:
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
    plt.savefig(f"{FIGURES_DIR}/sst_rolling_mean.png", dpi=300, bbox_inches="tight")
    plt.show()

def warmest_and_coldest_years(annual_mean: pd.Series):
    warmest_years = annual_mean.sort_values(ascending=False).head(10)
    coldest_years = annual_mean.sort_values(ascending=True).head(10)

    print("\nTop 10 warmest years:\n", warmest_years)
    print("\nTop 10 coldest years:\n", coldest_years)

    return warmest_years, coldest_years

def classify_period(year: int) -> str:
    for max_year, label in PERIODS.items():
        if year <= max_year:
            return label
    return DEFAULT_PERIOD

def compare_periods(df: pd.DataFrame) -> pd.Series:
    df["period"] = df["year"].apply(classify_period)
    period_mean = df.groupby("period")["sst_anomaly"].mean()
    print("\nMean SST anomaly by period:\n", period_mean)

    period_trends = {}
    for period in df["period"].unique():
        period_data = df[df["period"] == period]
        regression = linregress(period_data["year"], period_data["sst_anomaly"])
        period_trends[period] = regression.slope

    print("\nSST anomaly trend by period:")
    for period, slope in period_trends.items():
        print(period, ":", slope, "K/year")

    return period_mean

def classify_anomaly_sign(df: pd.DataFrame) -> None:
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

def build_summary_table(stats: dict, trend) -> pd.DataFrame:
    summary = pd.DataFrame({
        "Statistic": [
            "Mean anomaly",
            "Maximum anomaly",
            "Minimum anomaly",
            "Trend",
            "R-squared",
            "P-value",
        ],
        "Value": [
            stats["mean"],
            stats["max"],
            stats["min"],
            trend.slope,
            trend.rvalue ** 2,
            trend.pvalue,
        ],
    })
    print("\nSummary of the SST analysis:\n", summary)
    return summary

def export_results(annual_mean, monthly_mean, period_mean, summary) -> None:
    os.makedirs(TABLES_DIR, exist_ok=True)

    annual_mean.to_csv(f"{TABLES_DIR}/annual_sst_anomalies.csv")
    monthly_mean.to_csv(f"{TABLES_DIR}/monthly_sst_anomalies.csv")
    period_mean.to_csv(f"{TABLES_DIR}/period_sst_anomalies.csv")
    summary.to_csv(f"{TABLES_DIR}/sst_summary.csv", index=False)

    print("\nAnalysis results exported successfully.")

def main():
    os.makedirs(FIGURES_DIR, exist_ok=True)
    os.makedirs(TABLES_DIR, exist_ok=True)

    df = load_and_clean_data(INPUT_CSV)
    stats = basic_statistics(df)
    annual_mean, trend = compute_annual_trend(df)

    plot_monthly_anomaly(df)
    plot_annual_trend(annual_mean, trend)
    monthly_mean = analyze_seasonal_pattern(df)
    plot_rolling_mean(df)

    warmest_and_coldest_years(annual_mean)
    period_mean = compare_periods(df)
    classify_anomaly_sign(df)

    summary = build_summary_table(stats, trend)
    export_results(annual_mean, monthly_mean, period_mean, summary)

if __name__ == "__main__":
    main()
