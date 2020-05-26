# Initialize empty list of constraints
g = []

# 01 - Your code here!

# States at all collocation points
X = SX.sym('X', nx, K+1)
# Initial state
x_init = SX.sym('x0', nx)
# control input
u = SX.sym('u', nu)

# 01

# 02 - Your code here!
# Append constraint to enforce initial state
g0 = X[:,0]-x_init
g.append(g0)
# 02

# 03 - Your code here!
# Append collocation constraints
for k in range(1,K+1):
    gk = -dt*system(X[:,k], u)
    for j in range(K+1):
        gk += A[j,k]*X[:,j]
        
    g.append(gk)
# 03

# 04 - Your code here!    
# concatenate constraints to a vector
g = vertcat(*g)  
# 04


# 05 - Your code here!
# dictionary for nlpsol object (no objective function required)
nlp = {'x':X.reshape((-1,1)), 'g':g, 'p':vertcat(x_init, u)}

# create nlpsol object (with ipopt)
S = nlpsol('S', 'ipopt', nlp)

# 05
