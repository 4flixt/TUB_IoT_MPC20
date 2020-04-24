for k in range(5):
    plt.plot(x_reg,y_hat[k], label='Order {}'.format(str(k)))
plt.plot(x,y,'x', label='Measured')
plt.legend()
plt.show()
