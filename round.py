import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d

# Создание пространства для анимации
fig = plt.figure()
ax = plt3d.Axes3D(fig)

# Определение параметров кривой

N = 100
fi = np.linspace(0, np.pi, 100)
Q = np.linspace(0, 2 * np.pi, 100)
R = 1
# Параметрическое задание пространственной кривой

x = R * np.outer(np.sin(Q), np.cos(fi))
y = R * np.outer(np.sin(Q), np.sin(fi))
z = R * np.outer(np.cos(Q), np.ones(np.size(fi)))

# Построение пространственной кривой
ax.plot_surface(x, y, z)

# Подписи осей

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

	
# Подпись графика
ax.set_title('3D Test')

plt.show()