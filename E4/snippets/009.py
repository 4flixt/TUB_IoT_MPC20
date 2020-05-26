# 01 - Your code here!
x_init = SX.sym('x_init', nx)

x0 = opt_x['x', 0, 0]

g.append(x0-x_init)
lb_g.append(np.zeros((nx,1)))
ub_g.append(np.zeros((nx,1)))
# 01

for i in range(N):
    # 02 - Your code here!
    # objective
    J += stage_cost_fcn(opt_x['x',i,0], opt_x['u',i])
    # 02
    
    # 03 - Your code here!
    # equality constraints (system equation)
    for k in range(1,K+1):
        gk = -dt*system(opt_x['x',i,k], opt_x['u',i])
        for j in range(K+1):
            gk += A[j,k]*opt_x['x',i,j]
            
        
        g.append(gk)
        lb_g.append(np.zeros((nx,1)))
        ub_g.append(np.zeros((nx,1)))   
    # 03

    
    # 04 - Your code here!
    x_next = horzcat(*opt_x['x',i])@D
    g.append(x_next - opt_x['x', i+1, 0])
    lb_g.append(np.zeros((nx,1)))
    ub_g.append(np.zeros((nx,1)))
    # 04
    

# 05 - Your code here!
J += terminal_cost_fcn(opt_x['x', N, 0])
# 05

# 06 - Your code here!
g = vertcat(*g)

prob = {'f':J,'x':vertcat(opt_x),'g':g, 'p':x_init}
mpc_solver = nlpsol('solver','ipopt',prob)
# 06
