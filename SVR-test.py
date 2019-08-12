import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
import time

loadData = np.loadtxt("./testData.txt", skiprows=0)
dataLength = len(loadData[0])
dataY = loadData[:, dataLength - 1]
dataX = loadData[:, 0:dataLength - 1]

t0 = time.time()

xTrainData, xTestData, yTrainData, yTestData = train_test_split(dataX, dataY, test_size=0.5, random_state=0)
t1 = time.time()
print("cost time:")
print(t1 - t0)

print(len(xTrainData))
scX = StandardScaler()
xTrainData = scX.fit_transform(xTrainData)
xTestData = scX.fit_transform(xTestData)

scY = StandardScaler()
print("yTrainData Before:", yTrainData)
yTrainData = yTrainData.reshape(-1, 1)
yTestData = yTestData.reshape(-1, 1)
print("yTrainData After:", yTrainData.reshape(1, -1))
print("yTrainData After:", yTrainData.reshape(1, -1))
clf1 = SVR(kernel='poly')
clf1.fit(xTrainData, yTrainData)
# score = clf1.score(xTestData,yTestData,)
# print(score)
yPredict1 = clf1.predict(xTestData)

print("预测值：", yPredict1)
print("均方误差：", mean_squared_error(yTestData, yPredict1))
print("绝对均方误差：", mean_absolute_error(scY.inverse_transform(yTestData), scY.inverse_transform(yPredict1)))

k = 0
for i in range(len(yTestData)):
    if (yPredict1[i]) > 0.50:
        k += 1
print(k)

accuracySvm = float(k) / float(len(yTestData))
print(accuracySvm)
exit(0)
