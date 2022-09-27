skates_size = []
foot_size = []
people_with_skates = 0

quantity_skates = int(input('Кол-во коньков: '))
for size in range(quantity_skates):
    skates_size.append(int(input(f'Размер {size + 1}-ой пары: ')))

quantity_peoples = int(input('\nКол-во людей: '))
for size in range(quantity_peoples):
    foot_size.append(int(input(f'Размер ноги {size + 1}-го человека: ')))

for foot in foot_size:
    for skates in skates_size:
        if foot <= skates:
            skates_size.remove(skates)
            people_with_skates += 1

print('\nНаибольшее кол-во людей, которые могут взять ролики: ', people_with_skates)
