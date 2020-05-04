# Define the problem
prob = {'x':vertcat(l,u), 'f':f, 'g':g}
solver = nlpsol('solver','ipopt', prob)
