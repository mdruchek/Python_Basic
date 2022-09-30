length = int(input('Введите длину списка: '))

list_number = [1 if x % 2 == 0 else x % 5 for x in range(length)]

print('Результат: ', list_number)