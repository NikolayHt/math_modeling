import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
fly, = plt.plot([], [], '-', color='y', label='fly')
xdata, ydata = [], []

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

def babochka(time):
    alpha = np.arange(0,12*np.pi,0.1) 
    xdata = np.sin(alpha)*(np.exp(np.cos(alpha))-2*np.cos(4*alpha)+np.sin(alpha/12)**5)
    ydata = np.cos(alpha)*(np.exp(np.cos(alpha))-2*np.cos(4*alpha)+np.sin(alpha/12)**5)
    anim_object.set_data(xdata, ydata)
    return fly,

ani = animation.FuncAnimation(fig,
                              fly,
                              frames=360,
                              interval=30
                              )

plt.show()


