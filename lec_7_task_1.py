import matplotlib.pyplot as plt
import numpy as np

f='Циклоида(z) или астроида(a)'

def graf(f,R):
  if f == 'z':
    t = np.arange (-2*np.pi, 2*np.pi, 0.01)
    x = R*(t-(np.sin(t)**3))
    y = R*(1-(np.cos(t)**3))
  elif f == 'a':
    t = np.arange (-2*np.pi, 2*np.pi, 0.01)
    x = R*np.cos(t)**3
    y = R*np.sin(t)**3
  plt.plot(x, y, ls='--', lw=3)
  plt.axis('equal')
  plt.show()
print(graf(f='a',R=3))


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() # Создание пространства и подпространства

anim_object, = plt.plot([], [], '-', lw=2) # Объект анимации

xdata, ydata = [], [] # Координаты объекта анимации

def gr(f,R):
  t = np.arange (-2*np.pi, 2*np.pi, 0.01)
  ax.set_x(R*np.cos(t)**3) # Пределы изменения переменной Х
  ax.set_y(R*np.sin(t)**3) # Пределы изменения переменной У



def update(frame): # Функция подстановки координат в объект анимации
    xdata.append(frame) # Рассщет координаты Х
    ydata.append(np.sin(frame)) # Рассщет координаты У
    anim_object.set_data(xdata, ydata) # Передача координат
    return anim_object,

ani = FuncAnimation(fig, # Стандартный вызов пространства для анимации
                    update, # Вызов функции подстановки координат
                    frames=np.arange(0, 2*np.pi, 0.1),
                    interval=100 # Интервал между кадрами,
                    )            # по умолчанию 200 милисекунд

#ani.save('lec_7_create_animation_simple.gif')
plt.show()