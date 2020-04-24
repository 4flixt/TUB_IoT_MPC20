# 01 - Identify the shape of x and y and print it in a readable form:
# Your code here!
print('x.shape = {}'.format(x.shape))
print('y.shape = {}'.format(y.shape))
# 02 - Create a plot of x over y. Use plt.plot(). Feel free to add axis label, a title etc.
# Your code here!
plt.plot(x,y, 'x')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
