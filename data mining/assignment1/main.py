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

def genQ(X, y):
    C = 10
    N = 20
    P = X.shape[1]
    Q = np.zeros((C * N, P), dtype=np.float64)
    qY = []
    for i in range(C):
        Q[i * N:(i + 1) * N, :] += X[np.nonzero(y == i)[0][:20], :]
        for j in range(N):
            qY.append(i)
    return sp.csr_matrix(Q), np.array(qY)


tfDataFile = 'data\\tfData'
tfidfDataFile = 'data\\tfidfData'
yDataFile = 'data\\y.npy'

XTf = sparseIO.load_sparse_matrix(tfDataFile + '.npz').tocsr()
XTfidf = sparseIO.load_sparse_matrix(tfidfDataFile + '.npz').tocsr()
y = np.load(yDataFile)


# Q = genQ(XTfidf, y)
Q = XTfidf, y
K = [10,20,30,40,50]

print 'brute force:'
for k in K:
    start = time.time()
    lsh.test(Q, k, 'bf')
    elapsed = (time.time() - start)
    print 'time = ', elapsed


