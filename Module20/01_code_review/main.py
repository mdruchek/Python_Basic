def student_interests_len_surname(_dict):
    sum_len_surname = 0
    interests_students = set()

    for i_data in _dict.values():
        for j_key, j_value in i_data.items():
            if j_key == 'surname':
                sum_len_surname += len(j_value)
            if j_key == 'interests':
                interests_students.update(set(j_value))

    return interests_students, sum_len_surname


students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology', 'swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}

print('Список пар "ID студента - возраст": {}'.format([(id_student, data_student['age'])
                                                       for id_student, data_student in students.items()]))

interests_students, sum_len_surname = student_interests_len_surname(students)
print('Полный список интересов всех студентов: {}'.format(interests_students))
print('Общая длина всех фамилий студентов: {}'.format(sum_len_surname))