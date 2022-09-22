def identical_numbers(year):
    for figure_1 in str(year):
        count = 0
        for figure_2 in str(year):
            if figure_1 == figure_2:
                count += 1
    if count == 3:
        print(year)


year_1 = int(input('Введите первый год: '))
year_2 = int(input('Введите второй год: '))

print('Годы от', year_1, ' до ', year_2, ' с тремя одинаковыми цифрами: ')
for year in range(year_1, year_2 + 1):
    identical_numbers(year)
