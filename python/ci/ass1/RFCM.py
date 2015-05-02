import numpy as np
from scipy import *
from scipy.spatial.distance import cdist
from scipy import stats
import matplotlib.pyplot as plt
from sklearn.cluster import k_means

def _update_centroid(C, data, m, mu, t, w_low, w_up):
    N, M = data.shape
    BU = [[set(), set()] for i in range(C)]
    for k in range(N):
        if abs(mu[0, k] - mu[1, k]) < t:
            BU[0][1].add(k)
            BU[1][1].add(k)
        else:
            BU[0][0].add(k) if mu[0, k] > mu[1, k] else BU[1][0].add(k)
            BU[0][1].add(k) if mu[0, k] > mu[1, k] else BU[1][1].add(k)
    v = zeros((C, M))
    mum = np.power(mu, m)
    for i in range(C):
        low_set = BU[i][0]
        up_set = BU[i][1]
        if len(up_set - low_set) > 0:
            if len(low_set) != 0:
                low_x = np.array(list(low_set))
                v1 = (data[low_x, :] * (mum[i:i+1, low_x]).T / mum[i, low_x].sum()).sum(axis=0)
                diff_x = np.array(list(up_set - low_set))
                v2 = (data[diff_x, :] * (mum[i:i+1, diff_x]).T / mum[i, diff_x].sum()).sum(axis=0)
                v[i, :] = w_low * v1 + w_up * v2
            else:
                diff_x = np.array(list(up_set - low_set))
                v[i, :] = (data[diff_x, :] * (mum[i:i+1, diff_x]).T / mum[i, diff_x].sum()).sum(axis=0)
        else:
            low_x = np.array(list(low_set))
            v[i, :] = (data[low_x, :] * (mum[i:i+1, low_x]).T / mum[i, low_x].sum()).sum(axis=0)

    return v


def rfcm(data, C=2, w_low=0.2, t=0.2, max_iter=100):
    N, M = data.shape
    w_up = 1 - w_low
    m = 2

    mu = np.random.random((C, N))
    mu = mu / mu.sum(axis=0)
    v = _update_centroid(C, data, m, mu, t, w_low, w_up)
    # v = np.random.random((C, M))

    for i in xrange(max_iter):
        d = cdist(v, data)
        tmp = np.power(d, -2 / (m-1))
        mu = tmp / tmp.sum(axis=0)
        v = _update_centroid(C, data, m, mu, t, w_low, w_up)

        mum = np.power(mu, m)
        loss = sum(np.power(d, 2) * mum)
        print loss


    return v, mu

if __name__ == '__main__':
    mu1 = np.array([1,3])
    mu2 = np.array([3,1])
    sigma = np.array([[0.1, 0.01],[0.01, 0.1]])
    x1 = stats.multivariate_normal.rvs(mean=mu1, cov = sigma, size=100)
    x2 = stats.multivariate_normal.rvs(mean=mu2, cov = sigma, size=100)

    ytrain = r_[ones((100,1)), ones((100,1))*2]
    xtrain = r_[x1, x2]
    v, mu = rfcm(xtrain)
    print v
    print mu

    c, l, i = k_means(xtrain, n_clusters=2, max_iter=1000)
    print c
    print l