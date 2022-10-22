import zipfile


def sort_by_frequency(input_list):
    return input_list[1]


def sort_by_alphabet(input_list):
    return input_list[0]


def generator_line_text(file_txt):
    for line in file_txt:
        yield line.decode(encoding='utf8')


def statistics_letters_in_zip(file_zip, file_txt, file_output):
    archive = zipfile.ZipFile(file_zip, 'r')
    file_txt = archive.open(file_txt, 'r')
    symbol_dict = dict()
    for line in generator_line_text(file_txt):
        for symbol in line:
            if 'А' <= symbol <= 'Я' or 'а' <= symbol <= 'я' or 'a' <= symbol <= 'z' or 'A' <= symbol <= 'Z':
                if symbol not in symbol_dict:
                    symbol_dict[symbol] = 1
                else:
                    symbol_dict[symbol] += 1

    file_txt.close()
    archive.close()

    sorted_list = sorted(symbol_dict.items(), key=sort_by_alphabet)
    sorted_list = sorted(sorted_list, key=sort_by_frequency)

    file_output = open(file_output, 'a', encoding='utf8')
    for elem in sorted_list:
        file_output.write('{} - {}\n'.format(elem[0], elem[1]))

    file_output.close()


statistics_letters_in_zip('voyna-i-mir.zip', 'voyna-i-mir.txt', 'statistics.txt')