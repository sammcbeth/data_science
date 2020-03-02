import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5, 4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
# print(df)
# print(df['W'])
# print(df.W)
# print(df[["W", "Z"]]) # to show multiple columns pass them in as a list

# df['new'] = df['W'] + df['Y']
# print(df)
# df.drop('new', axis=1, inplace=True)
# print(df)
# # df.drop('E', axis=0, inplace=True)
# # print(df)

# # print(df.shape)
# print(df.loc['A'])

# print(df.iloc[3])

# print(df.loc['B', 'Y'])
# print(df.loc[['A', "B"], ['W', 'Y']])

# booldf = df > 0
# print(booldf)
# print(df[booldf])
# print(df[df > 0])

# print(df['W'] > 0)
resultDF = df[df['W'] > 0]
# print(df[df['Z'] < 0])

# print(df[df['W'] > 0][['X', 'Y']])

# print(df[(df['W'] > 0) & (df['Y'] > 1)])

# print(df.reset_index())

# newind = 'CA NY WY OR CO'.split()
# print(newind)
# df['States'] = newind
# print(df.set_index('States'))

# Index Levels
outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]
hier_index = list(zip(outside, inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

df = pd.DataFrame(randn(6, 2), hier_index, ['A', 'B'])
print(df)
# print(df.loc['G1'].loc[1])
df.index.names = ['Groups', 'Num']
print(df.loc['G2'].loc[1]['B'])
