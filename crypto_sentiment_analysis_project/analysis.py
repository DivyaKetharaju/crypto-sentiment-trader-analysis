import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load datasets
trades = pd.read_csv("data/historical_data.csv")
sentiment = pd.read_csv("data/fear_greed.csv")

# Convert timestamps correctly
trades['Timestamp'] = pd.to_datetime(
    trades['Timestamp'],
    unit='ms'
)

# Convert sentiment date
sentiment['date'] = pd.to_datetime(sentiment['date'])

# Create matching date columns
trades['date'] = trades['Timestamp'].dt.date
sentiment['date'] = sentiment['date'].dt.date

# Merge datasets
merged = trades.merge(
    sentiment[['date', 'classification']],
    on='date',
    how='left'
)

# Remove rows without sentiment
merged = merged.dropna(subset=['classification'])

# Create profit flag
merged['is_profit'] = merged['Closed PnL'] > 0

# Analysis
sentiment_pnl = merged.groupby(
    'classification'
)['Closed PnL'].sum()

avg_pnl = merged.groupby(
    'classification'
)['Closed PnL'].mean()

win_rate = merged.groupby(
    'classification'
)['is_profit'].mean() * 100

# Print outputs
print("\nClassification Counts:")
print(merged['classification'].value_counts())

print("\nTotal PnL:")
print(sentiment_pnl)

print("\nAverage PnL:")
print(avg_pnl)

print("\nWin Rate:")
print(win_rate)

# Create output folder
os.makedirs("outputs/charts", exist_ok=True)

# Plot PnL
plt.figure(figsize=(10,5))

sns.barplot(
    x=sentiment_pnl.index,
    y=sentiment_pnl.values
)

plt.title("Total PnL by Market Sentiment")
plt.xlabel("Market Sentiment")
plt.ylabel("Total PnL")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "outputs/charts/pnl_by_sentiment.png"
)

# Plot Win Rate
plt.figure(figsize=(10,5))

sns.barplot(
    x=win_rate.index,
    y=win_rate.values
)

plt.title("Win Rate by Market Sentiment")
plt.xlabel("Market Sentiment")
plt.ylabel("Win Rate %")
plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "outputs/charts/win_rate_by_sentiment.png"
)

print("\nCharts saved successfully.")
