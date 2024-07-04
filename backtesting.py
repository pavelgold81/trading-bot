import pandas as pd
from backtesting import Backtest, Strategy
from backtesting.lib import crossover
from backtesting.test import SMA
from datetime import datetime

# Load daily data
daily_data_path = '/Users/pgoldenshtein/Dropbox/trading-bot/SOL_USDT_1d_data.csv'
daily_data = pd.read_csv(daily_data_path, parse_dates=['timestamp'])

# Load hourly data
hourly_data_path = '/Users/pgoldenshtein/Dropbox/trading-bot/SOL_USDT_1h_data.csv'
hourly_data = pd.read_csv(hourly_data_path, parse_dates=['timestamp'])

# Define the Breakout Strategy
class BreakoutStrategy(Strategy):
    atr_period = 14

    def init(self):
        self.daily_resistance = self.I(lambda: daily_data['resistance'], name='resistance')
        self.atr = self.I(SMA, self.data.Close, self.atr_period)

    def next(self):
        # Get the previous day's resistance level
        daily_resistance = self.daily_resistance[-1]

        # Check for breakout on the hourly data
        if self.data.Close[-1] > daily_resistance:
            breakout_point = self.data.Close[-1]
            entry_price = (daily_resistance + breakout_point) / 2
            stop_loss = entry_price - self.atr[-1]
            self.buy(sl=stop_loss)

# Prepare the data for backtesting
hourly_data['date'] = hourly_data['timestamp'].dt.date
daily_data['date'] = daily_data['timestamp'].dt.date

# Merge daily resistance into hourly data
merged_data = pd.merge(hourly_data, daily_data[['date', 'resistance']], on='date', how='left')

# Fill forward resistance values for intra-day data
merged_data['resistance'] = merged_data['resistance'].fillna(method='ffill')

# Prepare data for backtesting.py
merged_data.set_index('timestamp', inplace=True)

# Run the backtest
bt = Backtest(merged_data, BreakoutStrategy, cash=100000, commission=.002)
stats = bt.run()
bt.plot()

# Print the stats
print(stats)
