# -*- coding: utf-8 -*-
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
        The data_engineering function is designed to work on the dataframe to One Hot Encode the data which allows
        categorical data to be converted to a series of 0s and 1s by adding labeled columns to the table.
        This increases the dimensionality but also allows more data to be used for analysis.
        param df: A pandas dataframe
        returns: Updated One Hot encoded df with outliers removed as per 3 sigma rule
        """
        df = self.dataset

        # One Hot Encoding
        df = pd.get_dummies(df)
        # Applying 3 sigma rule to remove outliers
        # df[(np.abs(stats.zscore(df)) < 3).all(axis=1)]
        
        return df