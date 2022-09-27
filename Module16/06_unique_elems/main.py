first_list = []
second_list = []
for i_number in range(3):
    number_list = int(input(f'Введите {i_number + 1}-е число для первого списка: '))
    first_list.append(number_list)

for i_number in range(7):
    number_list = int(input(f'Введите {i_number + 1}-е число для второго списка: '))
    second_list.append(number_list)

print('\nПервый список: ', first_list)
print('Второй список: ', second_list)

first_list.extend(second_list)
for number in first_list:
    count_number = first_list.count(number)
    while count_number > 1:
        first_list.remove(number)
        count_number = first_list.count(number)

print('\nНовый первый список с уникальными элементами: ', first_list)