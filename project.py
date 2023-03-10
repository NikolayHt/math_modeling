import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as plt3d
import imageio
import os

T = float(input('Напишите температуру звезды : '))
M0 = float(input("Напишите во сколько раз масса звезды больше солнечной : "))
R0 = float(input("Напишите во сколько радиус звезды отличается от солнечной : "))

#T = 5300
#M = 0.5 * (2 * 10**30)
#R = 7e10

fig = plt.figure()
ax = plt3d.Axes3D(fig)

fi = np.linspace(0, np.pi, 100)
Q = np.linspace(0, 2 * np.pi, 100)
Msol = 1.9885 * 10 ** 30
Rsol = 6.9551 * 10 ** 8
Msol1 = Msol * 60
Rsol1 = Rsol * 15

M = Msol * M0
N = 145
O = 2
rey = 0
R = R0 * Rsol
R1 = R0 * Rsol
r = R/5

x = R * np.outer(np.sin(Q), np.cos(fi))
y = R * np.outer(np.sin(Q), np.sin(fi))
z = R * np.outer(np.cos(Q), np.ones(np.size(fi)))

color1 = [0.109, 0.674, 0.956, 1]
color2 = [0.67, 0.89, 0.894, 1]
color3 = [0.94, 1, 1, 1]
color4 = [0.826, 0.862, 0.509, 1]
color5 = [0.967, 0.898, 0.02, 1]
color6 = [0.988, 0.486, 0.109, 1]
color7 = [1, 0.345, 0.345, 1]



