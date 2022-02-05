




import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
f='Циклоида(z) или астроида(a)'

fig, ax = plt.subplots()
anim_object, = plt.plot([], [], '-', lw=2) # Объект анимации
xdata, ydata = [], [] # Координаты объекта анимации

def graf(f,R):
  if f == 'z':
    t = np.arange (-2*np.pi, 2*np.pi, 0.1)
    x = R*(t-np.sin(t))
    y = R*(1-np.cos(t))
  elif f == 'a':
    t = np.arange (-2*np.pi, 2*np.pi, 0.1)
    R1 = R/4
    x = R1*np.cos(t)**3
    y = R1*np.sin(t)**3
  return x,y
  plt.show()

ax.set_xlim(0, 2*np.pi) # Пределы изменения переменной Х
ax.set_ylim(-1, 1) # Пределы изменения переменной У

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

graf(f='z')


