def output_result(_dict, name_dict):
    print('{} словарь частот: '.format(name_dict))
    for i_key in sorted(_dict.keys()):
        print('{} : {}'.format(i_key, _dict[i_key]))


def inverted_frequency_dictionary_dict(_dict):
    inverted_dictionary = {val: [] for val in set(_dict.values())}
    for i_key in _dict:
        inverted_dictionary[_dict[i_key]].append(i_key)
    return inverted_dictionary


def original_frequency_dictionary(text):
    original_dictionary = {symbol: 0 for symbol in text}

    for symbol in text:
        original_dictionary[symbol] += 1
    return original_dictionary


text = list(input('Введите текст: ').capitalize())

original_dictionary = original_frequency_dictionary(text)
inverted_dictionary = inverted_frequency_dictionary_dict(original_dictionary)

output_result(original_dictionary, 'Оригинальный')
output_result(inverted_dictionary, '\nИнвертированный')