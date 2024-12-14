
import pandas as pd
import yfinance as yf
import talib as ta

class Finanicial_Data:
    def __init__(self):
        pass
      
    def __init__(self,ticker, start, end):
        self.ticker =ticker
        self.start=start
        self.end =end
    
  
    
    def fetch_store_data(self):

        return yf.download(ticker=self.ticker,start=self.start, end=self.end)
    
    def stock_moving_average(self,data, window):
        """
        Moving average of a given stock data price

        Args:
           data(pd.series): the  data source
           window: the window size 

        Returns:
              data rolling
        """

        return ta.SMA(data, timeperiod =window)
    
    def data_loader(self,file_path):

        """
         Load news data related to stock market

        Args:
        file_path(str): Path to the CSV file
    
         Returns:
           loaded data in the form of DataFrame  
    
          """
        data = pd.read_csv(file_path)
        return data
