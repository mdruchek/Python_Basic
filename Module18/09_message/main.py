def reverse_list(word_list):
    temp_list = []
    reverse_list = []
    if '.' in word_list or ',' in word_list or '!' in word_list or ':' in word_list:
        for symbol in word_list:
            if symbol != '.' and symbol != ',' and symbol != '!' and symbol != ':':
                temp_list.append(symbol)
            else:
                temp_list.reverse()
                reverse_list.extend(temp_list)
                reverse_list.append(symbol)
                temp_list = []
        if word_list[len(word_list) - 1].isalpha():
            temp_list.reverse()
            reverse_list.extend(temp_list)
    else:
        word_list.reverse()
        reverse_list = word_list
    return reverse_list


message = input('Сообщение: ').split(' ')

message_list = [[symbol for symbol in word] for word in message]
message_list_revers = [reverse_list(word) for word in message_list]

reverse = ' '.join([''.join(word) for word in message_list_revers])

print('Новое сообщение: {}'.format(reverse))