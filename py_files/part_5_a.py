from numpy import matmul, exp, log, asarray, diag, outer


def sigmoid(x):
    return 1 / (1 + exp(-x))


def reg_obj_grad_hes(X, y, w):
    m = len(y)
    c_1 = y
    c_2 = 1-y
    sig = sigmoid(matmul(X.T,w))
    obj = -(1/m)*(matmul(c_1.T,log(sig))+matmul(c_2.T,log(1-sig)))
    grad = (1/m)*matmul(X, sig-c_1)
    hes = (1/m)*matmul(matmul(X, diag(sig*(1-sig))), X.T)
    return obj, grad, hes


