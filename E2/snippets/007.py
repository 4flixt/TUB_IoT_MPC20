# Define the problem
prob = {'x':x, 'f':y}
# Get a configure solver instance
solver = nlpsol('solver','ipopt',prob)
