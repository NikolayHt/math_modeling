import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d

# Создание пространства для анимации
fig = plt.figure()
ax = plt3d.Axes3D(fig)

# Определение параметров кривой
t = np.arange(0.01, 30*np.pi, 0.01)
R = 1

# Параметрическое задание пространственной кривой
#x = R * np.cos(t)
#y = R * t**0.5
#z = np.log10(t)

x = R * np.cos(t)
y = R * np.sin(t)
z = R * t

# Построение пространственной кривой
ax.plot(x, y, z, label='Dich')

ax.legend()
 
# Подписи осей

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

	
# Подпись графика
ax.set_title('3D Test')

plt.show()