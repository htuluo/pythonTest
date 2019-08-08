import numpy as np
from sklearn import svm
import matplotlib.pyplot as plt

x = [[1, 8], [3, 20], [1, 15], [3, 35], [5, 35], [4, 40], [7, 80], [6, 49]]
y = [[1, 1, 1, -1, 1, -1, -1, 1]]
arr=np.concatenate((x,y.T), axis=1)
print(arr)

clf = svm.SVC(kernel='poly');
clf.fit(x, y)

for i in x:
    res = clf.predict(np.array(i).reshape(1, -1))
    if res > 0:
        plt.scatter(i[0], i[1], c='r', marker="*")
    else:
        plt.scatter(i[0], i[1], c='g', marker="*")

rdm_arr = np.random.randint(1, 15, size=(15, 2))
for i in rdm_arr:
    res = clf.predict(np.array(i).reshape(1, -1))
    if res > 0:
        plt.scatter(i[0], i[1], c='y', marker='.')
    else:
        plt.scatter(i[0], i[1], c='b', marker='.')


plt.show()
