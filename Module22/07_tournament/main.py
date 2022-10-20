def results_first_round(first_fail, second_fail):
    first_fail = open(first_fail, 'r', encoding='utf8')
    second_tour = dict()

    for number_line, line in enumerate(first_fail):
        if number_line == 0:
            passing_score = int(line)
        else:
            score = int(''.join([symbol
                                 for symbol in line
                                 if symbol.isdigit()]))
            if score > passing_score:
                second_tour[score] = number_line

    second_fail = open(second_fail, 'a', encoding='utf8')
    second_fail.write('2\n')
    number_line_write = 0
    for score, number_line_second in sorted(second_tour.items(), reverse=True):
        first_fail.seek(0)
        for number_line_first, line in enumerate(first_fail):
            if number_line_first == number_line_second:
                number_line_write += 1
                line = line.split(' ')
                name = '{}.'.format(line.pop(1)[0])
                line.insert(0, name)
                line = ' '.join(line)
                second_fail.write('{number}) {line}'.format(number=number_line_write,
                                                            line=line))
                break

    first_fail.close()
    second_fail.close()


results_first_round('first_tour.txt', 'second_tour.txt')
