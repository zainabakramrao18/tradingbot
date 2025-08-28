import ccxt
import pandas as pd
import ta
import time

# Set up exchange
exchange = ccxt.binance({
    'apiKey': 'dzD92Pmgj3LVTbbD586oceRYJpdvzG34g52FvDoA0I9T4qQXmkrjtrL1TTEIMpMk',
    'secret': '5Mc1MduCbYr7JTyzE2hoaOh5a5oHgzfyj5CUEf3QbLdxOVULUBaUnfWNAhTIBsRB',
})

symbol = 'BTC/USDT'
timeframe = '15m'  # Changed from 1h to 15m

def fetch_data():
    bars = exchange.fetch_ohlcv(symbol, timeframe, limit=100)
    df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    return df

def rsi_strategy(df):
    df['rsi'] = ta.momentum.RSIIndicator(df['close']).rsi()
    last_rsi = df['rsi'].iloc[-1]
    if last_rsi < 30:
        print("BUY Signal")
    elif last_rsi > 70:
        print("SELL Signal")
    else:
        print("HOLD")

while True:
    df = fetch_data()
    rsi_strategy(df)
    time.sleep(60 * 15)  # Wait for 15 minutes before checking again
