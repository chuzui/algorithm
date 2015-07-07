import numpy as np

from cs231n.layers import *
from cs231n.fast_layers import *
from cs231n.layer_utils import *
from cs231n.gradient_check import eval_numerical_gradient

def two_layer_convnet(X, model, y=None, reg=0.0):
    """
    Compute the loss and gradient for a simple two-layer ConvNet. The architecture
    is conv-relu-pool-affine-softmax, where the conv layer uses stride-1 "same"
    convolutions to preserve the input size; the pool layer uses non-overlapping
    2x2 pooling regions. We use L2 regularization on both the convolutional layer
    weights and the affine layer weights.

    Inputs:
    - X: Input data, of shape (N, C, H, W)
    - model: Dictionary mapping parameter names to parameters. A two-layer Convnet
      expects the model to have the following parameters:
      - W1, b1: Weights and biases for the convolutional layer
      - W2, b2: Weights and biases for the affine layer
    - y: Vector of labels of shape (N,). y[i] gives the label for the point X[i].
    - reg: Regularization strength.

    Returns:
    If y is None, then returns:
    - scores: Matrix of scores, where scores[i, c] is the classification score for
      the ith input and class c.

    If y is not None, then returns a tuple of:
    - loss: Scalar value giving the loss.
    - grads: Dictionary with the same keys as model, mapping parameter names to
      their gradients.
    """

    # Unpack weights
    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
    N, C, H, W = X.shape

    # We assume that the convolution is "same", so that the data has the same
    # height and width after performing the convolution. We can then use the
    # size of the filter to figure out the padding.
    conv_filter_height, conv_filter_width = W1.shape[2:]
    assert conv_filter_height == conv_filter_width, 'Conv filter must be square'
    assert conv_filter_height % 2 == 1, 'Conv filter height must be odd'
    assert conv_filter_width % 2 == 1, 'Conv filter width must be odd'
    conv_param = {'stride': 1, 'pad': (conv_filter_height - 1) / 2}
    pool_param = {'pool_height': 2, 'pool_width': 2, 'stride': 2}

    # Compute the forward pass
    a1, cache1 = conv_relu_pool_forward(X, W1, b1, conv_param, pool_param)
    scores, cache2 = affine_forward(a1, W2, b2)

    if y is None:
        return scores

    # Compute the backward pass
    data_loss, dscores = softmax_loss(scores, y)

    # Compute the gradients using a backward pass
    da1, dW2, db2 = affine_backward(dscores, cache2)
    dX, dW1, db1 = conv_relu_pool_backward(da1, cache1)

    # Add regularization
    dW1 += reg * W1
    dW2 += reg * W2
    reg_loss = 0.5 * reg * sum(np.sum(W * W) for W in [W1, W2])

    loss = data_loss + reg_loss
    grads = {'W1': dW1, 'b1': db1, 'W2': dW2, 'b2': db2}

    return loss, grads


def init_two_layer_convnet(weight_scale=1e-3, bias_scale=0, input_shape=(3, 32, 32),
                           num_classes=10, num_filters=32, filter_size=5):
    """
    Initialize the weights for a two-layer ConvNet.

    Inputs:
    - weight_scale: Scale at which weights are initialized. Default 1e-3.
    - bias_scale: Scale at which biases are initialized. Default is 0.
    - input_shape: Tuple giving the input shape to the network; default is
      (3, 32, 32) for CIFAR-10.
    - num_classes: The number of classes for this network. Default is 10
      (for CIFAR-10)
    - num_filters: The number of filters to use in the convolutional layer.
    - filter_size: The width and height for convolutional filters. We assume that
      all convolutions are "same", so we pick padding to ensure that data has the
      same height and width after convolution. This means that the filter size
      must be odd.

    Returns:
    A dictionary mapping parameter names to numpy arrays containing:
      - W1, b1: Weights and biases for the convolutional layer
      - W2, b2: Weights and biases for the fully-connected layer.
    """
    C, H, W = input_shape
    assert filter_size % 2 == 1, 'Filter size must be odd; got %d' % filter_size

    model = {}
    model['W1'] = weight_scale * np.random.randn(num_filters, C, filter_size, filter_size)
    model['b1'] = bias_scale * np.random.randn(num_filters)
    model['W2'] = weight_scale * np.random.randn(num_filters * H * W / 4, num_classes)
    model['b2'] = bias_scale * np.random.randn(num_classes)
    return model


