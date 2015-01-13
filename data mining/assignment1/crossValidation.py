import numpy.random as nrandom
import numpy as np
from sklearn.linear_model import LogisticRegression


def tenFoldCV(X, y, func=None, lossFunc='01'):
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
            if lossFunc == '01':
                yPred = np.ravel(func(XTrain, yTrain, XTest))
                yTest = np.ravel(yTest)
                acc.append(float(np.sum(yTest == yPred)) / len(yTest))
                print acc[i]
            elif lossFunc == 'mse':
                yPred = np.ravel(func(XTrain, yTrain, XTest))
                yTest = np.ravel(yTest)
                loss = np.sqrt(np.mean((yPred - yTest) ** 2))
                acc.append(loss)
                print loss
        else:
            cl = LogisticRegression()
            yTrain = np.ravel(yTrain)
            cl.fit(XTrain, yTrain)

            yPred = np.ravel(cl.predict(XTest))
            yTest = np.ravel(yTest)
            acc.append(float(np.sum(yTest == yPred)) / len(yTest))
            print acc
    acc = np.array(acc)
    print acc
    print acc.mean(), acc.std()