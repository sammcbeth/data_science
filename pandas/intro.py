import pandas as pd
import numpy as np

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

# print(pd.Series(data=my_data))
# print(pd.Series(data=my_data, index=labels))
# print(pd.Series(arr, labels))
# pd.Series(d)
# print(d)


ser1 = pd.Series([1, 2, 3, 4], ['USA', 'Germany', 'Japan', 'Italy'])
# print(ser1)
# print(ser1['USA'])

ser2 = pd.Series([1, 2, 5, 4], ['USA', 'Germany', 'Japan', 'Italy'])
ser3 = pd.Series(data=labels)
# print(ser3[0])

print(ser1 + ser2)
