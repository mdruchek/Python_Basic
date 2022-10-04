def shift_word(shift, word_str):
    if word_str != '':
        word_list = [symbol for symbol in word_str]
        for transfer_symbol in range(shift):
            word_list.insert(0, word_list[len(word_list) - 1])
            word_list.pop()
        word_str_shift = ''
        for symbol in word_list:
            word_str_shift += symbol
        return word_str_shift


def special_characters(symbol):
    if symbol == ' ':
        return ' '
    if symbol == '.':
        return ''
    if symbol == '/':
        return ''
    if symbol == '(':
        return ''
    if symbol == '+':
        return ''
    if symbol == '"':
        return ''
    if symbol == '-':
        return ''


def decoded_text(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    shift = 51
    caesar_decoder_symbol_list = [alphabet[(alphabet.index(symbol) + shift) % len(alphabet)]
                      if symbol != ' ' and symbol != '.' and symbol != '/' and symbol != '(' and symbol != '+' and symbol != '"' and symbol != '-'
                      else special_characters(symbol)
                      for symbol in text]

    caesar_decoder_str = ''
    for symbol in caesar_decoder_symbol_list:
        caesar_decoder_str += symbol

    caesar_decoder_word_list = caesar_decoder_str.split(' ')
    caesar_decoder_word_shift_list = [shift_word(3, word_str) for word_str in caesar_decoder_word_list]

    return caesar_decoder_word_shift_list



text = 's .. fu(tm pe psfn gp tf"uip'

decoded = decoded_text(text)

print(decoded)