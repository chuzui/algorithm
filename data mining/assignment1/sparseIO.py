import scipy.sparse as ss
import numpy as np

def save_sparse_matrix(filename,x):
    x_coo=x.tocoo()
    row=x_coo.row
    col=x_coo.col
    data=x_coo.data
    shape=x_coo.shape
    np.savez(filename,row=row,col=col,data=data,shape=shape)

def load_sparse_matrix(filename):
    y=np.load(filename)
    z=ss.coo_matrix((y['data'],(y['row'],y['col'])),shape=y['shape'])
    return z