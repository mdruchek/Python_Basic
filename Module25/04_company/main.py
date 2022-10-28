class Person:
    """
    Базовый класс. Описывает человека

    Args:
        name (str): передаётся имя человека
        surname (str): передаётся фамилия человека
        age (int): передаётся возраст человека
    """
    def __init__(self, name, surname, age):
        self.__name = name
        self.__surname = surname
        self.__age = age

    def get_name(self):
        '''
        Геттер возвращающий имя человека

        :return __name: имя
        :rtype __name: str
        '''
        return self.__name

    def get_surmane(self):
        '''
        Геттер возвращающий фамилию человека

        :return __surname: фамилия
        :rtype __surname: str
        '''
        return self.__surname

    def get_age(self):
        '''
        Геттер возвращающий возраст человека

        :return __age: возраст
        :rtype __age: str
        '''
        return self.__age


class Employee(Person):
    """
    Класс Emploee. Родитель: Person

    Args:
        name (str): передаётся имя человека
        surname (str): передаётся фамилия человека
        age (int): передаётся возраст человека
    """
    def salary_calculation(self):
        """
        Метод расчета зарплаты
        """
        pass


class Manager(Employee):
    """
    Класс Manager. Родитель: Person.Emploee

    Args:
        name (str): передаётся имя человека
        surname (str): передаётся фамилия человека
        age (int): передаётся возраст человека
    """
    def salary_calculation(self):
        """
        Метод расчета зарплаты

        :return : зарплата
        :rtype : float
        """
        return float(13000)


class Agent(Employee):
    """
    Класс Agent. Родитель: Person.Emploee

    Args:
        name (str): передаётся имя человека
        surname (str): передаётся фамилия человека
        age (int): передаётся возраст человека
        sales_volume (int): передаётся объём продаж
    """
    def __init__(self, name, surname, age, sales_volume):
        super().__init__(name, surname, age)
        self.__sales_volume = sales_volume

    def salary_calculation(self):
        """
        Метод расчета зарплаты

        :return salary: зарплата
        :rtype salary: float
        """
        salary = 5000 + self.__sales_volume * 5 / 100
        return salary


class Worker(Employee):
    """
    Класс Agent. Родитель: Person.Emploee

    Args:
        name (str): передаётся имя человека
        surname (str): передаётся фамилия человека
        age (int): передаётся возраст человека
        number_hour_worked (int): передаётся количество отработанных часов
    """
    def __init__(self, name, surname, age, number_hour_worked):
        super().__init__(name, surname, age)
        self.__number_hour_worked = number_hour_worked

    def salary_calculation(self):
        """
        Метод расчета зарплаты

        :return salary: зарплата
        :rtype salary: float
        """
        salary = 100 * self.__number_hour_worked
        return float(salary)


employees = [Manager('Иван', 'Иванов', 25),
             Manager('Василий', 'Сидоров', 29),
             Manager('Анна', 'Краева', 35),
             Agent('Антон', 'Залётин', 20, 100000),
             Agent('Евгений', 'Миронов', 21, 130000),
             Agent('Пётр', 'Петров', 23, 150000),
             Worker('Артур', 'Маринин', 19, 160),
             Worker('Михаил', 'Краев', 18, 140),
             Worker('Матвей', 'Зимин', 20, 130)
]

print('Имя\t\tФамилия\t\tВозраст\t\tЗарплата')
for employee in employees:
    print('{name}\t\t{surname}\t\t{age}\t\t{salary}'.format(name=employee.get_name(),
                                                            surname=employee.get_surmane(),
                                                            age=employee.get_age(),
                                                            salary=employee.salary_calculation()))