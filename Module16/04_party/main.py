guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']

while True:
    quantity_guests = len(guests)
    print('\nСейчас на вечеринке ', quantity_guests, ' человек: ', guests)
    question = input('Гость пришел или ушёл? ')


    if question == 'пришёл':
        name = input('Имя гостя: ')
        if quantity_guests < 6:
            print('Привет, ', name, '!')
            guests.append(name)
        else:
            print('Прости, Гоша, но мест нет.')

    if question == 'ушёл':
        name = input('Имя гостя: ')
        print('Пока, ', name, '!')
        guests.remove(name)

    if question == 'Пора спать':
        print('\nВечеринка закончилась, все легли спать')
        break
