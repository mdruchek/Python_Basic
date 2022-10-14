def fibonachi(num_pos_user, num_pos_current=1, elem=None,
              elem_previous_1=None, elem_previous_2=None):
    if num_pos_current == 1:
        elem = 1
    elif num_pos_current == 2:
        elem = 1
        elem_previous_1 = 1
    else:
        elem_previous_2 = elem_previous_1
        elem_previous_1 = elem
        elem = elem_previous_1 + elem_previous_2

    if num_pos_current != num_pos_user:
        num_pos_current += 1
        fibonachi(num_pos_user, num_pos_current, elem, elem_previous_1, elem_previous_2)
    else:
        return number.append(elem)

number = []
num_pos = int(input('Введите позицию числа Фибоначчи: '))
fibonachi(num_pos)
print('Число: {}'.format(number[0]))