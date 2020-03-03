import pandas as pd
import numpy as np

d = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}

df = pd.DataFrame(d)
print(df)
# print(df.dropna(axis=1))
# print(df.dropna(thresh=2))
print(df.fillna(value=df['A'].mean()))
