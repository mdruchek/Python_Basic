str_1 = list(input('Первая строка: '))
str_2 = list(input('Вторая строка: '))

turned_out = False
for shift_number in range(len(str_2) - 1):
    str_2.insert(0, str_2[len(str_2) - 1])
    str_2.pop()
    if str_1 == str_2:
        print('Первая строка получается из второй со сдвигом {}.'.format(shift_number + 1))
        turned_out = True
        break

if not turned_out:
    print('Первую строку нельзя получить из второй с помощью циклического сдвига.')