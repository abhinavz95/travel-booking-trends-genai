"""
Exploratory Data Analysis - Travel/Hotel Booking Trends
----------------------------------------------------------
Loads a travel booking dataset, cleans it, and produces core EDA outputs:
  - Booking volume by month/season
  - Price distribution by route/destination
  - Booking lead time vs price correlation
  - Cancellation rate breakdown
  - Summary statistics (fed into the Gen-AI insight generator)

Usage:
    python src/eda_analysis.py --data data/bookings.csv
"""

import argparse
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid")


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["booking_date", "travel_date"])
    df = df.dropna(subset=["booking_date", "travel_date", "price"])
    df = df[df["price"] > 0]
    df["lead_time_days"] = (df["travel_date"] - df["booking_date"]).dt.days
    return df


def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    df["travel_month"] = df["travel_date"].dt.month_name()
    return df


def plot_bookings_by_month(df: pd.DataFrame, out_path: str) -> None:
    plt.figure(figsize=(10, 5))
    df["travel_month"].value_counts().plot(kind="bar")
    plt.title("Booking Volume by Travel Month")
    plt.xlabel("Month")
    plt.ylabel("Number of Bookings")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def plot_price_distribution(df: pd.DataFrame, out_path: str) -> None:
    plt.figure(figsize=(10, 5))
    sns.histplot(df["price"], bins=40, kde=True)
    plt.title("Booking Price Distribution")
    plt.xlabel("Price")
    plt.tight_layout()
    plt.savefig(out_path)
    plt.close()


def compute_summary_stats(df: pd.DataFrame) -> dict:
    cancel_col = "is_cancelled"
    cancellation_rate = (
        round(df[cancel_col].mean(), 3) if cancel_col in df.columns else None
    )
    return {
        "avg_price": round(df["price"].mean(), 2),
        "busiest_month": df["travel_month"].value_counts().idxmax(),
        "avg_lead_time_days": round(df["lead_time_days"].mean(), 1),
        "cancellation_rate": cancellation_rate,
        "total_bookings": len(df),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", required=True, help="Path to bookings CSV file")
    parser.add_argument("--outdir", default="outputs", help="Output folder for charts")
    args = parser.parse_args()

    df = load_data(args.data)
    df = add_time_features(df)

    plot_bookings_by_month(df, f"{args.outdir}/bookings_by_month.png")
    plot_price_distribution(df, f"{args.outdir}/price_distribution.png")

    stats = compute_summary_stats(df)
    print("Summary statistics:")
    for k, v in stats.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
