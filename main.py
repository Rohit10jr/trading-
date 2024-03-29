import yfinance as yf
import mplfinance as mpf
import numpy as np
import psycopg2
import pandas as pd

def load_stock_data_from_postgres(symbol):
    conn = psycopg2.connect(
        dbname="stock_data_db",
        user="your_username",
        password="your_password",
        host="your_host",
        port="your_port"
    )
    cursor = conn.cursor()

    query = f"SELECT date, close FROM stock_data WHERE symbol = '{symbol}'"
    cursor.execute(query)
    rows = cursor.fetchall()

    stock_data = pd.DataFrame(rows, columns=["date", "close"])
    
    conn.close()

    return stock_data

# Setting Ticker and Downloading Data:
ticker = "AAPL"
data = yf.download(ticker, start='2024-01-01', end='2024-02-02')

print(data)

mpf.plot(data)

mpf.plot(data, type='candle')

data = yf.download(ticker, start='2024-01-01', end='2024-02-02')
mpf.plot(data, type='renko')
mpf.plot(data, type='pnf')

