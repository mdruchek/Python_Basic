def sort_by_alphabet(input_list):
    return input_list[0]


def sort_by_frequency(input_list):
    return input_list[1]


def frequency_analysis(first_file, result_file):
    first_file = open(first_file, 'r', encoding='utf8')
    data_first_file = first_file.read()
    first_file.close()

    data_first_file_dict = dict()
    number_symbols = 0
    for symbol in data_first_file:
        if symbol.isalpha():
            number_symbols += 1
            if symbol.lower() in data_first_file_dict:
                data_first_file_dict[symbol.lower()] += 1
            else:
                data_first_file_dict[symbol.lower()] = 1

    data_first_file_list = []
    for symbol, number in data_first_file_dict.items():
        data_first_file_list.append([symbol, str(round(data_first_file_dict[symbol] / number_symbols, 3))])

    data_first_file_list.sort(key=sort_by_alphabet)
    data_first_file_list.sort(key=sort_by_frequency, reverse=True)

    data_first_file_str = '\n'.join(' '.join(elem) for elem in data_first_file_list)

    result_file = open(result_file, 'w', encoding='utf8')
    result_file.write(data_first_file_str)
    result_file.close()


frequency_analysis('text.txt', 'analysis.txt')