def deep_convnet(X, model, y=None, reg=0.0):
    W1, b1, W2, b2, W3, b3 = model['W1'], model['b1'], model['W2'], model['b2'], model['W3'], model['b3']
    W4, b4, W5, b5= model['W4'], model['b4'], model['W5'], model['b5']
    N, C, H, W = X.shape

    # We assume that the convolution is "same", so that the data has the same
    # height and width after performing the convolution. We can then use the
    # size of the filter to figure out the padding.
    conv_filter_height, conv_filter_width = W1.shape[2:]
    assert conv_filter_height == conv_filter_width, 'Conv filter must be square'
    assert conv_filter_height % 2 == 1, 'Conv filter height must be odd'
    assert conv_filter_width % 2 == 1, 'Conv filter width must be odd'
    conv_param = {'stride': 1, 'pad': (conv_filter_height - 1) / 2}
    pool_param = {'pool_height': 2, 'pool_width': 2, 'stride': 2}

    # Compute the forward pass
    a1, cache1 = conv_relu_pool_forward(X, W1, b1, conv_param, pool_param)
    a2, cache2 = conv_relu_pool_forward(a1, W2, b2, conv_param, pool_param)
    a3, cache3 = conv_relu_pool_forward(a2, W3, b3, conv_param, pool_param)
    a4, cache4 = affine_forward(a3, W4, b4)
    scores, cache5 = affine_forward(a4, W5, b5)

    if y is None:
        return scores

    # Compute the backward pass
    data_loss, dscores = softmax_loss(scores, y)

    # Compute the gradients using a backward pass
    da4, dW5, db5 = affine_backward(dscores, cache5)
    da3, dW4, db4 = affine_backward(da4, cache4)
    da2, dW3, db3 = conv_relu_pool_backward(da3, cache3)
    da1, dW2, db2 = conv_relu_pool_backward(da2, cache2)
    dX, dW1, db1 = conv_relu_pool_backward(da1, cache1)
    #print db3
    # Add regularization
    dW1 += reg * W1
    dW2 += reg * W2
    dW3 += reg * W3
    dW4 += reg * W4
    dW5 += reg * W5
    reg_loss = 0.5 * reg * sum(np.sum(W * W) for W in [W1, W2, W3, W4, W5])

    loss = data_loss + reg_loss
    grads = {'W1': dW1, 'b1': db1, 'W2': dW2, 'b2': db2, 'W3': dW3, 'b3': db3, 'W4': dW4, 'b4': db4, 'W5': dW5, 'b5': db5}

    return loss, grads


def init_deep_convnet(weight_scale=1e-3, bias_scale=0, input_shape=(3, 32, 32),
                      num_classes=10, num_filters=32, filter_size=3):
    C, H, W = input_shape
    assert filter_size % 2 == 1, 'Filter size must be odd; got %d' % filter_size

    N = 3
    M = 2

    model = {}
    w_init = lambda n: np.sqrt(2.0 / n)

    weight1 = w_init(C * filter_size * filter_size)
    model['W1'] = weight1 * np.random.randn(num_filters, C, filter_size, filter_size)
    model['b1'] = bias_scale * np.random.randn(num_filters)

    weight2 = w_init(num_filters * filter_size * filter_size)
    model['W2'] = weight2 * np.random.randn(num_filters, num_filters, filter_size, filter_size)
    model['b2'] = bias_scale * np.random.randn(num_filters)
    model['W3'] = weight2 * np.random.randn(num_filters, num_filters, filter_size, filter_size)
    model['b3'] = bias_scale * np.random.randn(num_filters)

    weight3 = w_init(num_filters *  H * W / 64)
    model['W4'] = weight_scale * np.random.randn(num_filters  * H * W / 64, 1024)
    model['b4'] = bias_scale * np.random.randn(1024)

    weight4 = w_init(1024)
    model['W5'] = weight4 * np.random.randn(1024, num_classes)
    model['b5'] = bias_scale * np.random.randn(num_classes)

    return model

def rel_error(x, y):
  """ returns relative error """
  return np.max(np.abs(x - y) / (np.maximum(1e-8, np.abs(x) + np.abs(y))))

if __name__ == '__main__':
    num_inputs = 4
    input_shape = (3, 32, 32)
    reg = 0.0
    num_classes = 10
    X = np.random.randn(num_inputs, *input_shape)
    y = np.random.randint(num_classes, size=num_inputs)

    model = init_deep_convnet( num_filters=3, filter_size=3, input_shape=input_shape)
    loss, grads = deep_convnet(X, model, y)
    for param_name in sorted(grads):
        f = lambda _: deep_convnet(X, model, y)[0]
        param_grad_num = eval_numerical_gradient(f, model[param_name], verbose=False, h=1e-6)
        e = rel_error(param_grad_num, grads[param_name])
        print '%s max relative error: %e' % (param_name, rel_error(param_grad_num, grads[param_name]))
    # num_inputs = 2
    # input_shape = (3, 16, 16)
    # reg = 0.0
    # num_classes = 10
    # X = np.random.randn(num_inputs, *input_shape)
    # y = np.random.randint(num_classes, size=num_inputs)
    #
    # model = init_two_layer_convnet(num_filters=3, filter_size=3, input_shape=input_shape)
    # loss, grads = two_layer_convnet(X, model, y)
    # for param_name in sorted(grads):
    #     f = lambda _: two_layer_convnet(X, model, y)[0]
    #     param_grad_num = eval_numerical_gradient(f, model[param_name], verbose=False, h=1e-6)
    #     e = rel_error(param_grad_num, grads[param_name])
    #     print '%s max relative error: %e' % (param_name, rel_error(param_grad_num, grads[param_name]))
