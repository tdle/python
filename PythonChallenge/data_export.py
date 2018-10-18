#import pandas module
import pandas as pd

#create dataframe variable of csv file I want to read
df = pd.read_csv('data.csv')

#Perform melt
pd.melt(df,
        id_vars=df.columns[:-2],
        value_vars=df.columns[-2:],
        var_name='Date',
        value_name='Value')



#print table contents to assert code is working

#write new data to table

#print new table to confirm code is working