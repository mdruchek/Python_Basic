_string = input('Введите строку: ').split(' ')

len_words = [len(word) for word in _string]
len_max_word = max(len_words)

print('Самое длинное слово: ', _string[len_words.index(len_max_word)])
print('Длина этого слова: ', len_max_word)