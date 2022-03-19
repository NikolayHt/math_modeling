import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

frames = 100

seconds_in_year = 365 * 24 * 60 * 60
years = 1
t = np.linspace(0, years * seconds_in_year, frames)

def move_func(s, t):
  (x1, u_x1, y1, u_y1,
   x2, u_x2, y2, u_y2,
   x3, u_x3, y3, u_y3,
   x4, u_x4, y4, u_y4,
   x5, u_x5, y5, u_y5) = s
  
  dxdt1 = u_x1
  du_xdt1 = -G * m * x1 / (x1**2 + y1**2)**1.5
  dydt1 = u_y1
  du_ydt1 = -G * m * y1 / (x1**2 + y1**2)**1.5

  dxdt2 = u_x2
  du_xdt2 = -G * m * x2 / (x2**2 + y2**2)**1.5
  dydt2 = u_y2
  du_ydt2 = -G * m * y2 / (x2**2 + y2**2)**1.5

  dxdt3 = u_x3
  du_xdt3 = -G * m * x3 / (x3**2 + y3**2)**1.5
  dydt3 = u_y3
  du_ydt3 = -G * m * y3 / (x3**2 + y3**2)**1.5

  dxdt4 = u_x4
  du_xdt4 = -G * m * x4 / (x4**2 + y4**2)**1.5
  dydt4 = u_y4
  du_ydt4 = -G * m * y4 / (x4**2 + y4**2)**1.5

  dxdt5 = u_x5
  du_xdt5 = -G * m * x5 / (x5**2 + y5**2)**1.5
  dydt5 = u_y5
  du_ydt5 = -G * m * y5 / (x5**2 + y5**2)**1.5

  return (dxdt1, du_xdt1, dydt1, du_ydt1,
          dxdt2, du_xdt2, dydt2, du_ydt2,
          dxdt3, du_xdt3, dydt3, du_ydt3,
          dxdt4, du_xdt4, dydt4, du_ydt4,
          dxdt5, du_xdt5, dydt5, du_ydt5) 

G = 6.67 * 10**(-11)
m = 1.98 * 10**(30)

x10 = 149 * 10 ** 9
u_x10 = 0
y10 = 0
u_y10 = 30000

x20 = 0.387 * 149 * 10**9
u_x20 = 0
y20 = 0
u_y20 = 47360

x30 = 108 * 10**9
u_x30 = 0
y30 = 0
u_y30 = 35000

x40 = 228 * 10**9
u_x40 = 0
y40 = 0
u_y40 = 24077

x50 = 2 *10**11
u_x50 = 0
y50 = 0
u_y50 = 20122

s0 = (x10, u_x10, y10, u_y10,
      x20, u_x20, y20, u_y20,
      x30, u_x30, y30, u_y30,
      x40, u_x40, y40, u_y40,
      x50, u_x50, y50, u_y50)

def solve_func(i, key):
  sol = odeint(move_func, s0, t)
  if key == 'point':
    x1 = sol[i, 0]
    y1 = sol[i, 2]
    x2 = sol[i, 4]
    y2 = sol[i, 6]
    x3 = sol[i, 8]
    y3 = sol[i, 10]
    x4 = sol[i, 12]
    y4 = sol[i, 14]
    x5 = sol[i, 16]
    y5 = sol[i, 18]
  else:
    x1 = sol[:i, 0]
    y1 = sol[:i, 2]
    x2 = sol[:i, 4]
    y2 = sol[:i, 6]
    x3 = sol[:i, 8]
    y3 = sol[:i, 10]
    x4 = sol[:i, 12]
    y4 = sol[:i, 14]
    x5 = sol[:i, 16]
    y5 = sol[:i, 18]
  return ((x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5))

fig, ax = plt.subplots()

ball1, = plt.plot([], [], 'o', color = 'seagreen')
ball_line1, = plt.plot([], [], '-', color = 'seagreen')

ball2, = plt.plot([], [], 'o', color = 'lightgray')
ball_line2, = plt.plot([], [], '-', color = 'lightgray')

ball3, = plt.plot([], [], 'o', color = 'wheat')
ball_line3, = plt.plot([], [], '-', color = 'wheat')

ball4, = plt.plot([], [], 'o', color = 'firebrick')
ball_line4, = plt.plot([], [], '-', color = 'firebrick')

ball5, = plt.plot([], [], 'o', color = 'aqua')
ball_line5, = plt.plot([], [], '-', color = 'aqua')

plt.plot([0], [0], 'o', color = 'y', ms=20)

def animate(i):
  ball1.set_data(solve_func(i, 'point')[0])
  ball_line1.set_data(solve_func(i, 'line')[0])

  ball2.set_data(solve_func(i, 'point')[1])
  ball_line2.set_data(solve_func(i, 'line')[1])

  ball3.set_data(solve_func(i, 'point')[2])
  ball_line3.set_data(solve_func(i, 'line')[2])
  
  ball4.set_data(solve_func(i, 'point')[3])
  ball_line4.set_data(solve_func(i, 'line')[3])
  
  ball5.set_data(solve_func(i, 'point')[4])
  ball_line5.set_data(solve_func(i, 'line')[4])

ani = FuncAnimation(fig,
                    animate, 
                    frames=frames,
                    interval=30)

plt.axis('equal')
edge = 2 * x10
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

plt.show()