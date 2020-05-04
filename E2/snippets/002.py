my_fun = Function('my_fun',[x],[y])

h_list = [1e-2, 1e-6,  1e-12, 1e-15, 1e-16]
x0 = 7
for h in h_list:
    dy = (my_fun(x0+h)-my_fun(x0))/h
    print(dy)
