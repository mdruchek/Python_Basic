number_orders = int(input('Введите количество заказов: '))

count = ['Первый', 'Второй', 'Третий', 'Четвёртый', 'Пятый', 'Шестой']
orders = dict()

for number in range(number_orders):
    order = input('{} заказ: '.format(count[number])).split(' ')

    if order[0] in orders.keys() and order[1] in orders[order[0]]:
        orders[order[0]][order[1]] += int(order[2])
    else:
        if order[0] not in orders.keys():
            orders[order[0]] = dict()
        orders[order[0]][order[1]] = int(order[2])

print()
for name in sorted(orders.keys()):
    print('{}:'.format(name))
    for pizza in sorted(orders[name]):
        print('\t\t{}: {}'.format(pizza, orders[name][pizza]))