import numpy as np


my_mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr = np.array(my_mat)
# print(arr)

# print(np.arange(0, 11, 2))

# print(np.zeros((2, 3)))
# print(np.ones((2, 3)))

# print(np.linspace(0, 5, 10))


# print(np.eye(4))

# print(np.random.rand(5, 5))

# print(np.random.randint(1, 100, 10))

# arr = np.arange(25)
# print(arr)
ranarr = np.random.randint(0, 50, 10)
print(ranarr)

# print(arr.reshape(5, 5))

print(ranarr.max())
print(ranarr.min())
print(ranarr.argmax())
print(ranarr.argmin())
print(ranarr.shape)
print(arr.dtype)
