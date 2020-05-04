res = solver(ubg = 0, x0=np.array([-1,-1, 1, 1]))
l = res['x'][:2]
u = res['x'][2:]
