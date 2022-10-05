_string = list(input('Введите строку: '))

compressed_string = []
compression = 1

for index in range(1, len(_string)):
    if _string[index] == _string[index - 1]:
        compression += 1
    else:
        compressed_string.append(_string[index - 1])
        compressed_string.append(str(compression))
        compression = 1
    if index == len(_string) - 1:
        compressed_string.append(_string[index])
        compressed_string.append(str(compression))

print('Закодированная строка: {}'.format(''.join(compressed_string)), )