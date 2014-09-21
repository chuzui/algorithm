from __future__ import division
import numpy as np
import scipy as sp
import numpy.linalg as ln

def sigmoid(inX):
    return 1.0 / (1 + sp.exp(-inX))

def logRegres(XTrain, y, **opts):
    CONV_THRESH = 1.e-15
    N, P = XTrain.shape
    maxIter = opts.get('maxIter', 100000)
    beta = sp.zeros((P, 1))
    XT = XTrain.T
    for i in xrange(maxIter):
        betaOld = beta
        ebx = np.exp(np.dot(XTrain, beta))
        p = ebx / (1.+ebx)
        s = np.dot(XT, y-p)
        JBar = np.dot(XT, XTrain * np.multiply(p, 1.-p))
        beta = betaOld + np.dot(ln.inv(JBar), s)
        diff = np.sum(np.fabs(beta - betaOld))
        if diff < CONV_THRESH:
            break
    return beta

def reduced_rank_LDA(XTrain, yTrain, XTest, yTest):
    K = len(sp.unique(yTrain))
    N = XTrain.shape[0]
    p = XTrain.shape[1]

    PiK = sp.zeros((K, 1))
    M = sp.zeros((K, p))
    ScatterMatrix = []
    for ci in range(1, K+1):
        inds = sp.nonzero(yTrain == ci)
        Nci = len(inds[0])
        PiK[ci-1] = Nci / N
        #print XTrain[inds, :]
        M[ci-1, :] = sp.mean(XTrain[inds[0], :], 0)
    print PiK
    print M