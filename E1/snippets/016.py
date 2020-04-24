# Get the parmeter vector p from the poly_regresssion function and compute yhat
# Alternatively, use your results from the previous task.
# Write your code here.
p = poly_regression(x,y, order = 4 )
X = X_fun(x, order = 4)
yhat =X@p

# Plot yhat over y
# Write your code here.
plt.plot(y,yhat,'x', label='evaluation points')

# Plot y over y (parity line)
# Write your code here.
plt.plot(y,y, label='parity')


# Plot y+20% over y  and y-20% over y
# Write your code here
plt.plot(y,y*(1+0.2), label='+20%')
plt.plot(y,y*(1-0.2), label='-20%')

# Optionally, make things pretty :)
plt.grid()
plt.ylabel('estimated values')
plt.xlabel('measured values')
plt.legend()
