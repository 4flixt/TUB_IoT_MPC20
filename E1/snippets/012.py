def X_fun(x,order):
    # Write your code here!
    X = np.concatenate([x**n for n in range(order)],axis=1)
    return X

print('2nd order, shape={}'.format(X_fun(x,order=2).shape))
print('3rd order, shape={}'.format(X_fun(x,order=3).shape))
