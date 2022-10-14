def _range(num):
    if num == 1:
        return print(num)
    _range(num - 1)
    return print(num)

number = int(input('Введите num: '))
_range(number)