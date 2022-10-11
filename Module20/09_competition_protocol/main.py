number_records = int(input('Сколько записей вносится в протокол? '))
print('Записи (результат и имя):')

protocol = {index: (input('{}-я запись: '.format(index + 1)).split())
            for index in range(number_records)}

sorting_results = []
for i_record, i_result in sorted(protocol.items()):
    if i_record == 0:
        sorting_results.append(i_result)
    else:
        name_found = False
        for j_record, j_result in enumerate(sorting_results):
            if int(i_result[0]) > int(j_result[0]):
                sorting_results.insert(j_record, i_result)
                name_found = True
                break
        if not name_found:
            sorting_results.append(i_result)

players = set()
result_competition = []
for i_result in sorting_results:
    if len(result_competition) == 3:
        break
    if i_result[1] not in players:
        result_competition.append(i_result)
        players.add(i_result[1])

print('\nИтоги соевнований:')
[print('{}-е место. {} ({})'.format(i_place + 1, i_result[1], i_result[0]))
 for i_place, i_result in enumerate(result_competition)]