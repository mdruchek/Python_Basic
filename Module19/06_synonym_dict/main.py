number_words = int(input('Введите количество пар слов: '))

count = ['Первая', 'Вторая', 'Третья']

dictionary_synonyms = {couple: input('{} пара: '.format(count[couple])).split(' — ')
                       for couple in range(number_words)}

print()
word_found = False

while True:
    word = input('Введите слово: ').title()

    for couple in dictionary_synonyms:
        if word in dictionary_synonyms[couple]:
            synonym_index = dictionary_synonyms[couple].index(word)
            dictionary_synonyms[couple].reverse()
            synonym = dictionary_synonyms[couple][synonym_index]
            word_found = True
            break

    if word_found:
        break

    print('Такого слова в словаре нет.')

print('Синоним: {}'.format(synonym))