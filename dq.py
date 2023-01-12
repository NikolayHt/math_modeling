#Модуль Нейрон
import numpy as np

#Создание класса "Нейрон
class Neuron:
    def __init__(self, w):
        self.w = w

    def y(self, x): #Сумматор
        s = np.dot(self.w, x)   #суммируем входы(Точечное произведение двух массивов)
        return s

    xi = np.array([2, 3])
    wi = np.array([1, 1])
    n = Neuron (wi)
    print('S1 = ', n.y(xi))
    xi = np.array([5, 6])
    print('S2 = ', n.y(xi))