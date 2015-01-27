import time
import numpy as np
import scipy.sparse as sp
import numpy.random as nrandom

def bfSearch(X, y, q, k):
    # rows = X.shape[0]
    # stackedQ = sp.csr_matrix((np.tile(q.data, rows), np.tile(q.indices, rows),
    #                        np.arange(0, rows*q.nnz + 1, q.nnz)), shape=X.shape)
    # t = X - stackedQ
    # t.data **= 2
    # d = t.sum(axis=1)
    tX = X.copy()
    tX.data **=2
    lenX = np.sqrt(tX.sum(axis=1))
    lenQ = np.sqrt(np.sum(q.data ** 2))
    cos = X * q.T / (lenX * lenQ)

    index = cos.argsort(axis=0)[-(k+1):-1]
    return index

def genSig(X, randPlanes):
    sig = X * randPlanes.T
    sig[sig > 0] = 1
    sig[sig < 0] = 0
    return np.array(sig, dtype=np.bool)

def lshSearch(sig, qIndex, k):
    sigLen = sig.shape[1]
    hammingDistance = sig ^ sig[qIndex, :]
    index = hammingDistance.sum(axis=1).argsort(axis=0)[1:k+1]
    return index

def testBs(Q, k=10):
    # X = Q[0].todense()
    X = Q[0]
    y = Q[1]
    N = X.shape[0]

    preList = []
    for i in range(N):
        index = bfSearch(X, y, X[i, :], k)
        pre = np.sum(y[index] == y[i]) / float(k)
        preList.append(pre)
    preList = np.array(preList)
    print 'mean = ', preList.mean(),
    print ' std = ', preList.std()

def testLsh(Q, k=10):
    X = Q[0]
    y = Q[1]
    N, P= X.shape
    sigLen = 2000

    randPlanes = nrandom.randn(sigLen, P)
    sig = genSig(X, randPlanes)
    preList = []
    for i in range(N):
        index = lshSearch(sig, i, k)
        pre = np.sum(y[index] == y[i]) / float(k)
        preList.append(pre)
    preList = np.array(preList)
    print 'mean = ', preList.mean(),
    print ' std = ', preList.std()




