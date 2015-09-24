from numpy import *
from nn.base import NNBase
from nn.math import softmax, make_onehot, sigmoid
from misc import random_weight_matrix


##
# Evaluation code; do not change this
##
from sklearn import metrics
def full_report(y_true, y_pred, tagnames):
    cr = metrics.classification_report(y_true, y_pred,
                                       target_names=tagnames)
    print cr

def eval_performance(y_true, y_pred, tagnames):
    pre, rec, f1, support = metrics.precision_recall_fscore_support(y_true, y_pred)
    print "=== Performance (omitting 'O' class) ==="
    print "Mean precision:  %.02f%%" % (100*sum(pre[1:] * support[1:])/sum(support[1:]))
    print "Mean recall:     %.02f%%" % (100*sum(rec[1:] * support[1:])/sum(support[1:]))
    print "Mean F1:         %.02f%%" % (100*sum(f1[1:] * support[1:])/sum(support[1:]))


def tanh(x):
    return 2 * sigmoid(2 * x) - 1.0

def d_tanh(x):
    return 4 * sigmoid(2.0 * x) * (1.0 - sigmoid(2.0 * x))

##
# Implement this!
##
class WindowMLP(NNBase):
    """Single hidden layer, plus representation learning."""

    def __init__(self, wv, windowsize=3,
                 dims=[None, 100, 5],
                 reg=0.001, alpha=0.01, rseed=10):
        """
        Initialize classifier model.

        Arguments:
        wv : initial word vectors (array |V| x n)
            note that this is the transpose of the n x |V| matrix L
            described in the handout; you'll want to keep it in
            this |V| x n form for efficiency reasons, since numpy
            stores matrix rows continguously.
        windowsize : int, size of context window
        dims : dimensions of [input, hidden, output]
            input dimension can be computed from wv.shape
        reg : regularization strength (lambda)
        alpha : default learning rate
        rseed : random initialization seed
        """

        # Set regularization
        self.lreg = float(reg)
        self.alpha = alpha # default training rate

        dims[0] = windowsize * wv.shape[1] # input dimension
        param_dims = dict(W=(dims[1], dims[0]),
                          b1=(dims[1],),
                          U=(dims[2], dims[1]),
                          b2=(dims[2],),
                          )
        param_dims_sparse = dict(L=wv.shape)

        # initialize parameters: don't change this line
        NNBase.__init__(self, param_dims, param_dims_sparse)

        random.seed(rseed) # be sure to seed this for repeatability!
        #### YOUR CODE HERE ####

        # any other initialization you need
        self.word_vec_size = wv.shape[1]
        self.windowsize = windowsize
        self.sparams.L = wv.copy()
        self.params.W = random_weight_matrix(*self.params.W.shape)
        self.params.U = random_weight_matrix(*self.params.U.shape)

        #### END YOUR CODE ####



    def _acc_grads(self, window, label):
        """
        Accumulate gradients, given a training point
        (window, label) of the format

        window = [x_{i-1} x_{i} x_{i+1}] # three ints
        label = {0,1,2,3,4} # single int, gives class

        Your code should update self.grads and self.sgrads,
        in order for gradient_check and training to work.

        So, for example:
        self.grads.U += (your gradient dJ/dU)
        self.sgrads.L[i] = (gradient dJ/dL[i]) # this adds an update for that index
        """
        #### YOUR CODE HERE ####

        (H, X) = self.params.W.shape # (100, 150)
        (Dy, H) = self.params.U.shape # (5, 100)

        ##
        # Forward propagation
        x = hstack(self.sparams.L[window]) # (150,) --> (X,)
        a = dot(self.params.W, x) + self.params.b1 # (H,)
        h = tanh(a) # (H,)
        y_hat = softmax(dot(self.params.U, h) + self.params.b2) # (Dy,)
        y = make_onehot(label, len(y_hat))
        delta = y_hat - y

        ##
        # Backpropagation

        # dJ/db2
        self.grads.b2 += delta

        # dJ/dU
        self.grads.U += outer(delta, h) + self.lreg * self.params.U

        # dJ/dW, dJ/db1
        # d_tanh(a) is (H,)
        x1 = dot(self.params.U.T, delta.reshape((Dy, 1))).reshape((H,)) * d_tanh(a)
        self.grads.W += outer(x1, x) + self.lreg * self.params.W
        self.grads.b1 += x1

        dL_updates = dot(self.params.W.T, x1.reshape((H, 1)))
        for pt in xrange(self.windowsize):
            f = dL_updates[pt * self.word_vec_size : (pt + 1) * self.word_vec_size]
            self.sgrads.L[window[pt]] = f.reshape((self.word_vec_size,))

        #### END YOUR CODE ####


    def predict_proba(self, windows):
        """
        Predict class probabilities.

        Should return a matrix P of probabilities,
        with each row corresponding to a row of X.

        windows = array (n x windowsize),
            each row is a window of indices
        """
        # handle singleton input by making sure we have
        # a list-of-lists
        if not hasattr(windows[0], "__iter__"):
            windows = [windows]

        #### YOUR CODE HERE ####

        print windows

        N = len(windows)
        windowsize = len(windows[0])
        (Dy, H) = self.params.U.shape

        P = zeros((N, Dy))

        for i, window in enumerate(windows):
            x = hstack(self.sparams.L[window]) # (150,) --> (X,)
            h = tanh(dot(self.params.W, x) + self.params.b1) # (H,)
            y_hat = softmax(dot(self.params.U, h) + self.params.b2) # (Dy,)
            P[i, :] = y_hat

        #### END YOUR CODE ####

        return P # rows are output for each input


    def predict(self, windows):
        """
        Predict most likely class.
        Returns a list of predicted class indices;
        input is same as to predict_proba
        """

        #### YOUR CODE HERE ####

        (N, windowsize) = windows.shape
        (Dy, H) = self.params.U.shape

        c = []

        for i, window in enumerate(windows):
            x = hstack(self.sparams.L[window]) # (150,) --> (X,)
            h = tanh(dot(self.params.W, x) + self.params.b1) # (H,)
            y_hat = softmax(dot(self.params.U, h) + self.params.b2) # (Dy,)
            curr = argmax(y_hat)
            c.append(curr)


        #### END YOUR CODE ####
        return c # list of predicted classes


    def compute_loss(self, windows, labels):
        """
        Compute the loss for a given dataset.
        windows = same as for predict_proba
        labels = list of class labels, for each row of windows
        """

        #### YOUR CODE HERE ####

        labels_lst = None

        # handle singleton input by making sure we have
        # a list-of-lists
        if not hasattr(windows[0], "__iter__"):
            windows = [windows]
            labels_lst = [labels]
        else:
            labels_lst = labels

        J = 0.0

        for window, label in zip(windows, labels_lst):
            x = hstack(self.sparams.L[window]) # (150,) --> (X,)
            h = tanh(dot(self.params.W, x) + self.params.b1) # (H,)
            y_hat = softmax(dot(self.params.U, h) + self.params.b2) # (Dy,)
            J -= log(y_hat[label])

        J += (self.lreg / 2.0) * (sum(self.params.W**2.0) + sum(self.params.U**2.0))

        #### END YOUR CODE ####
        return J

