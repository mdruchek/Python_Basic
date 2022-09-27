quantity_friends = int(input('Кол-во друзей: '))
quantity_receipt = int(input('Долговых расписок: '))
balance = [[], [], []]

for i_receipt in range(quantity_receipt):
    print('\n', i_receipt, '-я расписка')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    money = int(input('Сколько: '))
    
