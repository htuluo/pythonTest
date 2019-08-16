import numpy as np
from sklearn import preprocessing

standard_scaler = preprocessing.StandardScaler()
array0 = np.array([[0, 1], [0.5, -1]])
scaler_fit = standard_scaler.fit(array0)
print("Stand fit", scaler_fit)
array0 = standard_scaler.transform(array0)
print("Stand transform:", array0)
min_max_scaler = preprocessing.MinMaxScaler()

# normalize标准化
# array = np.array([[1.1, 2.2, 5.5]])
# normalize = preprocessing.normalize(array)
# print(normalize)
# randint = np.zeros((1,3))
# print("pre",np.linalg.norm(array))
# for col in range(3):
#     randint[0][col] = array[0][col] / np.linalg.norm(array[0])
# print(randint)


# one_hot demo
one_hot_encoder = preprocessing.OneHotEncoder(categories="auto")
one_hot_encoder.fit([[0, 1], [1, 2], [1, 3], [0, 1]])
transform__toarray = one_hot_encoder.transform([[0, 1]]).toarray()
print("One hot Transform:", transform__toarray)


def get_one_hot(val):
    hot_encoder = preprocessing.OneHotEncoder(categories='auto', sparse=False, handle_unknown='ignore')
    hot_encoder.fit(np.array([[100, 200, 300]]).reshape(-1, 1))
    return hot_encoder.transform([[val]])


hot = get_one_hot(400)
print("get:", hot)

# labelEncoder
# label_encoder = preprocessing.LabelEncoder()
# fit = label_encoder.fit([1, 222, 44, 228, 878])
# fit_transform = fit.transform([1, 222])
# print("FIT:",fit_transform)


# a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# b = a[1:3, 1:3]
# c = a[1:3, [1, 2]]
# d = a[..., 1:]
# print(a)
# print(b)
# print(c)
# print(d)

# arr = np.arange(24).reshape(4, 6)
# print(arr)
# print(np.array([1,2,3,4]).reshape(1,-1))
# print(np.array([1,2,3,4]).reshape(-1,1))
# print(arr[::2])
# print(arr[2::])
# print(arr[-1:])
# print(arr[:-1])
# print(arr[::-1])

exit(0)
