import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
heart, = plt.plot([], [], '-', color='r', label='heart')

def loveis(time):
    alpha = (0,2*np.pi,0.1)
    x = 16*np.sin(alpha)**3
    y = 13*np.cos(alpha)-5*np.cos(2*alpha)-2*np.cos(3*alpha)-np.cos(4*alpha)
    return x, y


plt.axis('equal')
ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

def animate(i):
    heart.set_data(loveis(time=i))

ani = animation.FuncAnimation(fig,
                              animate,
                              frames=100,
                              interval=30
                              )

plt.show()

