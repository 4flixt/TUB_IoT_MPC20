# Symbolic variables x and u:
x = SX.sym('x', nx)
u = SX.sym('u', nu)

# right hand side of ODE:
xdot = vertcat(
    x[1],
    -k[0]*x[0]-k[1]*x[0]**3+u
)

# Create the CasADi function
system = Function("sys",[x,u],[xdot])
