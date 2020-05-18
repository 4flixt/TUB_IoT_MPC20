for k in range(N):
    # 01 - Your code here!
    x_k = X[k*nx:(k+1)*nx,:]
    x_k_next = X[(k+1)*nx:(k+2)*nx,:]
    u_k = U[k*nu:(k+1)*nu,:]
    # 01

    # 02 - Your code here!
    # objective
    J += stage_cost_fcn(x_k,u_k)
    # 02
    
    # 03 - Your code here!
    # equality constraints (system equation)
    x_k_next_calc = system(x_k,u_k)
    # 03

    # 04 - Your code here!
    g.append(x_k_next - x_k_next_calc)
    lb_g.append(np.zeros((nx,1)))
    ub_g.append(np.zeros((nx,1)))
    # 04

    # 05 - Your code here!
    lb_X.append(lb_x)
    ub_X.append(ub_x)
    lb_U.append(lb_u)
    ub_U.append(ub_u)
    # 05

