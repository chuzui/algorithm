import numpy as np
import scipy.sparse as sp

def _addOnes(X):
    N = X.shape[0]
    ones = np.ones((N, 1))
    X = np.concatenate((ones, X), 1)
    return sp.csr_matrix(X)

def _transY(y, classes):
    N = y.shape[0]
    C = len(classes)
    Y = sp.lil_matrix((N, C))
    for i, yi in enumerate(y):
        Y[i, yi] = 1
    return Y.tocsr()

def _norm(X):
    min = X.min(axis=0)
    max = X.max(axis=0)
    range = max - min
    range[range == 0.0] = 1
    X = (X - min) / range
    # X = X - X.mean(axis=0)
    # varX = X.var(axis=0)
    # varX[varX == 0] = 1
    # X = X / np.sqrt(varX)
    return sp.csr_matrix(X)

def SGDLR(XTrain, yTrain, XTest, mu = 0 ):
    classes = np.lib.arraysetops.unique(yTrain)
    XTrain = _norm(XTrain.todense())
    XTrain = _addOnes(XTrain.todense())
    XTest = _addOnes(XTest.todense())
    yTrain = _transY(yTrain, classes)
    C = len(classes)
    N, P = XTrain.shape

    beta = np.zeros((P, C-1), dtype=np.float64)
    grad = np.zeros((P, C-1), dtype=np.float64)
    maxIter = 10

    for i in xrange(maxIter):
        lamda = 0.1 / (i + 2)
    #     t = np.exp(XTrain.dot(beta))
    #     prob = t / np.atleast_2d((t.sum(axis = 1) + 1)).T
    #     grad = XTrain.T.dot(yTrain[:, :C-1] - prob) -  mu * np.abs(beta)
    #     beta += lamda * grad

        for j in xrange(N):
            x = XTrain[j, :]
            t = np.exp(x * beta)
            prob = t / (t.sum() + 1)
            grad = x.T.dot(yTrain[j, :C-1] - prob) -  2 * mu * beta
            beta += lamda * grad

    t = np.exp(XTest.dot(beta))
    testProb = t / np.atleast_2d((t.sum(axis = 1) + 1)).transpose()
    lastClassProb = 1 - testProb.sum(axis=1)
    testProb = np.concatenate((testProb, np.atleast_2d(lastClassProb).transpose()), 1)
    return classes[np.argmax(testProb, axis=1)]





