def cesar_file(source_file, encrypted_file):
    alfabet = ''.join([chr(symbol) for symbol in range(97, 123)]) +\
              ''.join([chr(symbol) for symbol in range(65, 91)])

    source_file = open(source_file, 'r', encoding='utf8')
    encrypted_file = open(encrypted_file, 'a', encoding='utf8')
    for number_line, line in enumerate(source_file):
        encrypted_file.write(''.join([alfabet[alfabet.index(symbol) + number_line + 1]
                                      if symbol != '\n' else '\n'
                                      for symbol in line]))
    source_file.close()
    encrypted_file.close()


cesar_file('text.txt', 'cipher_text.txt')
