nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def open_list(nice_list):
    for elem in nice_list:
        if isinstance(elem, list):
            open_list(elem)
        else:
            new_list.append(elem)

new_list = []
open_list(nice_list)
print('Ответ: {}'.format(new_list))