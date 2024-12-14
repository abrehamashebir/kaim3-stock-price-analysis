
import pandas as pd
import yfinance as yf
import talib as ta

def stock_moving_average(data, window): 
        """
        Moving average of a given stock data price

        Args:
           data(pd.series): the  data source
           window: the window size 

        Returns:
              data rolling
        """

        return ta.SMA(data, timeperiod =window)

def RSI_indicator(data, window): 
        """
        Moving average of a given stock data price

        Args:
           data(pd.series): the  data source
           window: the window size 

        Returns:
              data rolling
        """

        return ta.RSI(data, timeperiod =window)

def MACD_indicator(data): 
        """
        Moving average of a given stock data price

        Args:
           data(pd.series): the  data source
           window: the window size 

        Returns:
              data rolling
        """

        return ta.MACD(data)