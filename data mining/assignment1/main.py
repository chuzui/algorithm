import numpy as np
import sparseIO
import naviebayes
from crossValidation import tenFoldCV
import cProfile

tfDataFile = 'data\\tfData'
tfidfDataFile = 'data\\tfidfData'
yDataFile = 'data\\y.npy'

XTf = sparseIO.load_sparse_matrix(tfDataFile + '.npz').tocsc()
XTfidf = sparseIO.load_sparse_matrix(tfidfDataFile + '.npz').tocsc()
y = np.load(yDataFile)


# cProfile.run('tenFoldCV(XTfidf, y, naviebayes.NBCG)')
# tenFoldCV(XTf, y, naviebayes.NBD)
# tenFoldCV(XTfidf, y, naviebayes.NBCG)
tenFoldCV(XTfidf, y)



