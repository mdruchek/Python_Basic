def sorting_average_score(student):
    return sum(student.academic_performance) / len(student.academic_performance)


class Student:
    def __init__(self, surname_name, group_number, academic_performance = []):
        self.surname_name = surname_name
        self.group_number = group_number
        self.academic_performance = academic_performance

students = [Student('Иванов Иван', 1, [5, 5, 5, 5, 5]),
            Student('Марков Пётр', 2, [5, 4, 5, 4, 5]),
            Student('Петров Пётр', 2, [5, 4, 4, 4, 5]),
            Student('Сидоров Василий', 1, [5, 5, 5, 5, 4]),
            Student('Егорова Валентина', 2, [5, 5, 4, 4, 5]),
            Student('Лукмазов Стас', 1, [5, 4, 5, 4, 3]),
            Student('Краева Арина', 2, [5, 5, 5, 5, 4]),
            Student('Васильев Михаил', 1, [5, 4, 4, 4, 4]),
            Student('Петрова Екатерина', 2, [3, 3, 4, 4, 5]),
            Student('Миронова Елизавета', 1, [5, 5, 5, 5, 5])]

students.sort(key=sorting_average_score, reverse=True)

print('Студенты, отсортированные по среднему баллу:')
for elem in students:
    print(elem.surname_name, sum(elem.academic_performance) / len(elem.academic_performance))