import random


def lucky_number(file):
    sum_numbers = 0
    with open(file, 'a', encoding='utf8') as data_file:
        while sum_numbers < 777:
            number = int(input('Введите число: '))
            if random.randint(1, 13) == 13:
                raise RuntimeError
            else:
                sum_numbers += number
                data_file.write('{}\n'.format(number))


try:
    lucky_number('out_file.txt')
except RuntimeError:
    print('Вас постигла неудача!')
else:
    print('Вы успешно выполнили условие для выхода из порочного цикла!')