for i in range(N):

  ax.set_xlim3d([-2 * R1, 2*R1])
  ax.set_xlabel('X')

  ax.set_ylim3d([-2 * R1, 2*R1])
  ax.set_ylabel('Y')

  ax.set_zlim3d([-2 * R1, 2*R1])
  ax.set_zlabel('Z')

  if T >= 30000:
    ax.cla()
    ax.plot_surface(x, y, z, color = color1)

  elif T >= 10000 and T < 30000:
    ax.cla()
    ax.plot_surface(x,y,z, color = color2)

  elif T >= 7500 and T < 10000:
    ax.cla()
    ax.plot_surface(x,y,z, color = color3)

  elif T >= 6000 and T < 7500:
    ax.cla()
    ax.plot_surface(x,y,z, color = color4)

  elif T >= 5200 and T < 6000:
    ax.cla()
    ax.plot_surface(x,y,z, color = color5)

  elif T >= 3700 and T < 5200:
    ax.cla()
    ax.plot_surface(x,y,z, color = color6)

  elif T >= 2700 and T < 3700:
    ax.cla()
    ax.plot_surface(x,y,z, color = color7)
  else:
    print("иди нафиг")

  ax.set_xlim3d([-2 * R1, 2*R1])
  ax.set_xlabel('X')

  ax.set_ylim3d([-2 * R1, 2*R1])
  ax.set_ylabel('Y')

  ax.set_zlim3d([-2 * R1, 2*R1])
  ax.set_zlabel('Z')

  if M > 0.3 * Msol and M < 18 * Msol:

    if i < 10 and i > 0 :
      x = x
      y = y
      z = z
      R = R
      O += 1

    elif i <= 62:
      x = x * 1.01
      y = y * 1.01
      z = z * 1.01
      R = R * 1.01
      O += 1
    elif R > r and i >= 63 and i < 84:
      x = x * 1.009
      y = y * 1.009
      z = z * 1.009
      R = R * 1.009
      O += 1
    elif i >= 85 and i <= 90:
      x = x * 1.007
      y = y * 1.007
      z = z * 1.007
      R = R * 1.007
      O += 1
      color1[3] -= 0.03
      color2[3] -= 0.03
      color3[3] -= 0.03
      color4[3] -= 0.03
      color5[3] -= 0.03
      color6[3] -= 0.03
      color7[3] -= 0.03
    elif R > r and i > 91 and i < 108:
      x = x * 1.003
      y = y * 1.003
      z = z * 1.003
      R = R * 1.003
      O += 1
      color1[3] -= 0.05
      color2[3] -= 0.05
      color3[3] -= 0.05
      color4[3] -= 0.05
      color5[3] -= 0.05
      color6[3] -= 0.05
      color7[3] -= 0.05


    elif i >= 108 and i < 110:
      x = R * np.outer(np.sin(Q), np.cos(fi))
      y = R * np.outer(np.sin(Q), np.sin(fi))
      z = R * np.outer(np.cos(Q), np.ones(np.size(fi)))
      R = r

    elif R==r :
      color1 = [1, 1, 1]
      color2 = [1, 1, 1]
      color3 = [1, 1, 1]
      color4 = [1, 1, 1]
      color5 = [1, 1, 1]
      color6 = [1, 1, 1]
      color7 = [1, 1, 1]

  elif M >= 18 * Msol and M < 60 * Msol:

    if i <= 60:
      x = x * 1.02
      y = y * 1.02
      z = z * 1.02
      R = R * 1.02
      O += 1

    elif R > r and i >= 63 and i < 84:
      x = x * 0.85
      y = y * 0.85
      z = z * 0.85
      R = R * 0.85
      O += 1

    elif i >= 85 and i <= 90:
      x = x * 1.35
      y = y * 1.35
      z = z * 1.35
      R = R * 1.35
      O += 1

    elif R > r and i > 90 and i < 108:
      x = x * 1.25
      y = y * 1.25
      z = z * 1.25
      R = R * 1.25
      O += 1
      color1[3] -= 0.05
      color2[3] -= 0.05
      color3[3] -= 0.05
      color4[3] -= 0.05
      color5[3] -= 0.05
      color6[3] -= 0.05
      color7[3] -= 0.05

    elif i >= 108 and i < 110:
      x = R * np.outer(np.sin(Q), np.cos(fi))
      y = R * np.outer(np.sin(Q), np.sin(fi))
      z = R * np.outer(np.cos(Q), np.ones(np.size(fi)))
      R = r

    elif R==r :
      color1 = [0.235, 0.764, 0.811]
      color2 = [0.235, 0.764, 0.811]
      color3 = [0.235, 0.764, 0.811]
      color4 = [0.235, 0.764, 0.811]
      color5 = [0.235, 0.764, 0.811]
      color6 = [0.235, 0.764, 0.811]
      color7 = [0.235, 0.764, 0.811]

  elif M > 60 * Msol:

    if i <= 60:
      x = x * 1.02
      y = y * 1.02
      z = z * 1.02
      R = R * 1.02
      O += 1

    elif R > r and i >= 63 and i < 84:
      x = x * 0.85
      y = y * 0.85
      z = z * 0.85
      R = R * 0.85
      O += 1

    elif i >= 85 and i <= 90:
      x = x * 1.35
      y = y * 1.35
      z = z * 1.35
      R = R * 1.35
      O += 1

    elif R > r and i > 90 and i < 108:
      x = x * 1.2
      y = y * 1.2
      z = z * 1.2
      R = R * 1.2
      O += 1
      color1[3] -= 0.05
      color2[3] -= 0.05
      color3[3] -= 0.05
      color4[3] -= 0.05
      color5[3] -= 0.05
      color6[3] -= 0.05
      color7[3] -= 0.05

    elif i >= 108 and i < 110:
      x = R * np.outer(np.sin(Q), np.cos(fi))
      y = R * np.outer(np.sin(Q), np.sin(fi))
      z = R * np.outer(np.cos(Q), np.ones(np.size(fi)))
      R = r

    elif R==r :
      color1 = [0,0,0]
      color2 = [0,0,0]
      color3 = [0,0,0]
      color4 = [0,0,0]
      color5 = [0,0,0]
      color6 = [0,0,0]
      color7 = [0,0,0]


  if i < 70 and i > 10:
    if color1[0] < 0.8:
      color1[0] += 0.06
      color1[2] += -0.0637333333333333
      color1[1] += -0.0449333333333333
    else:
      color1 = [0.8290000000000002, 0.13480000000000072, 0.19120000000000026, 1]

    if color2[0] < 0.8:
      color2[0] += 0.01
      color2[1] -= 0.05
      color2[2] -= 0.05
    else:
      color2 = [0.8290000000000002, 0.13480000000000072, 0.19120000000000026, 1]

    if color3[1] > 0.2:
      color3[0] += 0
      color3[1] -= 0.066
      color3[2] -= 0.066
    else:
      color3 = [0.8290000000000002, 0.13480000000000072, 0.19120000000000026, 1]

    if color4[1] > 0.2:
      color4[0] += 0
      color4[1] -= 0.057
      color4[2] -= 0.033
    else:
      color4 = [0.8290000000000002, 0.13480000000000072, 0.19120000000000026, 1]

    if color5[1] > 0.2:
      color5[0] += 0
      color5[1] -= 0.059
      color5[2] += 0
    else:
      color5 = [0.967, 0.15, 0.02, 1]

    if color6[1] > 0.2:
      color6[0] += 0
      color6[1] -= 0.0324
      color6[2] += 0
    else:
      color6 = [0.8290000000000002, 0.13480000000000072, 0.19120000000000026, 1]

    if color7[1] > 0.1:
      color7[0] += 0
      color7[1] -= 0.001
      color7[2] += 0.001
    else:
      color7 = [1, 0.1, 0.1, 1]



  plt.savefig(f'pic_{i}')

  #print(color1, " ")
  #print(color2, " ")
  #print(color3, " ")
  #print(color4, " ")
  #print(color5, " ")
  #print(color6, " ")
  #print(color7, " ")

images = []
filenames = [f'pic_{i}.png' for i in range(N)]
for filename in filenames:
  images.append(imageio.imread(filename))
  os.remove(filename)
imageio.mimsave('movie.gif', images)
