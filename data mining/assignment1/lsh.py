import time
import numpy as np
import scipy.sparse as sp

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


def lsh(X, y, q, k):
    pass

def test(Q, k=10, func='lsh'):
    # X = Q[0].todense()
    X = Q[0]
    y = Q[1]
    N = X.shape[0]
    if func == 'bf':
        f = bfSearch
    else:
        f = lsh

    preList = []
    for i in range(N):
        index = f(X, y, X[i, :], k)
        pre = np.sum(y[index] == y[i]) / float(k)
        preList.append(pre)
    preList = np.array(preList)
    print 'mean = ', preList.mean(),
    print ' std = ', preList.std()