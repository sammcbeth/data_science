import numpy as np

arr = np.arange(0, 11)

# print(arr[:6])

# print(arr[5:])

# arr[0:5] = 100
# print(arr)
# slice_of_arr = arr[0:5]
# slice_of_arr[:] = 99

# print(arr)

# arr_copy = arr.copy()

# arr_copy[:] = 100
# print(arr)
# print(arr_copy)

# array_2d = np.array([[5, 10, 15], [20, 25, 30], [35, 40, 45]])
# # print(array_2d[2, 1])

# print(array_2d[:2, 1:])
# bool_arr = arr > 5
# print(bool_arr)
# print(arr[bool_arr])
# print(arr[arr > 5])
# print(arr[arr < 3])

# arr_2d = np.arange(50).reshape(5, 10)
# print(arr_2d[1:3, 3:5])

print(arr * 100)
print(np.max(arr))
