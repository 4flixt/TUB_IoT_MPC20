def poly_regression(x,y, order):
    # Write your code here.
    X = X_fun(x,order=order)
    p = y.T@X@np.linalg.inv(X.T@X)
    return p.T
