import numpy.random as nrandom
import numpy as np
from sklearn.linear_model import LogisticRegression

def tenFoldCV(X, y, func=None):
    N = X.shape[0]
    index = range(N)
    nrandom.shuffle(index)
    foldSize = N / 10
    acc = []
    for i in range(10):
        testIndex = index[foldSize * i : foldSize * (i + 1)]
        trainIndex = index[: foldSize * i] + index[foldSize * (i + 1) : ]

        XTrain = X[trainIndex, :]
        yTrain = y[trainIndex]
        XTest = X[testIndex, :]
        yTest = y[testIndex]
        if func is not None:
            yPred = np.ravel(func(XTrain, yTrain, XTest))
            yTest = np.ravel(yTest)
            acc.append(float(np.sum(yTest == yPred)) / len(yTest))
        else:
            cl = LogisticRegression()
            yTrain = np.ravel(yTrain)
            cl.fit(XTrain, yTrain)

            yPred = np.ravel(cl.predict(XTest))
            yTest = np.ravel(yTest)
            acc.append(float(np.sum(yTest == yPred)) / len(yTest))
    acc = np.array(acc)
    print acc
    print acc.mean(), acc.std()