# Initialize variables
l = SX.sym("l",2,1)
u = SX.sym("u",2,1)

# The corners of the rectangle in terms of l and u:
x1 = l
x2 = u
x3 = vertcat(l[0], u[1])
x4 = vertcat(u[0], l[1])
