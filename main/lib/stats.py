import pandas as pd
import lib.FeatureEngineering as fe
from numpy.random import RandomState

default = 'data/iris.csv'

class stats:
    
    def __init__(self, data=default,f='csv'):
        data = fe.data(data)
        data = data.data_cleanup(f)
        data = fe.data(data)
        data = data.data_engineering()
        self.data = data
        

    def split_train_test(self):
        """
        Splits the input dataset into training and testing datasets with a 70-30 split
        param data: CSV dataset
        returns: Two DataFrames with training and testing data
        """
        df = self.data
        random_generator = RandomState()
        train = df.sample(frac = 0.7, random_state = random_generator) #70-30 split
        test = df.loc[~ df.index.isin(train.index)] #selecting all rows that are not in train
        return train, test
    
    def five_number_summary(self, data):
        """
        Calculates the five number summary of a dataset (the minimum, Q1, the median, Q3, maximum)
        param data: CSV dataset
        returns: A DataFrame with the five number summary of the dataset
        """
        result = []
        df = data
        num_cols = list(df.select_dtypes(['int64' , 'float64'])) #Selecting only numerical features for analysis
        for col in num_cols:
            sorted_list = sorted(list(df[col]))
            ##MEDIAN##
            median_val = self.median(sorted_list)
            ##MINIMUM##
            minimum_val = sorted_list[0]
            ##MAXIMUM##
            maximum_val = sorted_list[-1]
            ##QUARTILES##
            q1_val, q3_val = self.calc_quartiles(sorted_list)
            result.append([col, minimum_val, q1_val, median_val, q3_val, maximum_val])
        five_num_df = pd.DataFrame(result, columns=['feature', 'minimum', 'q1', 'median', 'q3', 'maximum'])
        return five_num_df
    
    def median(self, x):
        """
        Calculates the median (middle value) of a sorted list x
        Takes average of 2 middle-most values if length of x is even
        param x: A sorted list of numbers
        returns: A median value of the elements of the iterable
        """
        if len(x)%2==0:                                                #Condition to check if the length of x_sorted is even
            mid_up_index = len(x)//2
            mid_down_index = len(x)//2 - 1
            median_val = (x[mid_down_index]+x[mid_up_index])/2      #If true, calculate the median as the average of the two middle most values of x_sorted
        else:
            mid_index = len(x)//2
            median_val = x[mid_index]                                      #If false, calculate the median as the middle most value of x_sorted
        return median_val
    
    def calc_quartiles(self, x):
        """
        Calculates the first and third quartiles of a sorted list x (Q1 & Q3)
        In an even-length list of 2n numbers, Q1 = median of smallest n numbers, Q3 = median of largest n numbers
        In an odd-length list of 2n+1 numbers, Q1 = median of smallest n+1 numbers, Q3 = median of largest n+1 numbers
        param x: A list of sorted numbers
        returns: Two numeric values; the first and third quartiles of a sorted list x (Q1 & Q3)
        """
        
        mid_index = len(x)//2                                                 #Finding midpoint of x
        q3 = self.median(x[mid_index:])                                            #Setting q3 = median of largest numbers
        if len(x)%2==0:                                                       #Condition to check if the length of x is even
            q1 = self.median(x[0:mid_index])                                       #If true, q1 = median of smallest n numbers
        else:
            q1 = self.median(x[0:mid_index+1])                                     #If false, q1 = median of smallest n+1 numbers
        return q1, q3                                                         #Return result of q1, q3

