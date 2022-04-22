	
from matplotlib import pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d
from matplotlib.animation import FuncAnimation
import numpy as np

# Создание пространства для анимации
fig = plt.figure()
ax = plt3d.Axes3D(fig)
 
# Определение параметров пространственной кривой
N = 100
alpha = np.linspace(0, 30, N)
	
# Параметрическое задание пространственной кривой
x = np.cos(alpha)
y = np.sin(alpha)
z = alpha * 0.1

# Создание анимируемых объектов
ball, = ax.plot(x, y, z, 'o', color='g') # Сферический объект
line, = ax.plot(x, y, z, '-', color='g') # Линия
 
# Функция подстановки координат в анимируемые объекты
def animate(i): 	
    ball.set_data(x[i], y[i])
    ball.set_3d_properties(z[i])
 
    line.set_data(x[:i], y[:i])
    line.set_3d_properties(z[:i])
 
# Украшательсвта и масштабирование
ax.set_xlim3d([-1.0, 1.0])
ax.set_xlabel('X')
 
ax.set_ylim3d([-1.0, 1.0])
ax.set_ylabel('Y')
 
ax.set_zlim3d([-1.0, 30.0])
ax.set_zlabel('Z')
	
# Анимирование
ani = FuncAnimation(fig, animate, N, interval=30)
 
plt.show()