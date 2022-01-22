import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 1000)
y = []
for i in range(1000):
    y1 = x[i] // 1
    y.append(y1)
plt.plot(x, y)
plt.show()