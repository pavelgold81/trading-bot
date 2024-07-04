# Trading Bot

## Project Overview
This project involves creating a trading bot for educational purposes. The bot is designed to demonstrate various trading strategies and techniques using historical and real-time market data. The goal is to provide a hands-on learning experience for individuals interested in algorithmic trading and financial markets.

## Features
- **Automated Data Retrieval**: Fetches OHLCV (Open, High, Low, Close, Volume) data from the Binance exchange using the CCXT library.
- **Technical Analysis**: Calculates support and resistance levels using rolling window functions.
- **CSV Data Storage**: Stores retrieved and processed market data in CSV files for easy analysis and backtesting.

## Getting Started
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/pavelgold81/trading-bot.git
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure API Keys**:
   Create a file named `dontshareconfig.py` and add your Binance API key and secret.

4. **Run the Bot**:
   ```bash
   python get_data.py
   ```

## Project Structure
- `get_data.py`: Script to fetch market data and calculate support and resistance levels.
- `breakout_strategy.py`: Example of a breakout trading strategy using support and resistance levels.
- `dontshareconfig.py`: Configuration file to store API keys (not included in the repository for security reasons).
- `SOL_USDT_1d_data.csv`, `SOL_USDT_1h_data.csv`: Sample CSV files containing OHLCV data for the SOL/USDT trading pair.
# trading-bot
Creating a trading bot for education purpose
