# E-Library Data Insights Dashboard

A Python-based dashboard for managing and analyzing e-library book borrowing
trends. Built using **Control Structures, Arrays, OOP, NumPy, Pandas, and
Matplotlib/Seaborn**.

## Project Description

This project processes a library transaction log (`library_transactions.csv`)
and produces:

- Data validation and cleaning (missing values, duplicates, invalid entries)
- Key statistics: most borrowed book, average/median/std. dev. of borrowing
  duration, busiest day of the week, late-return rate, and more
- Flexible filtering by genre, date range, and borrowing duration
- A written summary report (`output_charts/summary_report.txt`)
- Four visualizations saved as PNG files:
  1. **Bar Chart** — Top 5 most borrowed books
  2. **Line Graph** — Borrowing trends over months
  3. **Pie Chart** — Distribution of books borrowed by genre
  4. **Heatmap** — Borrowing activity by day of week and month

All functionality is encapsulated in a single `LibraryDashboard` class.

## Files

| File                          | Description                                              |
|--------------------------------|-----------------------------------------------------------|
| `library_dashboard.py`         | Main script containing the `LibraryDashboard` class       |
| `library_transactions.csv`     | Sample dataset (AI-generated, 1500+ transactions)          |
| `generate_dataset.py`          | Script used to generate the sample CSV (optional, for reference) |
| `README.md`                    | This file                                                  |
| `output_charts/`                | Created automatically — contains generated charts + report |

## Setup Instructions

### 1. Requirements

- Python 3.8+
- Install dependencies:

```bash
pip install pandas numpy matplotlib seaborn
```

### 2. Run the Dashboard

From the project directory, run:

```bash
python library_dashboard.py library_transactions.csv
```

If you don't pass a file path, it defaults to `library_transactions.csv` in
the current directory:

```bash
python library_dashboard.py
```

### 3. Output

After running, check the `output_charts/` folder for:

- `summary_report.txt` — full text summary report
- `top_5_books_bar_chart.png`
- `monthly_trend_line_graph.png`
- `genre_distribution_pie_chart.png`
- `activity_heatmap.png`

## Using `LibraryDashboard` Programmatically

```python
from library_dashboard import LibraryDashboard

dashboard = LibraryDashboard()
dashboard.load_data("library_transactions.csv")
stats = dashboard.calculate_statistics()

# Filter examples
fantasy_long_loans = dashboard.filter_transactions(genre="Fantasy", min_duration=10)
q1_transactions = dashboard.filter_transactions(start_date="2025-01-01", end_date="2025-03-31")

dashboard.generate_report()
dashboard.generate_all_visualizations()
```

## Dataset Details

`library_transactions.csv` contains the following columns:

- `Transaction ID`
- `Date` (YYYY-MM-DD)
- `User ID`
- `Book Title`
- `Genre`
- `Borrowing Duration (Days)`

The dataset was synthetically generated (`generate_dataset.py`) to simulate
realistic library activity across 7 genres, 35 books, and 120 users over the
year 2025, and intentionally includes missing values, duplicate rows, and a
few invalid entries so the dashboard's cleaning/validation logic has real
issues to handle.

## Class Reference: `LibraryDashboard`

| Method                                   | Purpose                                                        |
|-------------------------------------------|------------------------------------------------------------------|
| `load_data(file_path)`                    | Loads & validates CSV, cleans missing/duplicate/invalid data     |
| `calculate_statistics()`                  | Computes metrics (NumPy for durations, Pandas for aggregation)   |
| `filter_transactions(**criteria)`         | Filters by genre, date range, duration, or a custom condition    |
| `generate_report()`                       | Prints & saves a text summary report                             |
| `visualize_top_books()`                   | Bar chart of top 5 borrowed books                                 |
| `visualize_monthly_trend()`               | Line graph of monthly borrowing trends                            |
| `visualize_genre_distribution()`          | Pie chart of genre distribution                                   |
| `visualize_activity_heatmap()`            | Heatmap of activity by day/month                                  |
| `generate_all_visualizations()`           | Runs all four visualizations at once                              |
