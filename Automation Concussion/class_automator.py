##Goals:##

#Get count of num of patients in each bucket 

import pandas as pd

class ConcussionAutomator:
    
    def __init__(self,df):
    #read csv file
        self.df = pd.read_csv(df)

    # clean dataset to get max number of rows x columns
    def clean_data(self, col_threshold=0.9, row_threshold=0.8, threshold_step=0.1):
        
        #run automation on copy of df
        df = self.df.copy() 

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

            # Update thresholds for the next iteration
            row_threshold = max(0, row_threshold - threshold_step)
            col_threshold = max(0, col_threshold - threshold_step)

            # Stop condition if no more rows/columns exceed thresholds
            if all(col_null_ratios <= col_threshold) and all(row_null_ratios <= row_threshold):
                break

        self.df = df 
        
    #- get count of # patients by bucket
    def bucket_count(self):
        bucket_1 = self.df['buckets'].value_counts().get(1,0)
        bucket_2 = self.df['buckets'].value_counts().get(2,0)
        print(f"Number of patients recovered under a month: {bucket_1}\n")
        print(f"Number of patients recovered exactly one month and over: {bucket_2}\n")
        
        
    #Get average days 2 clearance for each bucket

        
    def run(self):
        print("Concusion Patient Dataset Analyzer")
        print("---------------------------------------")
        self.clean_data()
        self.bucket_count()
        print("---------------------------------------")



#add time taken to run program