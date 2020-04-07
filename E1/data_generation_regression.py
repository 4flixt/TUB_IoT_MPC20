import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
np.random.seed(1234)

# Random coefficients are chosen to have a more or less interesting polynomial behavior:
x = 13*np.random.rand(50)-3
y = 3.2-0.75*x-1.34*x**2+0.3*x**3-0.018*x**4
y *= (1+0.2*np.random.rand(y.shape[0]))
num_outlier = 5
outlier_ind = np.random.choice(np.arange(y.shape[0]),num_outlier, replace=False)
y[outlier_ind] = 5*np.random.rand(num_outlier)
plt.ion()
plt.plot(x,y,'x')

sio.savemat('1d_data', mdict={'x':x.reshape(-1,1), 'y':y.reshape(-1,1)})


