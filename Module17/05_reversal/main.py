_string = input('Введите строку: ')

symbol_h = [index for index in range(len(_string)) if _string[index] == 'h']
first_h = symbol_h[0]
end_h = symbol_h[len(symbol_h) - 1]

print('Развёрнутая последовательность между первым и последним h: ', _string[end_h - 1:first_h:-1])