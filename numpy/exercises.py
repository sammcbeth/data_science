import numpy as np

arrZer = np.zeros(10)
arrOnes = np.ones(10)
arrFives = np.ones(10) * 5
print(arrFives)


arr = np.arange(10, 51)

arr = np.arange(10, 51, 2)

np.arange(9).reshape(3, 3)

np.eye(3)  # generates array with determinant of 1 or just ones in the diagonal 0s elsewhere
np.random.rand(1)  # random number between 0 and 1
# 25 digit array of random numbers from a normal distribution
np.random.randn(25)

print(np.linspace(0.01, 1, 100).reshape(10, 10))
