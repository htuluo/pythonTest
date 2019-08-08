import numpy as np
from sklearn import svm
from sklearn.linear_model import LogisticRegression

loadData = np.loadtxt("./testData.txt", skiprows=0)
dataLength = len(loadData[0])
dataY = loadData[:, dataLength - 1]
dataX = loadData[:, 0:dataLength - 1]

trainLength = int(len(dataY) * 0.7)
xTrainData = dataX[:trainLength]
yTrainData = dataY[:trainLength]
print(len(xTrainData))
xTestData = dataX[trainLength:]
yTestData = dataY[trainLength:]

clf1 = svm.SVC(kernel="poly")
clf1.fit(xTrainData, yTrainData)
clf2 = LogisticRegression()
clf2.fit(xTrainData, yTrainData)

yPredict1 = clf1.predict(xTestData)
yPredict2 = clf2.predict(xTestData)
print(yPredict1)
print(yPredict2)

k, h = 0, 0
for i in range(len(yTestData)):
    if yPredict1[i] == yTestData[i]:
        k += 1
for i in range(len(yTestData)):
    if yPredict2[i] == yTestData[i]:
        h += 1

print(k, h)

accuracySvm = float(k) / float(len(yTestData))
accuracyLS = float(h) / float(len(yTestData))
print(accuracySvm, accuracyLS)
