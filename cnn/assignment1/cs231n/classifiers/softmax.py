import numpy as np
from random import shuffle


def _transY(y, classes):
    N = y.shape[0]
    C = len(classes)
    Y = np.zeros((N, C))
    # for i, yi in enumerate(y):
    # Y[i, yi] = 1
    Y[range(N), y] = 1
    return Y


def softmax_loss_naive(W, X, y, reg):
    """
    Softmax loss function, naive implementation (with loops)
    Inputs:
    - W: C x D array of weights
    - X: D x N array of data. Data are D-dimensional columns
    - y: 1-dimensional array of length N with labels 0...K-1, for K classes
    - reg: (float) regularization strength
    Returns:
    a tuple of:
    - loss as single float
    - gradient with respect to weights W, an array of same size as W
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)
    num_train = X.shape[1]
    num_classes = W.shape[0]
    #############################################################################
    # TODO: Compute the softmax loss and its gradient using explicit loops.     #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    scores = W.dot(X)
    correct_scores = scores[y, range(num_train)]

    loss += np.sum(np.log(np.sum(np.exp(scores), 0)))
    loss -= np.sum(correct_scores)
    loss /= num_train
    loss += 0.5 * reg * np.sum(W * W)

    Y = _transY(y, range(num_classes))
    expMa = np.exp(scores)
    dW += (expMa / np.sum(expMa, 0)).dot(X.T) / num_train
    dW -= X.dot(Y).T / num_train
    dW += reg * W

    #############################################################################
    # END OF YOUR CODE                                 #
    #############################################################################

    return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
    """
    Softmax loss function, vectorized version.

    Inputs and outputs are the same as softmax_loss_naive.
    """
    # Initialize the loss and gradient to zero.
    loss = 0.0
    dW = np.zeros_like(W)

    #############################################################################
    # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
    # Store the loss in loss and the gradient in dW. If you are not careful     #
    # here, it is easy to run into numeric instability. Don't forget the        #
    # regularization!                                                           #
    #############################################################################
    num_train = X.shape[1]
    num_classes = W.shape[0]
    scores = W.dot(X)
    correct_scores = scores[y, range(num_train)]

    loss += np.sum(np.log(np.sum(np.exp(scores), 0)))
    loss -= np.sum(correct_scores)
    loss /= num_train
    loss += 0.5 * reg * np.sum(W * W)

    Y = _transY(y, range(num_classes))
    expMa = np.exp(scores)
    dW += (expMa / np.sum(expMa, 0)).dot(X.T) / num_train
    dW -= X.dot(Y).T / num_train
    dW += reg * W
    #############################################################################
    # END OF YOUR CODE                                 #
    #############################################################################

    return loss, dW
