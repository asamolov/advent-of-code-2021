import matplotlib.pyplot as plt
import numpy as np

#a = np.random.random((16, 16))
a = np.zeros((16, 16))

for x in range(8):
    a[x, 2*x] += x
    a[2*x, x] += 2*x

plt.imshow(a,cmap='cool', interpolation='nearest')
plt.colorbar()
plt.show()