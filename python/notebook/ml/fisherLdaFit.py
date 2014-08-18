__author__ = 'Administrator'
from scipy import *
import numpy as np
from scipy import linalg
from scipy import stats
import matplotlib.pyplot as plt

if __name__ == '__main__':
    mu1 = np.array([1,3])
    mu2 = np.array([3,1])
    sigma = np.array([[4, 0.01],[0.01, 0.1]])
    x1 = stats.multivariate_normal.rvs(mean=mu1, cov = sigma, size=100)
    x2 = stats.multivariate_normal.rvs(mean=mu2, cov = sigma, size=100)
    plt.plot(x1[:,0], x1[:,1], 'o', color='r')
    plt.plot(x2[:,0], x2[:,1], 'x', color='b')
    plt.show()
    ytrain = r_[ones((100,1)), ones((100,1))*2]
    xtrain = r_[x1, x2]

    w,z = fisherLdaFit(xtrain, ytrain)
    print w

    fw1 = dot(x1, w)
    fw2 = dot(x2, w)
    plt.figure()
    hist, bins = np.histogram(fw1)
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center')

    hist, bins = np.histogram(fw2)
    center = (bins[:-1] + bins[1:]) / 2
    plt.bar(center, hist, align='center', color = 'r')
    plt.show()