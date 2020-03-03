import numpy as np
import pandas as pd

df = pd.DataFrame({'col1': [1, 2, 3, 4], 'col2': [
                  444, 555, 666, 444], 'col3': ['abc', 'def', 'ghi', 'xyz']})
# print(df.head())


# print(df['col2'].nunique()) #number of unique values in column
# print(df['col2'].value_counts()) # number of times unique value occurs

# print(df[(df['col1'] > 2) & (df['col2'] == 444)])


def times2(f):
    return f*2


# print(df['col1'].apply(times2))  # apply a function to values in a col
# print(df['col3'].apply(len))
# print(df['col2'].apply(lambda x: x*2))

# print(df.drop('col1', axis=1))

# print(df.columns)
# print(df.index)

# print(df.sort_values('col3'))

# print(df.isnull())

data = {'A': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'],
        'B': ['one', 'one', 'two', 'two', 'one', 'one'],
        'C': ['x', 'y', 'x', 'y', 'x', 'y'],
        'D': [1, 3, 2, 5, 4, 1]}

df = pd.DataFrame(data)
print(df.pivot_table(values='D', index=['A', 'B'], columns=['C']))
