
import pandas as pd

def stock_moving_average(data, window):

    """
    Moving average of a given stock data price

    Args:
        data(pd.series): the  data source
        window: the window size 

    Returns:
         data rolling
    """

    return data.rolling(window=window).mean()