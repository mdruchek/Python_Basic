max_number = int(input('Введите максимальное число: '))

estimated_numbers_int = set(range(1, max_number + 1))
estimated_numbers_str = {str(num) for num in estimated_numbers_int}
while True:
    question_str = input('\nНужное число есть среди вот этих чисел: ')
    if question_str.title() == 'Помогите!':
        break
    question_set = set(question_str.split(' '))

    answer = input('Ответ Артёма: ')

    if answer.title() == 'Да':
        estimated_numbers_str &= question_set
    if answer.title() == 'Нет':
        estimated_numbers_str -= question_set

print('Артём мог загадать следующие числа: ', ' '.join(sorted(estimated_numbers_str)))