def counting_numerals(file_read, file_write):
    file_numbers = open(file_read, 'r', encoding='utf8')
    numbers_str = file_numbers.read()
    file_numbers.close()

    numbers_list = [int(elem) for elem in numbers_str.split()]

    file_answer = open(file_write, 'w', encoding='utf8')
    file_answer.write(str(sum(numbers_list)))
    file_answer.close()


counting_numerals('numbers.txt', 'answer.txt')