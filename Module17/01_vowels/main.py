text = input('Введите текст: ')

vowel_letters_list = [x for x in text if x == 'о' or x == 'е' or x == 'у' or x == 'ю' or x == 'а' or
                                         x == 'я' or x == 'ё' or x == 'э' or x == 'и' or x == 'ы']

print('\nСписок гласных букв: ', vowel_letters_list)
print('Длина списка: ', len(vowel_letters_list))