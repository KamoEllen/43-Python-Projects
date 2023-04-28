import pandas as pd
import matplotlib.pyplot as plt

#data into dataframe ,read_csv() 
df = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/AAPL,GOOG,MSFT?period1=1459363200&period2=1617235200&interval=1d&events=history&includeAdjustedClose=true', index_col='Date', parse_dates=True)

print(df.head())

# Calculate the daily returns
returns = df.pct_change()

# Calculate the moving averages
ma_20 = df.rolling(window=20).mean()
ma_50 = df.rolling(window=50).mean()

volatility = returns.rolling(window=20).std()

# Create a new DataFrame to store the calculated values
df_new = pd.DataFrame({
    'AAPL': df['Adj Close']['AAPL'],
    'GOOG': df['Adj Close']['GOOG'],
    'MSFT': df['Adj Close']['MSFT'],
    'AAPL Returns': returns['Adj Close']['AAPL'],
    'GOOG Returns': returns['Adj Close']['GOOG'],
    'MSFT Returns': returns['Adj Close']['MSFT'],
    'AAPL MA 20': ma_20['Adj Close']['AAPL'],
    'GOOG MA 20': ma_20['Adj Close']['GOOG'],
    'MSFT MA 20': ma_20['Adj Close']['MSFT'],
    'AAPL MA 50': ma_50['Adj Close']['AAPL'],
    'GOOG MA 50': ma_50['Adj Close']['GOOG'],
    'MSFT MA 50': ma_50['Adj Close']['MSFT'],
    'AAPL Volatility': volatility['Adj Close']['AAPL'],
    'GOOG Volatility': volatility['Adj Close']['GOOG'],
    'MSFT Volatility': volatility['Adj Close']['MSFT']
})

# Create line charts for the daily stock prices
df_new[['AAPL', 'GOOG', 'MSFT']].plot(figsize=(10, 5))
plt.title('Daily Stock Prices')
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()

# Create candlestick charts for the open, high, low, and close prices
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates

# Resample the data to weekly frequency
df_weekly = df_new.resample('W').agg({
    'AAPL': 'last',
    'GOOG': 'last',
    'MSFT': 'last',
    'AAPL Volatility': 'last',
    'GOOG Volatility': 'last',
    'MSFT Volatility': 'last',
    'AAPL Returns': 'sum',
    'GOOG Returns': 'sum',
    'MSFT Returns': 'sum'
})

# Convert the date index to a numerical format
df_weekly['Date'] = mdates.date2num(df_weekly.index)

# Create the subplots for the candlestick charts
fig, ax = plt.subplots(figsize=(10, 5))

# Plot the candlestick charts for AAPL, GOOG, and MSFT
candlestick_ohlc(ax, df_weekly[['Date', 'AAPL Open', 'AAPL High', 'AAPL Low', 'AAPL Close']].values, width=0.6)
candlestick_ohlc(ax, df_weekly[['Date', 'GOOG Open', 'GOOG High', 'GOOG Low', 'GOOG Close']].values, width=0.6)
candlestick_ohlc(ax, df_weekly[['Date', 'MSFT Open', 'MSFT High', 'MSFT Low', 'MSFT Close']].values, width=0.6)

# Set the x-axis tick labels to show the dates
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))

# Set the title and axis labels
plt.title('Candlestick Charts')
plt.xlabel('Date')
plt.ylabel('Price')

plt.show()
