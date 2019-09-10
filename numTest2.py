import numpy as np

arr1 = np.array([[1, 2, 3]])
print(arr1.reshape(3, 1))
arr2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
hstack = np.hstack((arr1.reshape(3, 1), arr2))
print(hstack)
