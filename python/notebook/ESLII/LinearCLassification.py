from __future__ import division
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import numpy.linalg as ln
def loadSAData(path):
    data = {}
    with open(path) as f:
        data['name'] = f.readline().split(',')[1:-1]

        XTrain = []
        y = []
        for l in f:
            ls = l.split(',')
            XTrain.append(map(float, ls[1:-1]))
            y.append([float(ls[-1])])
        data['XTrain'] = np.array(XTrain)
        data['y'] = np.array(y)
        return data


def loadVowelData(path):
    with open(path) as f:
        f.readline()
        data = np.array([map(float, l.split(',')) for l in f])
        y = data[:, 1]
        x = data[:, 2:]
        return x, y

def dup_fig(x, y):
    colors = [None, 'black','blue','brown','purple','orange','cyan','gray','yellow','black','red','green']
    k = len(sp.unique(y))
    for i in range(1, k+1):
        inds = sp.nonzero(y == i)
        plt.plot(x[inds, 0], x[inds, 1], 'o', color=colors[i])
    plt.show()

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

def processData(X, **opts):
    N,M = X.shape
    if opts.get('std', True):
        X = X - np.mean(X, 0)
    if opts.get('scale', True):
        X = X / (X.max(0) - X.min(0))
    if opts.get('addones', True):
        X = sp.c_[sp.ones((N,1)), X]
    return X

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

def SATest():
    data = loadSAData('../data/SAheart.data')
    XTrain = processData(data['XTrain'], std=False, scale=False)
    XTrain = XTrain[:, :][:, [0,1,2,3,5,7,8,9]]
    N, P = XTrain.shape
    y = data['y']
    name = ['intercept']
    name.append(data['name'])
    beta = logRegres(XTrain, y, maxIter=100000)
    m = ln.inv(XTrain.T.dot(XTrain))
    ebx = np.exp(np.dot(XTrain, beta))
    p = ebx / (1.+ebx)
    print p
    sigma = np.sum((y - p) ** 2) / (N - P - 1)
    print sigma
    covarBetaHat  =  m
    print covarBetaHat.shape
    for i in range(covarBetaHat.shape[0]):
        print sp.sqrt(covarBetaHat[i][i])
SATest()

# path = '../data/vowel.train'
# x, y = loadVowelData(path)
# reduced_rank_LDA(x,y, None, None)



