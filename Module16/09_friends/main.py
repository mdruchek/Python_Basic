quantity_friends = int(input('Кол-во друзей: '))
quantity_receipt = int(input('Долговых расписок: '))
balance = []
for _ in range(quantity_friends):
    balance.append(0)

for i_receipt in range(quantity_receipt):
    print('\n', i_receipt + 1, '-я расписка')
    to_whom = int(input('Кому: '))
    from_whom = int(input('От кого: '))
    money = int(input('Сколько: '))
    for i_friend in range(quantity_friends):
        if to_whom == i_friend + 1:
            balance[i_friend] = balance[i_friend] - money

        if from_whom == i_friend + 1:
            balance[i_friend] = balance[i_friend] + money

print('\nБаланс друзей:')
for i_friend in range(len(balance)):
    print(i_friend + 1, ': ', balance[i_friend])