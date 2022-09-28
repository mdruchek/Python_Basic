import math

def point_in_circle(x, y):
    r = math.sqrt(x ** 2 + y ** 2)
    if r <= 1:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет: ')


print('Введите координаты монетки: ')
x = float(input('X: '))
y = float(input('У: '))
point_in_circle(x, y)
