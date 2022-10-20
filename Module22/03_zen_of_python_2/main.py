import os


def zen_counting(file):
    file_zen = open(file, 'r', encoding='utf8')
    data_zen = file_zen.read()

    number_letters = 0
    letters_dict = dict()
    for symbol in data_zen:
        if symbol.isalpha():
            number_letters += 1
            symbol = symbol.lower()
            if symbol not in letters_dict:
                letters_dict[symbol] = 1
            else:
                letters_dict[symbol] += 1

    min_number_repetitions_letters = min(letters_dict.values())
    rarest_letter = ''
    for i_key, i_value in letters_dict.items():
        if i_value == min_number_repetitions_letters:
            rarest_letter += i_key

    number_lines = len(data_zen.split('\n'))

    file_zen.seek(0)

    number_words = 0
    for line in file_zen:
        words_line_list = line.split(' ')
        for word in words_line_list:
            for symbol in word:
                if symbol.isalpha():
                    number_words += 1
                    break

    file_zen.close()

    return number_letters, number_words, number_lines, rarest_letter


path = os.path.abspath(os.path.join('..', '02_zen_of_python', 'zen.txt'))
number_letters, number_words, number_lines, rarest_letter = zen_counting(path)
print('Количество букв в файле: {number_letters}\n'
      'Количество слов в файле: {number_words}\n'
      'Количество строк в файле: {number_lines}\n'
      'Наиболее редкая буква: {rarest_letter}'.format(number_letters=number_letters,
                                                      number_words=number_words,
                                                      number_lines=number_lines,
                                                      rarest_letter=rarest_letter))