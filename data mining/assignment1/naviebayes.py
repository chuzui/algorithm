import numpy as np
import scipy.sparse as sp
from sklearn.preprocessing import StandardScaler

def _transY(y, classes):
    N = y.shape[0]
    C = len(classes)
    Y = sp.lil_matrix((N, C))
    for i, yi in enumerate(y):
        Y[i, yi] = 1
    return Y


def _discretize(x):
    min = x.min(axis = 0)
    max = x.max(axis = 0)
    ran = max - min
    p1 = min + ran / 3
    p2 = ran + ran * 2 / 3
    x[(x > 0) & (x<=p1)] = 1
    x[(x > p1) & (x <= p2)] = 9
    x[x>p2] = 30
    return x


def NBD(XTrain, y, XTest):
    scaler = StandardScaler(with_mean=False)
    scaler.fit(XTrain)  # Don't cheat - fit only on training data
    X_train = scaler.transform(XTrain)
    X_test = scaler.transform(XTest)  # apply same transformation to test data

    N = XTrain.shape[0]
    P = XTrain.shape[1]
    classes = np.lib.arraysetops.unique(y)
    C = len(classes)
    classCount = np.array([[np.sum(y == c)] for c in classes])
    logClassPrior = np.log(classCount)  - np.log(np.sum(classCount))

    Y = _transY(y, classes)
    featureCount = Y.T * XTrain
    featureCount.data = featureCount.data + 1
    sumlog = np.log(featureCount.sum(axis=1))
    featureCount.data = np.log(featureCount.data)
    logFeatureProb = featureCount - sumlog


    testProb = XTest * logFeatureProb.T + logClassPrior.T
    return classes[np.argmax(testProb, axis=1)]

def NBCG(XTrain, y, XTest):
    N = XTrain.shape[0]
    P = XTrain.shape[1]
    classes = np.lib.arraysetops.unique(y)
    C = len(classes)
    classCount = np.array([np.sum(y == c) for c in classes])
    logClassPrior = np.log(classCount) - np.log(np.sum(classCount))

    mu = np.zeros((C, P))
    sigma = np.zeros((C, P))
    epsilon = 1e-9
    for i, c in enumerate(classes):
        mu[i, :] = XTrain[np.nonzero(y == c)[0], :].mean(axis=0)
        sigma[i, :] = np.var(XTrain[np.nonzero(y == c)[0], :].todense(), axis=0) + epsilon

    testProb = []
    for i in range(C):
        probi = - 0.5 * np.sum(np.log(np.pi * sigma[i, :])) - \
                0.5 * np.sum((np.power(XTest - mu[i, :], 2)) / (sigma[i, :]), 1)
        testProb.append(probi)
    testProb = np.array(testProb)[:, :, 0].T
    testProb += logClassPrior
    return  classes[np.argmax(testProb, axis=1)]

def NBCD(XTrain, y, XTest):
    XTrain = sp.csr_matrix(_discretize(XTrain.todense()))
    return NBD(XTrain, y, XTest)