# from numpy import *
# from nn.base import NNBase
# from nn.math import softmax, make_onehot, sigmoid
# from misc import random_weight_matrix
#
#
# ##
# # Evaluation code; do not change this
# ##
# from sklearn import metrics
# def full_report(y_true, y_pred, tagnames):
#     cr = metrics.classification_report(y_true, y_pred,
#                                        target_names=tagnames)
#     print cr
#
# def eval_performance(y_true, y_pred, tagnames):
#     pre, rec, f1, support = metrics.precision_recall_fscore_support(y_true, y_pred)
#     print "=== Performance (omitting 'O' class) ==="
#     print "Mean precision:  %.02f%%" % (100*sum(pre[1:] * support[1:])/sum(support[1:]))
#     print "Mean recall:     %.02f%%" % (100*sum(rec[1:] * support[1:])/sum(support[1:]))
#     print "Mean F1:         %.02f%%" % (100*sum(f1[1:] * support[1:])/sum(support[1:]))
#
# def d_tanh(x):
#     return 4 * sigmoid(2.0 * x) * (1.0 - sigmoid(2.0 * x))
#
#
# ##
# # Implement this!
# ##
# class WindowMLP(NNBase):
#     """Single hidden layer, plus representation learning."""
#
#     def __init__(self, wv, windowsize=3,
#                  dims=[None, 100, 5],
#                  reg=0.001, alpha=0.01, rseed=10):
#         """
#         Initialize classifier model.
#
#         Arguments:
#         wv : initial word vectors (array |V| x n)
#             note that this is the transpose of the n x |V| matrix L
#             described in the handout; you'll want to keep it in
#             this |V| x n form for efficiency reasons, since numpy
#             stores matrix rows continguously.
#         windowsize : int, size of context window
#         dims : dimensions of [input, hidden, output]
#             input dimension can be computed from wv.shape
#         reg : regularization strength (lambda)
#         alpha : default learning rate
#         rseed : random initialization seed
#         """
#
#         # Set regularization
#         self.lreg = float(reg)
#         self.alpha = alpha # default training rate
#
#         dims[0] = windowsize * wv.shape[1] # input dimension
#         param_dims = dict(W=(dims[1], dims[0]),
#                           b1=(dims[1],),
#                           U=(dims[2], dims[1]),
#                           b2=(dims[2],),
#                           )
#         param_dims_sparse = dict(L=wv.shape)
#
#         # initialize parameters: don't change this line
#         NNBase.__init__(self, param_dims, param_dims_sparse)
#
#         random.seed(rseed) # be sure to seed this for repeatability!
#         #### YOUR CODE HERE ####
#
#         # any other initialization you need
#         self.word_vec_size = wv.shape[1]
#         self.windowsize = windowsize
#         self.sparams.L = wv.copy()
#
#         self.params.W = random_weight_matrix(*self.params.W.shape)
#         self.params.U = random_weight_matrix(*self.params.U.shape)
#
#
#
#         #### END YOUR CODE ####
#
#
#
#     def _acc_grads(self, window, label):
#         """
#         Accumulate gradients, given a training point
#         (window, label) of the format
#
#         window = [x_{i-1} x_{i} x_{i+1}] # three ints
#         label = {0,1,2,3,4} # single int, gives class
#
#         Your code should update self.grads and self.sgrads,
#         in order for gradient_check and training to work.
#
#         So, for example:
#         self.grads.U += (your gradient dJ/dU)
#         self.sgrads.L[i] = (gradient dJ/dL[i]) # this adds an update for that index
#         """
#         #### YOUR CODE HERE ####
#
#         ##
#         # Forward propagation
#
#         ##
#         # Backpropagation
#         (H, X) = self.params.W.shape # (100, 150)
#         (Dy, H) = self.params.U.shape # (5, 100)
#
#         ##
#         # Forward propagation
#         x = hstack(self.sparams.L[window]) # (150,) --> (X,)
#         a = dot(self.params.W, x) + self.params.b1 # (H,)
#         h = tanh(a) # (H,)
#         y_hat = softmax(dot(self.params.U, h) + self.params.b2) # (Dy,)
#         y = make_onehot(label, 5)
#         delta = y_hat - y
#
#         ##
#         # Backpropagation
#
#         # dJ/db2
#         self.grads.b2 += delta
#
#         # dJ/dU
#         self.grads.U += outer(delta, h) + self.lreg * self.params.U
#
#         # dJ/dW, dJ/db1
#         # d_tanh(a) is (H,)
#         x1 = dot(self.params.U.T, delta.reshape((Dy, 1))).reshape((H,)) * d_tanh(a)
#         self.grads.W += outer(x1, x) + self.lreg * self.params.W
#         self.grads.b1 += x1
#
#         dL_updates = dot(self.params.W.T, x1.reshape((H, 1)))
#         for pt in xrange(self.windowsize):
#             f = dL_updates[pt * self.word_vec_size : (pt + 1) * self.word_vec_size]
#             self.sgrads.L[window[pt]] = f.reshape((self.word_vec_size,))
#
#
#
#
#         #### END YOUR CODE ####
#
#
#     def predict_proba(self, windows):
#         """
#         Predict class probabilities.
#
#         Should return a matrix P of probabilities,
#         with each row corresponding to a row of X.
#
#         windows = array (n x windowsize),
#             each row is a window of indices
#         """
#         # handle singleton input by making sure we have
#         # a list-of-lists
#         if not hasattr(windows[0], "__iter__"):
#             windows = [windows]
#
#         size = 3
#         d = self.sparams.L.shape[1]
#
#         idx = reshape(windows, -1)
#         x = reshape(self.sparams.L[idx], (size * d, -1))
#         #### YOUR CODE HERE ####
#         h = tanh(self.params.W.dot(x) + self.params.b1[:, newaxis])
#         y_hat = softmax(self.params.U.dot(h) + self.params.b2[:, newaxis])
#
#         P = y_hat.T
#         # print P.shape
#         # print P[1]
#         #### END YOUR CODE ####
#
#         return P # rows are output for each input
#
#
#     def predict(self, windows):
#         """
#         Predict most likely class.
#         Returns a list of predicted class indices;
#         input is same as to predict_proba
#         """
#
#         #### YOUR CODE HERE ####
#         P = self.predict_proba(windows)
#         c = argmax(P, axis=1)
#
#         #### END YOUR CODE ####
#         return c # list of predicted classes
#
#
#     def compute_loss(self, windows, labels):
#         """
#         Compute the loss for a given dataset.
#         windows = same as for predict_proba
#         labels = list of class labels, for each row of windows
#         """
#
#         #### YOUR CODE HERE ####
#         if not hasattr(windows[0], "__iter__"):
#             windows = [windows]
#             labels = [labels]
#
#         N = len(labels)
#
#         P = self.predict_proba(windows)
#
#         J = 0
#
#         J -= log(P[range(N), labels]).sum()
#
#         J += self.lreg / 2 * (power(self.params.W, 2).sum() + power(self.params.U, 2).sum())
#
#         #### END YOUR CODE ####
#         return J
#
# # if __name__ == "__main__":
# #     clf = WindowMLP(wv, windowsize=windowsize, dims=[None, 100, 5],
# #                 reg=0.001, alpha=0.01)
# #     clf.grad_check(X_train[0], y_train[0]) # gradient check on single point