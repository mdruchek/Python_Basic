quantity_number = int(input('Кол-во чисел: '))
initial_list = []

for _ in range(quantity_number):
    initial_list.append(int(input('Число: ')))
print('Последовательность: ', initial_list)

for _ in range(len(initial_list) // 2 + 1):
    flag = True
    for __ in range(len(initial_list) // 2 + 1):
        if initial_list[-len(initial_list) // 2 - __ - 1] != initial_list[-len(initial_list) // 2 + __]:
            flag = False
            break
    if flag: