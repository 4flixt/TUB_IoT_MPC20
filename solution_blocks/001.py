def numerical_grad(f, x, h):
    df = f(x+h)-f(x-h)
    dx = 2*h
    
    grad = df/dx
    
    return grad
