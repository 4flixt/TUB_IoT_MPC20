for i in range(N_sim):
    # 01 - Your code here!
    # solve optimization problem
    mpc_res = mpc_solver(p=x_0, lbg=0, ubg=0, lbx = lb_opt_x, ubx = ub_opt_x)
    
    # optionally: Warmstart the optimizer by passing the previous solution as an initial guess!
    if i>0:
        mpc_res = mpc_solver(p=x_0, x0=opt_x_k, lbg=0, ubg=0, lbx = lb_opt_x, ubx = ub_opt_x)
        
    # 01
        
        
    # 02 - Your code here!
    # Extract the control input
    opt_x_k = opt_x(mpc_res['x'])
    u_k = opt_x_k['u',0]
    # 02

    # 03 - Your code here!
    # simulate the system
    res_integrator = ode_solver(x0=x_0, p=u_k)
    x_next = res_integrator['xf']
    # 03
    
    # 04 - Your code here!
    # Update the initial state
    x_0 = x_next
    # 04
    
    # 05 - Your code here!    
    # Store the results
    res_x_mpc.append(x_next)
    res_u_mpc.append(u_k)
    # 05
    
# Make an array from the list of arrays:
res_x_mpc = np.concatenate(res_x_mpc,axis=1)
res_u_mpc = np.concatenate(res_u_mpc, axis=1)
