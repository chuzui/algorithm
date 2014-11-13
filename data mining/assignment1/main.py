import StringIO
import numpy as np
import sparseIO
import naviebayes
from crossValidation import tenFoldCV
import logistic
import scipy.sparse as sp
import cProfile
import pstats
import time
import lsh
import cluster
from sklearn.metrics.cluster import normalized_mutual_info_score
from sklearn.cluster import KMeans
import numpy.random as nrandom
from sklearn import tree
tfDataFile = 'data\\tfData'
tfidfDataFile = 'data\\tfidfData'
yDataFile = 'data\\y.npy'

XTf = sparseIO.load_sparse_matrix(tfDataFile + '.npz').tocsr()
XTfidf = sparseIO.load_sparse_matrix(tfidfDataFile + '.npz').tocsr()
y = np.ravel(np.load(yDataFile))


# for k in range(2,21):
#     for i in range(1000):
#         nmi = []
#         ypred = np.ravel(cluster.kMeans(XTfidf, 10, y))
#         nmi.append(normalized_mutual_info_score(y, ypred))
#     print k
#     print max(nmi)


cluster.fastCluster(XTfidf, y)
