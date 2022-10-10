def checking_palindrome(text):
    palindrome = True
    number_of_odd_values = 0
    symbol_dict = dict()

    for symbol in text:
        if symbol in symbol_dict.keys():
            symbol_dict[symbol] += 1
        else:
            symbol_dict[symbol] = 1

    for value in symbol_dict.values():
        if value % 2 == 1:
            number_of_odd_values += 1

    if len(text) % 2 == 1 and number_of_odd_values == 1\
            or len(text) % 2 == 0 and number_of_odd_values == 0:
        print('Можно сделать палиндромом')
    else:
        print('Нельзя сделать палиндромом')


text_list = input('Введите строку: ')

checking_palindrome(text_list)