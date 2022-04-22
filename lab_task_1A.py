import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d

# Создание пространства для анимации
fig = plt.figure()
ax = plt3d.Axes3D(fig)

# Определение параметров кривой

N = 100
fi = np.linspace(0, 4 * np.pi, 100)
Q = np.linspace(0, 2 * np.pi, 100)

# Параметрическое задание пространственной кривой

x = np.outer(fi, np.cos(Q))
y = np.outer(fi, np.sin(Q))
z = np.outer(np.ones(np.size(Q)), fi**2)  

# Построение пространственной кривой
ax.plot_surface(x, y, z)

ax.legend()
 
# Подписи осей

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

	
# Подпись графика
ax.set_title('3D Test')

plt.show()