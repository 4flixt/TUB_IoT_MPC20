
for i in range(N_sim):
    x_next = system(x_0,u_k)
    res_x.append(x_next)
    x_0 = x_next

# Make an array from the list of arrays:
res_x = np.concatenate(res_x,axis=1)
