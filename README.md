# Crypto Trading Bot (RSI Strategy)

This is a simple crypto trading bot built with **Python** that uses the **RSI (Relative Strength Index)** indicator to generate **BUY, SELL, or HOLD** signals on the **Binance exchange**.

---

## 🚀 Features
- Connects to Binance using the `ccxt` library.
- Fetches **15-minute candlestick (OHLCV) data** for BTC/USDT.
- Uses the **RSI indicator** from the `ta` library.
- Prints simple trading signals:
  - `BUY` when RSI < 30
  - `SELL` when RSI > 70
  - `HOLD` otherwise
- Runs continuously, checking signals every 15 minutes.

---

## 🛠️ Requirements
Make sure you have Python installed, then install dependencies:

```bash
pip install ccxt pandas ta
