import yfinance as yf
import mplfinance as mpf
import numpy as np

# Setting Ticker and Downloading Data:
ticker = "AAPL"
data = yf.download(ticker, start='2024-01-01', end='2024-02-02')

print(data)

mpf.plot(data)

mpf.plot(data, type='candle')

data = yf.download(ticker, start='2024-01-01', end='2024-02-02')
mpf.plot(data, type='renko')
mpf.plot(data, type='pnf')