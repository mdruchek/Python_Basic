main_list = [1, 5, 3]
side_list_1 = [1, 5, 1, 5]
side_list_2 = [1, 3, 1, 5, 3, 3]

main_list.extend(side_list_1)
print('Кол-во цифр 5 при первом объединении:', main_list.count(5))
for _ in range(main_list.count(5)):
    main_list.remove(5)

main_list.extend(side_list_2)
print('Кол-во цифр 3 при втором объединении:', main_list.count(3))
print('Итоговый список:', main_list)