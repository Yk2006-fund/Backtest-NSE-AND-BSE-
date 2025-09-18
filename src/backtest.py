src/backtest.py
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download stock data
df = yf.download("AAPL", start="2020-01-01", end="2023-01-01")

# Simple strategy: 50/200-day moving average crossover
df["SMA50"] = df["Adj Close"].rolling(50).mean()
df["SMA200"] = df["Adj Close"].rolling(200).mean()

# Position: 1 if SMA50 > SMA200, else 0
df["Position"] = (df["SMA50"] > df["SMA200"]).astype(int)

# Strategy returns
df["Returns"] = df["Adj Close"].pct_change()
df["Strategy"] = df["Position"].shift(1) * df["Returns"]

# Equity curve
df["Equity"] = (1 + df["Strategy"]).cumprod()

# Save metrics
total_return = df["Equity"].iloc[-1] - 1
print(f"Total return: {total_return:.2%}")

# Plot equity curve
plt.figure(figsize=(10,5))
plt.plot(df.index, df["Equity"], label="Strategy")
plt.legend()
plt.title("SMA Crossover Backtest")
plt.savefig("results/equity.png")
plt.close()

# Save CSV of results
df.to_csv("results/backtest_results.csv")





