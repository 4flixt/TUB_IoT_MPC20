x = SX.sym('x')
y = x**2 - 5*x + 9

y_fun = Function('y', [x], [y])
