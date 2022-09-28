import math

quantity_number = int(input('Кол-во чисел: '))

if quantity_number != 1:
    initial_list = []

    added_list = []
    mirror_found = False
    number_added = int

    for _ in range(quantity_number):
        initial_list.append(int(input('Число: ')))
    print('\nПоследовательность: ', initial_list)
    initial_list_size = len(initial_list)

    first_two = math.ceil(initial_list_size / 2)

    if initial_list_size % 2 != 0:
        centre = initial_list_size // 2
        first_list = []
        second_list = []
        for i_number in range(centre + 1, initial_list_size):
            first_list.append(initial_list[i_number])
        for i_number in range(-centre - 2, -initial_list_size - 1, -1):
            second_list.append(initial_list[i_number])
        if first_list == second_list:
            number_added = 0

    if number_added != 0:
        for _ in range(first_two):
            if first_two < initial_list_size:
                first_list = []
                second_list = []
                if initial_list[first_two - 1] == initial_list[first_two]:
                    found_couple = True
                    for i_number in range(first_two, initial_list_size):
                        first_list.append(initial_list[i_number])
                    first_list_size = len(first_list)
                    for i_number in range(-first_list_size - 1, -first_list_size * 2 - 1, -1):
                        second_list.append(initial_list[i_number])
                    if first_list == second_list:
                        mirror_found = True
                        break
                first_two += 1
            else:
                break

        if mirror_found:
            number_added = initial_list_size - first_list_size * 2
            for i_number in range(-first_list_size * 2 - 1, -initial_list_size - 1, -1):
                added_list.append(initial_list[i_number])
        else:
            number_added = initial_list_size - 1
            for i_number in range(-2, -initial_list_size - 1, -1):
                added_list.append(initial_list[i_number])

    if number_added != 0:
        print('Нужно приписать чисел: ', number_added)
        print('Сами числа: ', added_list)
    else:
        print('Последовательность симметричная')

else:
    print('\nКол-во должно быть болеше 1')