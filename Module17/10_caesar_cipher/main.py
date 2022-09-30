def point_or_space(symbol):
    if symbol == ' ':
        return ' '
    if symbol == '.':
        return '.'


def encrypt(text, shift):
    _str = ''
    alphabet = list('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    text = [point_or_space(symbol) if symbol == ' ' or symbol =='.'
                                   else alphabet.index(symbol) + shift
                                   for symbol in text]
    text = [point_or_space(symbol) if symbol == ' ' or symbol =='.' else symbol
                                   if symbol < len(alphabet) else symbol - len(alphabet)
                                   for symbol in text]
    text = [point_or_space(symbol) if symbol == ' ' or symbol =='.' else alphabet[symbol]
                                   for symbol in text]
    for symbol in text:
        _str += symbol
    return _str


text = list(input('Введите сообщение: '))
shift = int(input('Введите сдвиг: '))

print('Зашифрованное сообщение: ', encrypt(text, shift))