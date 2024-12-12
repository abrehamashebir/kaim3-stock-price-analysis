
import pandas as pd



def data_loader(file_path):
    """
    Load news data related to stock market

    Args:
        file_path(str): Path to the CSV file
    
    Returns:
           loaded data in the form of DataFrame  
    
    """
    data = pd.read_csv(file_path)

    return data
