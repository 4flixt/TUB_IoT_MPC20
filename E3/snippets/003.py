
x_next = A@x + B@u 

# Create the CasADi function
system = Function("sys",[x,u],[x_next])

print(x_next)
