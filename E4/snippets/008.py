for i in range(N_sim):
    res_oc = S(lbg=0, ubg=0, p=vertcat(x_0, u_k))
    X_k = res_oc['x'].full().reshape(K+1,nx)
    x_next = X_k.T@D
    res_x_oc.append(x_next)
    x_0 = x_next

# Make an array from the list of arrays:
res_x_oc = np.concatenate(res_x_oc,axis=1)
