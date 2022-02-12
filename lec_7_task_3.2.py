import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
heart, = plt.plot([], [], '-', color='r', label='heart')
xdata, ydata = [], [] 
ax.set_xlim(-20,20)
ax.set_ylim(-20,20)

def update(time):
    t = 0.1*time
    x = 16*np.sin(t)**3 
    y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
    
    xdata.append(x)
    ydata.append(y)
    heart.set_data(xdata,ydata)
    return heart,

ani = FuncAnimation(fig, 
                    update, 
                    frames=100,
                    interval=30 
                    )            


plt.show()
