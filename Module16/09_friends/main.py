quantity_friends = int(input('Кол-во друзей: '))
quantity_receipt = int(input('Долговых расписок: '))
bank = []
balans = []

for _ in range(quantity_receipt):
    print('\n', i_receipt + 1, '-я расписка')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    money = int(input('Сколько: '))
    receipt = [to_whom, from_whom, money]
    bank.append(receipt)

for _ in range(quantity_friends):
    for __ in _:
