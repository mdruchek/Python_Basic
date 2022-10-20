def counting_numerals(file_read, file_write):
    file_numbers = open(file_read, 'r', encoding='utf8')
    numbers_str = file_numbers.read()
    file_numbers.close()

    summ = 0
    for symbol in numbers_str:
        if symbol.isdigit():
            summ += int(symbol)

    file_answer = open(file_write, 'w', encoding='utf8')
    file_answer.write(str(summ))
    file_answer.close()


counting_numerals('numbers.txt', 'answer.txt')