for i in range(N_sim):
    res_integrator = ode_solver(x0=x_0, p=u_k)
    x_next = res_integrator['xf']
    res_x_sundials.append(x_next)
    x_0 = x_next

# Make an array from the list of arrays:
res_x_sundials = np.concatenate(res_x_sundials,axis=1)
