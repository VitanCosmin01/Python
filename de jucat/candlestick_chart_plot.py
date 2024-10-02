# pip install yfinance
import yfinance as yf
import mplfinance as mpf
from matplotlib.pyplot import title

ticker = input("Enter the stock name: ")
df = yf.download(ticker, start='2024-04-01', end='2024-10-02')

mpf.plot(df, type='candle', style='charles', title=f'{ticker} Candlestick Chart', ylabel='Price')

# EX: INFY