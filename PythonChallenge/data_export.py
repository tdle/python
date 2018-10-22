"""
    Transforms Data into Desired Format
"""

import pandas as pd

df = pd.read_csv('data.csv')

cols = df.columns
transformed_df = pd.melt(df,
                         id_vars=cols[:6],
                         value_vars=cols[6:])
print(transformed_df)

