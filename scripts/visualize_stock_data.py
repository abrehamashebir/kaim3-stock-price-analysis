
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import talib as ta

def plot_stock(data):
    """
    plot stock data for the given stock

    Args: 
        data(pd.DataFrame): the data to be presented

    """
    plt.figure(figsize=(12,6))
    plt.plot(data['Date'], data['Open'], label='Open Price', color='blue')
    plt.plot(data['Date'], data['moving_average'], label='Moving Average', color='red')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Stock Price')
    plt.legend()
    plt.grid()
    plt.show()


def visualize_moving_average(data):
       plt.figure(figsize=(12, 8))  # Adjust figure size if needed
       plt.subplot(2, 1, 1)  # Two subplots, first one
       plt.plot(data['Close'], label='Close Price')
       plt.plot(data['moving_average'], label='moving_average')
       plt.title('Close Price with moving_average')
       plt.legend()
def visualize_RSI(data):     
       plt.figure(figsize=(12, 8))  # Adjust figure size if needed      
       plt.subplot(2, 1, 2) # Second subplot
       plt.plot(data['RSI'], label='RSI')
       plt.title('RSI')
       plt.axhline(y=30, color='r', linestyle='--') # Overbought/oversold lines
       plt.axhline(y=70, color='r', linestyle='--')
       plt.legend()
       plt.show()
def visualize_MACD(data):
       plt.figure(figsize=(12, 4))
       plt.plot(data['MACD'], label='MACD')
       plt.plot(data['MACD_signal'], label='Signal Line')
       plt.title('MACD')
       plt.legend()
       plt.show()
def visualize_daily_return(data):
       plt.figure(figsize=(12, 4))
       plt.plot(data['Daily_Return'], label="Daily Returns")
       plt.title("Daily Returns")
       plt.legend()
       plt.show()

