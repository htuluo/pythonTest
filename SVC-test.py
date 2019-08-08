import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

loadData = np.loadtxt("./testData.txt", skiprows=0)
dataLength = len(loadData[0])
dataY = loadData[:, dataLength - 1]
dataX = loadData[:, 0:dataLength - 1]

xTrainData, xTestData, yTrainData, yTestData = train_test_split(dataX, dataY, test_size=0.5, random_state=0)

print(len(xTrainData))
# scX = StandardScaler()
# xTrainData = scX.fit_transform(xTrainData)
# xTestData = scX.fit_transform(xTestData)

clf1 = SVC(kernel='poly', random_state=0)
clf1.fit(xTrainData, yTrainData)
yPredict1 = clf1.predict(xTestData)

print(yPredict1)

k = 0
for i in range(len(yTestData)):
    if yPredict1[i] == yTestData[i]:
        k += 1
print(k)

accuracySvm = float(k) / float(len(yTestData))
print(accuracySvm)
