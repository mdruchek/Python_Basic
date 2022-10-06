def adding_descendant(_dict, _list):
    if _list[1] in _dict.keys():
        _dict[_list[1]][_list[0]] = {}
        return
    for key in _dict.keys():
        adding_descendant(_dict[key], _list)


quantity_people = int(input('Введите количество человек: '))

count = ['Первая', 'Вторая', 'Третья', 'Четвёртая', 'Пятая', 'Шестая', 'Седьмая', 'Восьмая']
family_tree = dict()
for index in range(quantity_people - 1):
    names_set = set()
    couple_list = input('{} пара: '.format(count[index])).split()
    names_set.update(set(couple_list))
    if index == 0:
        family_tree[couple_list[1]] = {couple_list[0]: {}}
    else:
        adding_descendant(family_tree, couple_list)

print(family_tree)
print(sorted(names_set))