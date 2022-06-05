# Ввычислить число пи, (использовать Ряд Нилаканта или 
# любой другой вариант расчета числа Пи примеры 
# расчетов можно посмотреть по ссылке
# c заданной точностью d

d = int(input('Задайте точность: '))

def PiNilakanta (Num):
    PiN = 3
    z = 1
    for i in range(2, Num+1, 2):
        PiN = PiN + (4*z/(i*(i+1)*(i+2)))
        z = -z
    return PiN

import math
def PiEuler (Num):
    PiE = 1
    for i in range (2, Num+1):
        PiE = PiE+ 1/pow(i,2)
    PiE =math.sqrt(6*PiE) 
    return (PiE)

print(f'Ряд Нилаканта: {PiNilakanta(d)}')
print(f'Ряд Эйлера: {PiEuler(d)}')