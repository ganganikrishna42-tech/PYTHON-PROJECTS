<div align="center">

# -- ! Air Quality Analysis ! --
### *Exploring Urban Pollution Trends Through Time, Weather & Correlation Analysis*

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data%20Wrangling-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=plotly&logoColor=white)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-4C72B0?style=for-the-badge&logo=python&logoColor=white)](https://seaborn.pydata.org/)

<br/>

> *"You can't manage what you can't measure — and the air we breathe is no exception."*

</div>

---

## 📋 Table of Contents

- [📌 Overview](#-overview)
- [🎯 Problem Statement](#-problem-statement)
- [🗂️ Dataset](#️-dataset)
- [✨ Key Features](#-key-features)
- [🏗️ Project Structure](#️-project-structure)
- [🔄 Project Workflow](#-project-workflow)
- [🧹 Part A — Data Cleaning](#-part-a--data-cleaning)
- [📈 Part B — Time-Based Trends](#-part-b--time-based-trends)
- [🌡️ Part C — Weather Relationships](#️-part-c--weather-relationships)
- [🔗 Part D — Correlation & Distribution Analysis](#-part-d--correlation--distribution-analysis)
- [🛠️ Tech Stack](#️-tech-stack)
- [📊 Results & Insights](#-results--insights)
- [🏆 Advantages](#-advantages)
- [🚀 How to Run](#-how-to-run)
- [📄 License](#-license)
- [🙏 Acknowledgements](#-acknowledgements)

---

## 📌 Overview

The **Air Quality Analysis** project is a data-analytics notebook that explores hourly air quality sensor readings collected in an Italian city, examining how pollutant concentrations evolve **over time**, vary with **weather conditions**, and relate to one another. Using **Pandas** for data wrangling and **Matplotlib/Seaborn** for visualization, the notebook walks through the full analysis pipeline — from raw, messy sensor data to cleaned, resampled time series and correlation heatmaps.

This project is designed to:
- Practice real-world data cleaning (missing values, sentinel codes, malformed timestamps)
- Build time-series aggregations (daily, hourly, monthly resampling)
- Explore relationships between pollutants and weather variables
- Produce a clear, visual narrative of urban air quality patterns

---

## 🎯 Problem Statement

> **Objective:** Analyze a multi-pollutant air quality dataset to uncover temporal patterns and environmental relationships that explain fluctuations in pollution levels.

Air quality sensors continuously log gas concentrations (CO, NOx, NO2, C6H6) alongside temperature and humidity. Raw readings are noisy, contain missing-value sentinels (`-200`), and are logged in a locale-specific date/time format. The goal is to clean this data, then answer questions such as: *When is pollution worst during the day? Does it vary by weekday? How does temperature or humidity affect pollutant levels? Which pollutants move together?*

| 📂 Analysis Area | 📄 Type | 🔍 Description |
|-------------------|---------|-----------------|
| Data Cleaning | Preprocessing | Handles missing sentinels, parses datetimes, interpolates gaps |
| Time-Series Trends | Visualization | Daily/monthly resampled pollutant trends |
| Time-of-Day & Weekday Patterns | Visualization | Hourly and day-of-week pollution averages |
| Weather Relationships | Scatter Analysis | CO vs. temperature, NOx vs. humidity |
| Correlation & Distribution | Statistical | Heatmap, histograms, and pairwise plots |

The goal is to demonstrate a **complete exploratory data analysis (EDA) workflow** on a real, imperfect sensor dataset.

---

## 🗂️ Dataset

| Field | Description |
|-------|-------------|
| 📄 **Source** | UCI Machine Learning Repository — Air Quality Dataset |
| 📁 **File** | `air_quality.csv` |
| 🧾 **Format** | Semicolon-delimited CSV, comma as decimal separator |
| 📊 **Rows** | ~9,357 hourly readings |
| 🧪 **Columns** | `CO(GT)`, `NOx(GT)`, `NO2(GT)`, `C6H6(GT)`, `T` (temperature), `RH` (relative humidity), `AH` (absolute humidity), plus several sensor response columns |
| ⚠️ **Missing Data** | Encoded as `-200`, replaced with `NaN` during cleaning |

---

## ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🧹 **Robust Cleaning** | Drops empty columns, parses `Date`/`Time` into a proper `DateTime` index, replaces sentinel missing values |
| 🔁 **Interpolation** | Fills small gaps in pollutant readings using linear interpolation |
| 🕒 **Time Feature Engineering** | Extracts `Year`, `Month`, `Hour`, and `DayOfWeek` from timestamps |
| 📉 **Daily Resampling** | Aggregates hourly data into daily averages for CO, NOx, NO2, and Benzene |
| 🕐 **Hourly Profiles** | Reveals rush-hour pollution peaks across the day |
| 📅 **Weekday Comparison** | Bar chart of average CO by day of week |
| 📆 **Monthly Trends** | Line plot of monthly pollutant averages across the year |
| 🌡️ **Weather Correlation** | Scatter plots linking temperature/humidity to pollutant levels |
| 🔗 **Correlation Heatmap** | Full pairwise correlation matrix across pollutants and weather |
| 📊 **Distribution Plots** | Histograms with KDE overlays for CO, NOx, and NO2 |
| 🧮 **Pairplot** | Sampled pairwise scatter matrix of pollutants vs. weather |

---

## 🏗️ Project Structure

```
📦 air-quality-analysis/
│
├── 📄 air_quality_analysis.ipynb   ← Main analysis notebook
├── 📄 air_quality.csv              ← Raw sensor dataset
└── 📄 README.md                    ← Project documentation
```

---

## 🔄 Project Workflow

```
Load Raw CSV
      │
      ▼
┌─────────────────────────────┐
│   Drop empty columns/rows   │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Replace -200 with NaN      │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Parse Date + Time → DateTime│
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Interpolate missing values  │
└────────────┬────────────────┘
             │
             ▼
┌─────────────────────────────┐
│  Engineer Year/Month/Hour/  │
│  DayOfWeek features          │
└────────────┬────────────────┘
             │
     ┌───────┴────────────────────────┐
     ▼                                ▼
┌─────────────────┐          ┌─────────────────────┐
│ Time-Series      │          │ Weather & Correlation│
│ Trend Analysis   │          │ Analysis              │
└─────────────────┘          └─────────────────────┘
             │                                │
             └───────────────┬────────────────┘
                              ▼
                    Visual Insights & Report
```

---

## 🧹 Part A — Data Cleaning

### 📝 1. Handling Missing Sentinels

The dataset uses `-200` to mark missing sensor readings. These are replaced with `NaN` so they don't distort statistics or plots.

**Logic:**
```python
df = df.replace(-200, np.nan)
```

### 🕒 2. Parsing Date & Time

Raw timestamps are split across `Date` (`DD/MM/YYYY`) and `Time` (`HH.MM.SS`) columns and combined into a single `DateTime` index.

**Logic:**
```python
df['DateTime'] = pd.to_datetime(
    df['Date'] + ' ' + df['Time'].str.replace('.', ':', regex=False),
    format='%d/%m/%Y %H:%M:%S'
)
df = df.sort_values('DateTime').reset_index(drop=True)
```

### ➕ 3. Interpolating Gaps

Short gaps in key pollutant and weather columns are filled using linear interpolation rather than dropped, preserving the continuity of the time series.

```python
df[['CO(GT)', 'NOx(GT)', 'NO2(GT)', 'T', 'RH', 'AH']] = \
    df[['CO(GT)', 'NOx(GT)', 'NO2(GT)', 'T', 'RH', 'AH']].interpolate()
```

---

## 📈 Part B — Time-Based Trends

### 🔍 4. Daily & Monthly Pollutant Trends

Hourly readings are resampled to daily averages to smooth out noise and reveal longer-term trends for CO, NOx, NO2, and Benzene (C6H6).

```python
daily_co = df.set_index('DateTime')['CO(GT)'].resample('D').mean()
```

### 🕐 5. Hour-of-Day & Day-of-Week Patterns

Grouping by `Hour` and `DayOfWeek` exposes recurring daily rhythms (e.g., traffic-driven pollution peaks) and weekly patterns (weekday vs. weekend differences).

```python
hourly_avg = df.groupby('Hour')[['CO(GT)', 'NOx(GT)', 'NO2(GT)']].mean()
weekday_avg = df.groupby('DayOfWeek')['CO(GT)'].mean().reindex(day_order)
```

---

## 🌡️ Part C — Weather Relationships

### 🔍 6. Temperature & Humidity vs. Pollutants

Scatter plots examine whether temperature or relative humidity relate to CO and NOx concentrations, hinting at atmospheric dispersion effects.

```python
sns.scatterplot(data=df, x='T', y='CO(GT)', alpha=0.3)
sns.scatterplot(data=df, x='RH', y='NOx(GT)', alpha=0.3)
```

---

## 🔗 Part D — Correlation & Distribution Analysis

### 🔍 7. Correlation Heatmap

A correlation matrix across CO, C6H6, NOx, NO2, temperature, relative humidity, and absolute humidity quantifies how strongly these variables move together.

```python
corr = df[['CO(GT)', 'C6H6(GT)', 'NOx(GT)', 'NO2(GT)', 'T', 'RH', 'AH']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt='.2f')
```

### 📊 8. Distributions & Pairwise Relationships

Histograms (with KDE) show the shape of each pollutant's distribution, while a sampled pairplot visualizes pairwise relationships between pollutants and weather variables at a glance.

**Key Concepts Used:**

| Concept | Detail |
|---------|--------|
| 🔁 `resample('D')` | Time-series aggregation to daily frequency |
| 🧮 `groupby()` | Aggregating by hour, month, and day of week |
| 📐 `.interpolate()` | Filling missing values along a continuous series |
| 🔗 `.corr()` | Pearson correlation matrix computation |
| 🎨 Seaborn plots | Heatmaps, histograms, scatterplots, pairplots |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| 🐍 **Python 3.8+** | Core programming language |
| 🐼 **Pandas** | Data loading, cleaning, resampling, and grouping |
| 🔢 **NumPy** | Numerical operations (NaN handling) |
| 📊 **Matplotlib** | Base plotting and figure control |
| 🎨 **Seaborn** | Statistical visualizations (heatmaps, distributions, pairplots) |
| 📓 **Jupyter Notebook** | Interactive analysis environment |

---

## 📊 Results & Insights

After running the notebook, the following outputs are produced:

- ✅ **Cleaned Time Series** — Missing sentinel values replaced and interpolated, malformed timestamps parsed into a proper `DateTime` index
- 📈 **Daily & Monthly Trends** — Smoothed views of CO, NOx, NO2, and Benzene levels across the full monitoring period
- 🕐 **Hourly Pollution Profile** — Clear peaks aligned with expected high-traffic hours
- 📅 **Weekday Patterns** — Comparative CO levels across days of the week
- 🌡️ **Weather Relationships** — Visual evidence of how temperature and humidity relate to pollutant concentration
- 🔗 **Correlation Heatmap** — Quantified relationships between all pollutants and weather variables
- 📊 **Distribution & Pairplots** — Shape and spread of pollutant readings, and their pairwise interactions

---

## 🏆 Advantages

| Advantage | Detail |
|-----------|--------|
| 🎓 **Educational** | Demonstrates a full real-world EDA pipeline, not just toy data |
| 🧹 **Realistic Cleaning** | Handles genuine data-quality issues (sentinels, locale date formats, gaps) |
| 📚 **Reusable Patterns** | Resampling and groupby logic can be adapted to other time-series datasets |
| 🖥️ **Self-Contained** | Single notebook + single CSV, runnable end-to-end without external services |
| 🧪 **Extensible** | Easy to add new pollutants, additional weather variables, or predictive modeling |
| 📖 **Readable Code** | Clear cell-by-cell structure with markdown section headers |

---

## 🚀 How to Run

1. Ensure Python 3.8+ is installed along with `pandas`, `numpy`, `matplotlib`, and `seaborn`.
2. Place `air_quality.csv` in the same directory as the notebook.
3. Open `air_quality_analysis.ipynb` in Jupyter Notebook or JupyterLab.
4. Run all cells sequentially from top to bottom.

```bash
pip install pandas numpy matplotlib seaborn jupyter
jupyter notebook air_quality_analysis.ipynb
```

---

## 📄 License

This project is licensed under the **MIT License** — free to use, modify, and distribute with attribution.

---

## 🙏 Acknowledgements

Special thanks to the following resources that made this project possible:

- 📚 [UCI Machine Learning Repository — Air Quality Dataset](https://archive.ics.uci.edu/dataset/360/air+quality) — Source dataset
- 🐼 [Pandas Documentation](https://pandas.pydata.org/docs/) — Time-series and data-wrangling reference
- 🎨 [Seaborn Documentation](https://seaborn.pydata.org/) — Statistical visualization reference
- 🖼️ [Matplotlib Documentation](https://matplotlib.org/stable/index.html) — Plotting reference

---

<div align="center">

---

*A clean-air analysis, one pollutant at a time.* 🌍

</div>