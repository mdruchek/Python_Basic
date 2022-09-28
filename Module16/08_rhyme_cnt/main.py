quantity_people = int(input('Кол-во человек: '))
number = int(input('Какое число в считалке: '))

print('Значит, выбывает каждый ', number, '-й человек')

list_people = list(range(1, quantity_people + 1))
print('\nТекущий круг людей: ', list_people)
print('Начало счёта с номера 1')

count = 1
while count <= number and len(list_people) != 1:
    account_start = 0
    for number_man in range(account_start, len(list_people)):
        if count == number:
            print('Выбывает человек под номером ', list_people[number_man])
            if len(list_people) == number_man + 1:
                account_start = 0
            else:
                account_start = list_people.index(list_people[number_man + 1])
            list_people.remove(list_people[number_man])

            if len(list_people) == 1:
                print('\nОстался человек под номером ', list_people[0])
                break

            print('\nТекущий круг людей: ', list_people)

            if account_start == 0:
                print('Начало счёта с номера ', list_people[0])
            else:
                print('Начало счёта с номера ', list_people[account_start - 1])

        if count == number:
            count = 1
        else:
            count += 1