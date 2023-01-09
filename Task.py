# есть квадратное уравнение, пользователь вводит коэф. а,б,с (a*xкор2 + b*x +c = 0
# если в уравнении один корень, нарисовать прямую из точки 0.0 до х,0
# если в уравнении два кореня, нарисовать прямую из точки x1.0 до х2,3
# решаем уравнение
# отметить корни на координатной плоскости
# добавить исключения когда нет корней

import matplotlib.pyplot as plt
import math

a = float(input("Enter a :"))
b = float(input("Enter b :"))
c = float(input("Enter c :"))

d = b**2 - 4*a*c
print("Discr = ",d)

if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("two roots: ",x1,x2)
    plt.plot([x1*1,0],[x1*2,3])
    plt.plot([x1, 0], [x2, 0], "ro")
    plt.show()
elif d == 0:
    x = -b / (2 * a)
    print("one roots :", x)
    plt.plot([0,x],[0,0])
    plt.show()
else:
    print("no roots")

