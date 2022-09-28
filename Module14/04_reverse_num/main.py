def contrary_number(number):
    integer = ''
    fractional = ''
    point = False
    for figure in str(number):
        if figure == '.':
            point = True
            continue
        if point:
            fractional = figure + fractional
        else:
            integer = figure + integer
    return float(integer + '.' + fractional)


number_1 = float(input('Введите первое число: '))
number_2 = float(input('Введите второе число: '))
contrary_number_1 = contrary_number(number_1)
contrary_number_2 = contrary_number(number_2)

print('Первое число наоборот: ', contrary_number_1)
print('Второе число наоборот: ', contrary_number_2)
print('Сумма: ', contrary_number_1 + contrary_number_2)