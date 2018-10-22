"""
    Transforms Data into Desired Format
"""

#import pandas module
import pandas as pd

#create variable where df = to data.csv
df = pd.read_csv('data.csv')

#create new variable for df.columns
cols = df.columns
#use .melt() function to complete data manipulation
transformed_df = pd.melt(df,
                         id_vars=cols[:6],
                         value_vars=cols[6:])

#Assert Data has been formatted correctly
print(transformed_df)

#create new csv file with new data
transformed_df.to_csv('melted_data.csv')

print("\nData has been Melted!")

