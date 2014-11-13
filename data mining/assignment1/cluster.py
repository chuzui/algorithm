import numpy as np
import scipy
import scipy.sparse as sp
import numpy.random as nrandom
from sklearn.metrics.cluster import normalized_mutual_info_score

def _findClosestCentroid(X, centroids):
    N, P = X.shape
    # y = []
    # for i in xrange(N):
    #     y.append(np.argmin(np.sum(np.power(centroids - X[i, :], 2), axis=1)))
    # return np.array(y)
    tX = X.copy()
    tX.data **=2
    lenX = np.sqrt(tX.sum(axis=1))
    tC = centroids.copy()
    tC.data **= 2
    lenC = np.sqrt(tC.sum(axis=1))
    return np.argmax(X * centroids.T / (lenX * lenC.T), axis=1)



def _computerCentroids(X, y, c):
    N, P = X.shape
    centroids = np.ones((c, P), dtype=np.float64)
    for i in xrange(c):
        if np.sum(y == i) > 0:
            centroids[i, :] = X[np.nonzero(y == i)[0], :].mean(axis=0)
    return sp.csr_matrix(centroids)


def kMeans(X, c, y, iters=100):
    N, P = X.shape
    index = np.array(range(N))
    nrandom.shuffle(index)
    centroids = X[index[:c], :]
    oldY = None
    for i in xrange(iters):
        ypred = _findClosestCentroid(X, centroids)
        ypred = np.ravel(ypred)
        centroids = _computerCentroids(X, ypred, c)
        if oldY is not None and (oldY == ypred).all():
            break
        oldY = ypred

    return ypred

def fastCluster(X, y):
    N, P = X.shape
    tX = X.copy()
    tX.data **=2
    lenX = np.sqrt(tX.sum(axis=1))
    d = 1 - (X * X.T).todense() / (lenX * lenX.T)

    ld = np.ravel(d.copy())
    ld.sort()
    cutD = ld[N * N * 4 / 100]

    p = np.zeros((N, 1), dtype=np.int32)
    for i in range(N):
        pi = 0
        for j in range(N):
            if d[i, j] < cutD:
                pi += 1
        p[i, 0] += pi

    delta = np.ones((N, 1)) * 2
    for i in range(N):
        minDistance = 0
        pi = p[i, 0]
        for j in range(N):
            if p[j, 0] > pi and d[i, j] < minDistance:
                minDistance = d[i, j]
        delta[i, 0] = minDistance

    beta = p / p.max() * delta
    indexs = np.argsort(beta,axis=0)
    for k in range(2, 21):
        print k
        cIndexs = indexs[-k:]
        centroids = X[np.ravel(cIndexs), :]
        ypred = _findClosestCentroid(X, centroids)
        ypred = np.ravel(ypred)
        print normalized_mutual_info_score(y, ypred)




