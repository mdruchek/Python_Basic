import random


def f(x, y):
    x += random.randint(0, 10)
    y += random.randint(0, 5)
    return x / y


def f2(x, y):
    x -= random.randint(0, 10)
    y -= random.randint(0, 5)
    return y / x


try:
    file = open('coordinates.txt', 'r', encoding='utf8')
    file_2 = open('result.txt', 'a', encoding='utf8')
    for line in file:
        nums_list = line.split()
        try:
            res1 = str(f(int(nums_list[0]), int(nums_list[1])))
            res2 = str(f2(int(nums_list[0]), int(nums_list[1])))
        except ZeroDivisionError:
            file_2.write('Деление на ноль в одной из функций.\n')
        else:
            number = str(random.randint(0, 100))
            my_list = sorted([res1, res2, number])
            file_2.write(' '.join(my_list) + '\n')

except TypeError('Операция применена к объекту несоответствующего типа.'):
    print()
except ValueError('Функция получает аргумент правильного типа, но некорректного значения.'):
    print()
finally:
    file.close()
    file_2.close()