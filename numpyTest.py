import numpy as np

# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# b = a[1:3, 1:3]
# c = a[1:3, [1, 2]]
# d = a[..., 1:]
# print(a)
# print(b)
# print(c)
# print(d)

arr = np.arange(24).reshape(4, 6)
print(arr)
print(arr[::2])
print(arr[2::])
print(arr[-1:])
print(arr[:-1])
print(arr[::-1])

exit(0)
