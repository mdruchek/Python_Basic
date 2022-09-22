def summ_figure(number):
    summ = 0
    for figure in str(number):
        summ += int(figure)
    return summ


def quantity_figure(number):
    count = 0
    for figure in str(number):
        count += 1
    return count


number = int(input('Введите число: '))

summ = summ_figure(number)
quantity = quantity_figure(number)
print('Сумма чисел: ', summ)
print('Количество цифр в числе:', quantity)
print('Разность суммы и количества цифр: ', summ - quantity)
