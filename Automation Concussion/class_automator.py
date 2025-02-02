##Goals:##

#Get count of num of patients in each bucket 

import csv
import pandas as pd
import numpy as np

#read csv file
def read_csv(df):
    pd.read_csv(df).head()

# clean dataset to get max number of rows x columns
def clean_data(df, col_threshold=.9, row_threshold=.8, threshold_step=0.1):
    # Convert percentage thresholds to proportions
    col_threshold, row_threshold = col_threshold, row_threshold

    # Iteratively clean data
    while True:
        # Calculate null ratios
        row_null_ratios = df.isnull().mean(axis=1)
        col_null_ratios = df.isnull().mean()
        

        # Remove rows with null ratios above row threshold
        rows_to_drop = row_null_ratios[row_null_ratios > row_threshold].index
        df.drop(index=rows_to_drop, inplace=True)
        
        # Remove columns with null ratios above column threshold
        cols_to_drop = col_null_ratios[col_null_ratios > col_threshold].index
        df.drop(columns=cols_to_drop, inplace=True)
        

        # Update thresholds by reducing them for the next iteration
        row_threshold = max(0, row_threshold - threshold_step)
        col_threshold = max(0, col_threshold - threshold_step)


        # Stop condition if no columns or rows exceed the thresholds
        if all(col_null_ratios <= col_threshold) and all(row_null_ratios <= row_threshold):
            break

    return df

def bucket_count(df):
    pass
#- get count of # patients by bucket


#Get average days 2 clearance for each bucket