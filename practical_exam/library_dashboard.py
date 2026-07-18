"""
library_dashboard.py
=====================
E-Library Data Insights Dashboard

A Python-based dashboard that loads, cleans, analyzes, and visualizes
e-library book borrowing transaction data.

Concepts demonstrated:
    - Control Structures & Arrays  : input validation, loops, conditionals
    - OOP                          : LibraryDashboard class
    - NumPy                        : duration statistics
    - Pandas                       : cleaning, grouping, aggregation
    - Matplotlib & Seaborn         : bar chart, line graph, pie chart, heatmap

Usage:
    python library_dashboard.py
    (or import LibraryDashboard and use it programmatically)
"""

import os
import sys
from datetime import datetime

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")  # safe for headless/script execution
import matplotlib.pyplot as plt
import seaborn as sns


REQUIRED_COLUMNS = [
    "Transaction ID",
    "Date",
    "User ID",
    "Book Title",
    "Genre",
    "Borrowing Duration (Days)",
]


class LibraryDashboard:
    """
    Encapsulates loading, validation, analysis, filtering, reporting,
    and visualization for e-library transaction data.
    """

    def __init__(self, output_dir="output_charts"):
        self.raw_data = None          # untouched, as-loaded DataFrame
        self.data = None              # cleaned/working DataFrame
        self.statistics = {}          # populated by calculate_statistics()
        self.output_dir = output_dir

        # Control structure: ensure the output folder for charts exists
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    # ------------------------------------------------------------------
    # 1. DATA INPUT & VALIDATION (Control Structures & Arrays)
    # ------------------------------------------------------------------
    def load_data(self, file_path):
        """
        Loads the CSV using Pandas, validates its structure, and cleans it:
          - Checks the file exists and is a CSV
          - Checks all required columns are present
          - Loops through rows (via vectorized + explicit checks) to
            flag missing / inconsistent entries
          - Cleans: drops duplicates, fixes invalid durations, parses dates
        """
        # --- basic file validation (control structures) ---
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        if not file_path.lower().endswith(".csv"):
            raise ValueError("Invalid file format. Please provide a .csv file.")

        df = pd.read_csv(file_path)
        self.raw_data = df.copy()

        # --- required column validation ---
        missing_columns = []
        for col in REQUIRED_COLUMNS:          # explicit loop over an array of expected columns
            if col not in df.columns:
                missing_columns.append(col)

        if missing_columns:
            raise ValueError(f"Dataset is missing required columns: {missing_columns}")

        print(f"Loaded {len(df)} raw rows from '{file_path}'.")

        # --- row-level validation summary using loops/conditionals ---
        missing_counts = {}
        for col in REQUIRED_COLUMNS:
            n_missing = df[col].isna().sum() + (df[col].astype(str).str.strip() == "").sum()
            if n_missing > 0:
                missing_counts[col] = int(n_missing)

        if missing_counts:
            print("Missing/blank values detected per column:")
            for col, count in missing_counts.items():
                print(f"   - {col}: {count} missing")
        else:
            print("No missing values detected.")

        duplicate_count = df.duplicated().sum()
        if duplicate_count > 0:
            print(f"Found {duplicate_count} duplicate rows -> will be removed during cleaning.")

        # --- cleaning ---
        df = self._clean_data(df)
        self.data = df

        print(f"After cleaning: {len(self.data)} valid rows remain.\n")
        return self.data

    def _clean_data(self, df):
        """
        Internal helper: cleans the raw dataframe.
          - Removes exact duplicate rows
          - Converts Date to datetime, drops unparseable dates
          - Converts Borrowing Duration to numeric, drops invalid/negative values
          - Drops rows with missing Book Title / Genre
        """
        df = df.drop_duplicates().copy()

        # Replace blank strings with NaN so pandas treats them as missing
        df.replace(r"^\s*$", np.nan, regex=True, inplace=True)

        # Parse dates; invalid dates become NaT and are dropped
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

        # Convert duration to numeric; invalid entries (e.g. "N/A") become NaN
        df["Borrowing Duration (Days)"] = pd.to_numeric(
            df["Borrowing Duration (Days)"], errors="coerce"
        )

        # Conditional cleaning: drop negative or zero durations (invalid/inconsistent)
        df = df[(df["Borrowing Duration (Days)"].isna()) | (df["Borrowing Duration (Days)"] > 0)]

        # Drop rows still missing essential fields
        essential = ["Date", "Book Title", "Genre", "Borrowing Duration (Days)", "User ID"]
        df = df.dropna(subset=essential)

        df["Borrowing Duration (Days)"] = df["Borrowing Duration (Days)"].astype(int)
        df.reset_index(drop=True, inplace=True)
        return df

    # ------------------------------------------------------------------
    # 2 & 3. STATISTICS (NumPy + Pandas)
    # ------------------------------------------------------------------
    def calculate_statistics(self):
        """
        Calculates key metrics using NumPy for numerical computation and
        Pandas for grouping/aggregation:
          - Most borrowed book / genre
          - Average & std. dev. of borrowing duration (NumPy)
          - Busiest day of the week
          - Total borrowings per book, average duration per genre
          - Frequent borrowers, late-return flag counts
        """
        if self.data is None:
            raise RuntimeError("No data loaded. Call load_data() first.")

        df = self.data

        # NumPy array of durations for statistical computation
        durations = df["Borrowing Duration (Days)"].to_numpy()

        stats = {}
        stats["total_transactions"] = len(df)
        stats["unique_users"] = df["User ID"].nunique()
        stats["unique_books"] = df["Book Title"].nunique()

        # NumPy-based duration statistics
        stats["avg_duration_days"] = float(np.mean(durations))
        stats["std_duration_days"] = float(np.std(durations))
        stats["min_duration_days"] = int(np.min(durations))
        stats["max_duration_days"] = int(np.max(durations))
        stats["median_duration_days"] = float(np.median(durations))

        # Most borrowed book (Pandas aggregation)
        book_counts = df["Book Title"].value_counts()
        stats["most_borrowed_book"] = book_counts.index[0]
        stats["most_borrowed_book_count"] = int(book_counts.iloc[0])
        stats["top_5_books"] = book_counts.head(5)

        # Genre distribution
        genre_counts = df["Genre"].value_counts()
        stats["most_popular_genre"] = genre_counts.index[0]
        stats["genre_distribution"] = genre_counts

        # Busiest day of week
        df["Day of Week"] = df["Date"].dt.day_name()
        day_counts = df["Day of Week"].value_counts()
        stats["busiest_day"] = day_counts.index[0]
        stats["day_distribution"] = day_counts

        # Borrowing trend over months
        df["Month"] = df["Date"].dt.to_period("M")
        monthly_trend = df.groupby("Month").size()
        stats["monthly_trend"] = monthly_trend

        # Aggregations: total borrowings per book, avg duration per genre
        stats["avg_duration_by_genre"] = df.groupby("Genre")["Borrowing Duration (Days)"].mean()
        stats["borrowings_per_book"] = book_counts

        # Frequent borrowers (top 5 users by transaction count)
        stats["frequent_borrowers"] = df["User ID"].value_counts().head(5)

        # Computed column: flag "late returns" (duration > 21 days is considered late)
        df["Late Return"] = df["Borrowing Duration (Days)"] > 21
        stats["late_return_count"] = int(df["Late Return"].sum())
        stats["late_return_pct"] = round(100 * df["Late Return"].mean(), 2)

        self.data = df  # persist computed columns (Day of Week, Month, Late Return)
        self.statistics = stats
        return stats

    # ------------------------------------------------------------------
    # FILTERING
    # ------------------------------------------------------------------
    def filter_transactions(self, condition=None, genre=None, start_date=None,
                             end_date=None, min_duration=None, max_duration=None):
        """
        Filters transactions based on user-defined criteria.

        Parameters:
            condition   : optional custom function(row) -> bool for advanced filtering
            genre       : str, filter by exact genre match
            start_date  : str 'YYYY-MM-DD', inclusive lower bound on Date
            end_date    : str 'YYYY-MM-DD', inclusive upper bound on Date
            min_duration, max_duration : int bounds on Borrowing Duration (Days)

        Returns:
            Filtered pandas DataFrame (does not mutate self.data)
        """
        if self.data is None:
            raise RuntimeError("No data loaded. Call load_data() first.")

        filtered = self.data.copy()

        if genre is not None:
            filtered = filtered[filtered["Genre"].str.lower() == genre.lower()]

        if start_date is not None:
            filtered = filtered[filtered["Date"] >= pd.to_datetime(start_date)]

        if end_date is not None:
            filtered = filtered[filtered["Date"] <= pd.to_datetime(end_date)]

        if min_duration is not None:
            filtered = filtered[filtered["Borrowing Duration (Days)"] >= min_duration]

        if max_duration is not None:
            filtered = filtered[filtered["Borrowing Duration (Days)"] <= max_duration]

        if condition is not None:
            filtered = filtered[filtered.apply(condition, axis=1)]

        print(f"Filter applied -> {len(filtered)} of {len(self.data)} transactions match.")
        return filtered

    # ------------------------------------------------------------------
    # REPORTING
    # ------------------------------------------------------------------
    def generate_report(self):
        """Generates and prints a human-readable summary report."""
        if not self.statistics:
            self.calculate_statistics()

        s = self.statistics
        lines = []
        lines.append("=" * 60)
        lines.append("        E-LIBRARY DATA INSIGHTS - SUMMARY REPORT")
        lines.append("=" * 60)
        lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        lines.append("-" * 60)
        lines.append(f"Total valid transactions : {s['total_transactions']}")
        lines.append(f"Unique users             : {s['unique_users']}")
        lines.append(f"Unique books             : {s['unique_books']}")
        lines.append("")
        lines.append(f"Most borrowed book       : {s['most_borrowed_book']} "
                      f"({s['most_borrowed_book_count']} borrows)")
        lines.append(f"Most popular genre       : {s['most_popular_genre']}")
        lines.append(f"Busiest day of the week  : {s['busiest_day']}")
        lines.append("")
        lines.append("Borrowing Duration Stats (days):")
        lines.append(f"   Average : {s['avg_duration_days']:.2f}")
        lines.append(f"   Median  : {s['median_duration_days']:.2f}")
        lines.append(f"   Std Dev : {s['std_duration_days']:.2f}")
        lines.append(f"   Min/Max : {s['min_duration_days']} / {s['max_duration_days']}")
        lines.append("")
        lines.append(f"Late returns (>21 days)  : {s['late_return_count']} "
                      f"({s['late_return_pct']}% of transactions)")
        lines.append("")
        lines.append("Top 5 Most Borrowed Books:")
        for title, count in s["top_5_books"].items():
            lines.append(f"   - {title}: {count}")
        lines.append("")
        lines.append("Top 5 Frequent Borrowers:")
        for user, count in s["frequent_borrowers"].items():
            lines.append(f"   - {user}: {count} transactions")
        lines.append("")
        lines.append("Average Borrowing Duration by Genre:")
        for genre, avg in s["avg_duration_by_genre"].sort_values(ascending=False).items():
            lines.append(f"   - {genre}: {avg:.1f} days")
        lines.append("=" * 60)

        report_text = "\n".join(lines)
        print(report_text)

        report_path = os.path.join(self.output_dir, "summary_report.txt")
        with open(report_path, "w") as f:
            f.write(report_text)
        print(f"\nReport saved to: {report_path}")
        return report_text

    # ------------------------------------------------------------------
    # 4. VISUALIZATIONS (Matplotlib & Seaborn)
    # ------------------------------------------------------------------
    def visualize_top_books(self):
        """Bar Chart: Top 5 most borrowed books."""
        top5 = self.statistics["top_5_books"]
        plt.figure(figsize=(9, 6))
        sns.barplot(x=top5.values, y=top5.index, hue=top5.index, palette="viridis", legend=False)
        plt.title("Top 5 Most Borrowed Books", fontsize=14, fontweight="bold")
        plt.xlabel("Number of Borrows")
        plt.ylabel("Book Title")
        plt.tight_layout()
        path = os.path.join(self.output_dir, "top_5_books_bar_chart.png")
        plt.savefig(path, dpi=150)
        plt.close()
        print(f"Saved: {path}")

    def visualize_monthly_trend(self):
        """Line Graph: Borrowing trends over months."""
        trend = self.statistics["monthly_trend"]
        plt.figure(figsize=(10, 6))
        plt.plot(trend.index.astype(str), trend.values, marker="o", color="teal", linewidth=2)
        plt.title("Borrowing Trends Over Months", fontsize=14, fontweight="bold")
        plt.xlabel("Month")
        plt.ylabel("Number of Transactions")
        plt.xticks(rotation=45)
        plt.grid(alpha=0.3)
        plt.tight_layout()
        path = os.path.join(self.output_dir, "monthly_trend_line_graph.png")
        plt.savefig(path, dpi=150)
        plt.close()
        print(f"Saved: {path}")

    def visualize_genre_distribution(self):
        """Pie Chart: Distribution of books borrowed by genre."""
        genre_dist = self.statistics["genre_distribution"]
        plt.figure(figsize=(8, 8))
        colors = sns.color_palette("Set2", len(genre_dist))
        plt.pie(
            genre_dist.values,
            labels=genre_dist.index,
            autopct="%1.1f%%",
            startangle=90,
            colors=colors,
        )
        plt.title("Distribution of Books Borrowed by Genre", fontsize=14, fontweight="bold")
        plt.tight_layout()
        path = os.path.join(self.output_dir, "genre_distribution_pie_chart.png")
        plt.savefig(path, dpi=150)
        plt.close()
        print(f"Saved: {path}")

    def visualize_activity_heatmap(self):
        """Heatmap: Borrowing activity by day of week and month."""
        df = self.data
        pivot = df.pivot_table(
            index="Day of Week",
            columns="Month",
            values="Transaction ID",
            aggfunc="count",
            fill_value=0,
        )

        day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        pivot = pivot.reindex(day_order)
        pivot.columns = pivot.columns.astype(str)

        plt.figure(figsize=(12, 6))
        sns.heatmap(pivot, cmap="YlGnBu", annot=True, fmt="d", linewidths=0.5)
        plt.title("Borrowing Activity by Day of Week and Month", fontsize=14, fontweight="bold")
        plt.xlabel("Month")
        plt.ylabel("Day of Week")
        plt.tight_layout()
        path = os.path.join(self.output_dir, "activity_heatmap.png")
        plt.savefig(path, dpi=150)
        plt.close()
        print(f"Saved: {path}")

    def generate_all_visualizations(self):
        """Runs all four required visualizations."""
        if not self.statistics:
            self.calculate_statistics()
        print("\nGenerating visualizations...")
        self.visualize_top_books()
        self.visualize_monthly_trend()
        self.visualize_genre_distribution()
        self.visualize_activity_heatmap()
        print("All visualizations generated.\n")


# ==========================================================================
# MAIN EXECUTION / EXAMPLE WORKFLOW
# ==========================================================================
def main():
    csv_path = sys.argv[1] if len(sys.argv) > 1 else "library_transactions.csv"

    dashboard = LibraryDashboard(output_dir="output_charts")

    # 1. Input Validation & Loading
    dashboard.load_data(csv_path)

    # 2. Statistics Calculation
    dashboard.calculate_statistics()

    # 3. Data Filtering example: Fantasy books borrowed for more than 10 days
    filtered = dashboard.filter_transactions(genre="Fantasy", min_duration=10)
    print(f"Example filter result (Fantasy, >=10 days): {len(filtered)} rows\n")

    # 4. Report Generation
    dashboard.generate_report()

    # 5. Visualizations
    dashboard.generate_all_visualizations()


if __name__ == "__main__":
    main()
