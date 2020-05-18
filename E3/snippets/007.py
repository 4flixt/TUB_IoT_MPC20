x_terminal = X[N*nx:(N+1)*nx,:]
J += terminal_cost_fcn(x_terminal)
lb_X.append(lb_x)
ub_X.append(ub_x)
