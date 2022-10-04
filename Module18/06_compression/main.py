unencoded_string = input('Введите строку: ')

unencoded_list_str = [simbol for simbol in unencoded_string]
encoded_list_str = [unencoded_list_str.remove(index - 1]) if list_str[index] == list_str[index - 1] else list_str.insert(index + 1, 3) for index in range(1, len(list_str))]

print(list_str)