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
import tree
import genData
import ensemble
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif

tfDataFile = 'data\\tfData'
tfidfDataFile = 'data\\tfidfData'
yDataFile = 'data\\y.npy'

print 'lily DT'
XTf = sparseIO.load_sparse_matrix(tfDataFile + '.npz').tocsr()
XTfidf = sparseIO.load_sparse_matrix(tfidfDataFile + '.npz').tocsr()
y = np.ravel(np.load(yDataFile))
#X_new = SelectKBest(f_classif, k=2000).fit_transform(XTfidf.todense(), y)

tenFoldCV(XTfidf.todense(), y, ensemble.adaboost)




