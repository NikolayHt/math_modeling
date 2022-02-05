import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()
circle, = plt.plot([], [], '-', color='g', label='circle')

def circle_move (bet, angle_vel, time):
    alpha = angle_vel * (np.pi/360) * time #angle_vel = амега
    R = alpha * time
    x = R*np.cos(bet)
    y = R*np.sin(bet)
    return x, y

edge = 40
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    circle.set_data(circle_move(bet=np.linspace(0, 2*np.pi, 100), angle_vel=1, time=i))

ani = animation.FuncAnimation(fig,
                              animate,
                              frames=360,
                              interval=30
                              )

#ani.save('lec_7_standart_animation.gif')
plt.show()



