import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Определение пределов переменновй величины
# В данном случае переменной величиной явялется расстояние
initial_pos = 384400000
Earth_Radius = 6400000
r = np.arange(0, initial_pos - Earth_Radius, 500)

# Создание дифференциальной функции изменяемой величины
def asteroid_vel(v, r):
    dvdr = G * M / (v * (initial_pos + Earth_Radius - r)**2)
    return dvdr

# Определение начальных условий и параметров
v_0 = 1
M = 5.94 * 10**24
G = 6.67 * 10**(-11)
# Решение поставленной задачи
solve_ast_vel = odeint(asteroid_vel, v_0, r)

# Построение решения в виде графика функции
plt.plot(initial_pos-r, solve_ast_vel[:,0], label='Скорость')

plt.xlabel('Расстояние до Земли, м')
plt.ylabel('Скорость астероида, м/с')
plt.title('Кривая армагедонна')
plt.xlim(initial_pos, -Earth_Radius)
plt.plot([Earth_Radius, Earth_Radius], [v_0, 11000], label='Земля')
plt.legend()
plt.grid()

plt.show()