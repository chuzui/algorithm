import StringIO
import numpy as np
import sparseIO
import naviebayes
from crossValidation import tenFoldCV
import logistic
import scipy.sparse as sp
import cProfile
import pstats
def norm(X):
    X.data = X.data ** 2
    t = np.sqrt(X.sum(axis=0))
    t[t==0] = 1
    X = X / t
    return sp.csr_matrix(X)


tfDataFile = 'data\\tfData'
tfidfDataFile = 'data\\tfidfData'
yDataFile = 'data\\y.npy'

XTf = sparseIO.load_sparse_matrix(tfDataFile + '.npz').tocsr()
XTfidf = sparseIO.load_sparse_matrix(tfidfDataFile + '.npz').tocsr()
y = np.load(yDataFile)


# pr = cProfile.Profile()
# pr.enable()
tenFoldCV(XTfidf, y, logistic.SGDLR)
# pr.disable()
# sortby = 'cumtime'
# ps = pstats.Stats(pr).sort_stats(sortby)
# ps.print_stats()

