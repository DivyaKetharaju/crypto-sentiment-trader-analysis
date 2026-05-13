# Crypto Sentiment Trader Analysis

## Overview

This project analyzes the relationship between Bitcoin market sentiment and trader performance using:

- Bitcoin Fear & Greed Index
- Hyperliquid historical trader data

The objective is to uncover behavioral patterns, profitability trends, and risk characteristics under different market sentiment conditions.

---

# Datasets

## 1. Bitcoin Fear & Greed Index
Contains:
- sentiment classification
- market emotion indicators
- daily sentiment data

Columns:
- timestamp
- value
- classification
- date

---

## 2. Hyperliquid Historical Trader Data

Contains:
- trader account activity
- execution prices
- trade sizes
- closed profit/loss
- timestamps
- trading direction

Columns:
- Account
- Coin
- Execution Price
- Size Tokens
- Size USD
- Side
- Timestamp
- Closed PnL
- Direction
- etc.

---

# Project Objectives

- Analyze trader profitability across market sentiments
- Compare win rates during Fear vs Greed periods
- Identify behavioral trading patterns
- Discover hidden risk trends
- Generate actionable trading insights

---

# Technologies Used

- Python
- Pandas
- Matplotlib
- Seaborn

---

# Project Structure

```text
crypto_sentiment_analysis_project/
│
├── data/
│   ├── historical_data.csv
│   └── fear_greed.csv
│
├── outputs/
│   └── charts/
│
├── analysis.py
├── requirements.txt
└── README.md
```

---

# Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Run the Project

```bash
python analysis.py
```

---

# Features

## Data Cleaning
- Timestamp conversion
- Dataset merging
- Missing value handling

## Exploratory Data Analysis
- Profit/Loss analysis
- Win rate analysis
- Sentiment comparison

## Visualization
- PnL by sentiment
- Win rate by sentiment

---

# Key Analysis Performed

## 1. Profitability Analysis
Analyzed total and average trader profit under:
- Fear
- Extreme Fear
- Greed
- Extreme Greed

## 2. Win Rate Analysis
Compared trader success rates across different market sentiments.

## 3. Behavioral Insights
Explored how trader behavior changes during emotional market conditions.

---

# Example Insights

- Traders tend to overtrade during Extreme Greed
- Fear periods often reduce aggressive trading behavior
- Profitability varies significantly with sentiment conditions

---

# Output

Generated charts are saved in:

```text
outputs/charts/
```

Examples:
- pnl_by_sentiment.png
- win_rate_by_sentiment.png

---

# Future Improvements

- Add machine learning models
- Build Streamlit dashboard
- Add leverage/risk analysis
- Create interactive visualizations
- Add Sharpe ratio and drawdown analysis

---

# Author

Ketharaju Divya

## Key Goals
- Analyze trader performance under different market sentiments
- Discover leverage and risk behavior patterns
- Generate actionable trading insights

## How to Run
1. Place datasets inside the data/ folder
2. Open notebooks/analysis.ipynb
3. Run all cells
