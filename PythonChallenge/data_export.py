import pandas as pd

#create variable of csv file

#read csv file
df = pd.read_csv('data.csv', sep = ',')

pd.melt(df,
        id_vars = ['Hierarchy', 'Dept', 'Emp ', 'Alpha', 'Bravo', 'Charlie'],
        value_vars = ['01/01/2018', '08/01/2018'],
        var_name = 'Date',
        value_name = 'Value')

df2 = pd.melt(df)

df2.to_csv('new_data.csv')
