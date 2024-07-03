import ccxt
import pandas as pd
import numpy as np
import csv
from datetime import datetime

# Load API keys from dontshareconfig.py
from dontshareconfig import api_key, api_secret

# Create an instance of the Binance exchange
binance = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret,
})

def fetch_ohlcv(symbol, timeframe, limit=500):
    ohlcv = binance.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)
    return ohlcv

def calculate_support_resistance(data, window=50):
    # Ensure there are enough data points to calculate rolling window
    if len(data) < window:
        data['support'] = np.nan
        data['resistance'] = np.nan
    else:
        # Calculate support and resistance levels using rolling min and max
        data['support'] = data['low'].rolling(window=window, min_periods=1).min()
        data['resistance'] = data['high'].rolling(window=window, min_periods=1).max()

        # Forward fill the NaN values
        data['support'] = data['support'].ffill()
        data['resistance'] = data['resistance'].ffill()
    
    return data

# Define the symbol and timeframe
symbol = 'SOL/USDT'
timeframes = ['1d', '1h']

for timeframe in timeframes:
    # Fetch OHLCV data
    data = fetch_ohlcv(symbol, timeframe)
    
    # Create a DataFrame
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    
    # Calculate support and resistance levels
    df = calculate_support_resistance(df)
    
    # Convert timestamp to readable format
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    
    # Save the data to a CSV file
    filename = f'SOL_USDT_{timeframe}_data.csv'
    df.to_csv(filename, index=False)
    print(f'Data saved to {filename}')
