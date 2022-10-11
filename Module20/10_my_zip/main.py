def genexpr(_str, _tuple):
    for index in range(len(_str)):
        yield _str[index], _tuple[index]

def tuple_int_to_string(_str):
    return tuple([int(number) for number in (_str[1: len(_str) - 1].split(', '))])


_str = input('Строка: ')
_tuple = tuple_int_to_string((input('Кортеж чисел: ')))


united_tuple = genexpr(_str, _tuple)
print('\nРезультат: ')
print(united_tuple)
[print(element) for element in united_tuple]