import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
fly, = plt.plot([], [], '-', color='y', label='fly')

def babochka(time):
    alpha = np.arange(0,12*np.pi,0.1) 
    x = np.sin(alpha)*(np.exp(np.cos(alpha))-2*np.cos(4*alpha)+np.sin(alpha/12)**5)
    y = np.cos(alpha)*(np.exp(np.cos(alpha))-2*np.cos(4*alpha)+np.sin(alpha/12)**5)
    return x, y


plt.axis('equal')
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

def animate(i):
    fly.set_data(babochka(time=i))

ani = animation.FuncAnimation(fig,
                              animate,
                              frames=360,
                              interval=30
                              )

plt.show()

