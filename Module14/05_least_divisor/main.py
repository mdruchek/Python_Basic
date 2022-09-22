def smallest_divisor(number):
    for divisor in range(2, number):
        if number % divisor == 0:
            return divisor
    return number


number = int(input('Введите число: '))
print('Наименьший делитель, отличный от единицы: ', smallest_divisor(number))
