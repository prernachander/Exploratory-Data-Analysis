"""
Created on Sat Aug  6 00:37:01 2022

@author: bornf
"""
import os
import pandas as pd
import numpy as np
from scipy import stats

class data:
    
    def __init__(self, dataset = 'data/iris.csv'):
        self.dataset = dataset
        
    def drop_const(self, df):
        """
        The drop_const function is designed to drop all columns that have a constant value and any rows that have NaN entries
        to reduce the dimensionality of the dataset from incomplete data.
        param df: A pandas dataframe
        returns: Updated df
        """
        # Dropping constant columns
        df = df.loc[:, (df != df.iloc[0]).any()]
        # Dropping rows that have NaN
        df = df.dropna(axis=0)
        
        return df
    
    def data_cleanup(self, f):
        """
        The data_cleanup function is designed to identify the type of file that has been passed to the class object, read
        the file in the correct format to initialize the dataframe and utilise the drop_const function to cleanup the dataframe.
        params fileName, f: fileName with the file path, and f is a flag for the file extension
        returns: Cleaned up df or raises a ValueError if the file is not in standard format
        """
        fileName = self.dataset
        # Initializing the file extension to the ext variable
        if isinstance(fileName, pd.DataFrame):
            pass
        else:
            ext = os.path.splitext(fileName)[1]
        # Checking if the ext and f are equal and a valid extension
        if ext in ['.csv','.xlsx','.json','.tsv']:
            if f == ext[1:]:
                # Using the match-case statement to identify which file type has been passed to use the apt pandas read function
                match f:
                    case 'csv':  
                        df = pd.read_csv(fileName)
                        df = self.drop_const(df)
                    case 'xlsx':  
                        df = pd.read_excel(fileName)
                        df = self.drop_const(df)
                    case 'tsv':  
                        df = pd.read_table(fileName)
                        df = self.drop_const(df)
                    case 'json':  
                        df = pd.read_json(fileName)
                        df = self.drop_const(df)
                
                return df
            # If it is not any of the aforementioned file types then raise the ValueError
            else:
                raise ValueError('Expected ' + f +' file, received '+ os.path.splitext(fileName)[1][1:] + ' file instead' )
        else:
            raise ValueError('[Unknown File Type] Expected csv, xlsx, json or tsv, received ' + os.path.splitext(fileName)[1][1:] + ' file instead')
            
    def data_engineering(self):
        """
        The data_engineering function is designed to work on the dataframe to apply the 3 sigma rule for outlier removal.
        The 3 sigma rule is a statistical calculation which states that all data that lies outside 3 standard
        deviations from the mean is a statistical outlier and may be removed to improve the analysis on the dataset.
        returns: Updated df with outliers removed as per 3 sigma rule
        """
        df = self.dataset        
        # Selecting only numerical features for analysis
        if isinstance(df, pd.DataFrame):
            num_cols = list(df.select_dtypes(['int64' , 'float64'])) 
            for col in num_cols:
                df[(np.abs(stats.zscore(df[col])) < 3)] # Applying 3 sigma rule to remove outliers
            
            return df
        else:
            raise ValueError('[Unknown File Type] Expected pandas DataFrame')