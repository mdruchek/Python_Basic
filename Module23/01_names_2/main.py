import os


def length_names(file_data, file_log):
    sum_len_names = 0
    with open(file_data, 'r', encoding='utf8') as file_name, open(file_log, 'w', encoding='utf8') as file_log:
        for line_number, name in enumerate(file_name):
            len_name = len(name)
            if name.endswith('\n'):
                len_name -= 1
            try:
                if len_name < 3:
                    raise BaseException
            except BaseException:
                file_log.write('Ошибка: менее трёх символов в строке {}'.format(line_number + 1))
            sum_len_names += len_name

        print('Общее количество символов: {}'.format(sum_len_names))


length_names('people.txt', 'errors.log')
