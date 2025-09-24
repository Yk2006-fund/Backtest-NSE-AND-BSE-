import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# Fetch data
ticker = "RELIANCE.NS"
data = yf.download(ticker, start="2020-01-01", end="2023-01-01")

# Create SMAs
data["SMA20"] = data["Close"].rolling(20).mean()
data["SMA50"] = data["Close"].rolling(50).mean()

# Generate signals
data["Signal"] = 0
data["Signal"][20:] = (data["SMA20"][20:] > data["SMA50"][20:]).astype(int)
data["Position"] = data["Signal"].diff()

# Plot
plt.figure(figsize=(12,6))
plt.plot(data["Close"], label="Close Price")
plt.plot(data["SMA20"], label="SMA20")
plt.plot(data["SMA50"], label="SMA50")
plt.legend()
plt.title(f"SMA Crossover Backtest - {ticker}")
plt.savefig("results/sma_crossover.png")
plt.show()
