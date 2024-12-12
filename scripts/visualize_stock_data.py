
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
