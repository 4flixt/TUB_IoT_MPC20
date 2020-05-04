x = SX.sym('x')
y = x
for k in range(10):
    y = y*np.sin(y)

print(y)
