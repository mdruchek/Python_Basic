quantity_people = int(input('Введите количество человек: '))

count = ['Первая', 'Вторая', 'Третья', 'Четвёртая', 'Пятая', 'Шестая', 'Седьмая', 'Восьмая']
family_tree = dict()

for index in range(quantity_people - 1):
    couple_list = input('{} пара: '.format(count[index])).split()
    if couple_list[1] not in family_tree.keys():
        family_tree[couple_list[1]] = 0
        family_tree[couple_list[0]] = 1
    else:
        family_tree[couple_list[0]] = family_tree[couple_list[1]] + 1

print('\nВысота каждого члена семьи:')
{print('{} {}'.format(key, family_tree[key])) for key in sorted(family_tree.keys())}