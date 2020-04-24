x_reg = np.linspace(np.min(x), np.max(x), num=200).reshape(-1,1)
y_hat = []

for order_k in range(1,6):
    X = X_fun(x_reg, order=order_k)
    p = poly_regression(x,y,order=order_k)
    y_hat.append(X@p)
