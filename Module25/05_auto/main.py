from math import cos, sin, pi


class Car:
    """
    Базовый класс. Описывает автомобиль

    Args:
        coordinates (list): передаются начальные координаты автомобиля [x, y]
        direction_movement (int): передаётся направление движения автомобиля (угол в градусах)
    """
    def __init__(self, coordinates, direction_movement):
        self.__coordinates = coordinates
        self.__direction_movement = direction_movement

    def get_coordinates(self):
        """
        Геттер для возврата координат

        :return __coordinates: координаты
        :rtype __coordinates: list
        """
        return self.__coordinates

    def move(self, distance):
        """
        Метод движения автомобиля (изменяет координаты, в зависимости от направления и расстояния)

        Args:
        distance (int): передаётся расстояние, на которое передвигается автомобиль
        """
        self.__coordinates = [self.__coordinates[0] + round(distance * cos(self.__direction_movement * pi / 180), 2),
                              self.__coordinates[1] + round(distance * sin(self.__direction_movement * pi / 180), 2)]

    def turn(self, angle_rotation):
        """
        Метод поворота автомобиля (изменяет направление движения автомобиля)

        Args:
        angle_rotation (int): передаётся угол, на который нужно повернуть автомобиль
        """
        self.__direction_movement += angle_rotation


class Bus(Car):
    """
    Класс Bus. Родитель Car

    Atributs:
        __fare (int): стоимость проезда в автобусе за километр

    Args:
        coordinates (list): передаются начальные координаты автомобиля [x, y]
        direction_movement (int): передаётся направление движения автомобиля (угол в градусах)
        number_passengers (int): передаётся количество пассажиров в автобусе (по умолчанию 0)
        amount_money (int): передаётся количество денег в кассе автобуса (по умолчанию 0)
    """
    __fare = 1

    def __init__(self, coordinates, direction_movement, number_passengers=0, amount_money=0):
        super().__init__(coordinates, direction_movement)
        self.__number_passengers = number_passengers
        self.__amount_money = amount_money

    def get_number_passengers(self):
        """
        Геттер для возврата количества пассажиров

        :return __number_passengers: количество пассажиров
        :rtype__number_passengers: int
        """
        return self.__number_passengers

    def get_amount_money(self):
        """
        Геттер для возврата количества денег в кассе автобуса

        :return __amount_money: количество денег в кассе
        :rtype __amount_money: int
        """
        return self.__amount_money

    def enter(self, number_passengers):
        """
        Метод входа пассажиров (прибавляет количество пассажиров в автобусе)

        Args:
        number_passengers (int): передаётся количество пассажиров, вошедших в автобус
        """
        self.__number_passengers += number_passengers

    def exit(self, number_passengers):
        """
        Метод выхода пассажиров (убавляет количество пассажиров в автобусе)

        Args:
        number_passengers (int): передаётся количество пассажиров, вышедших из автобуса
        """
        self.__number_passengers -= number_passengers

    def move(self, distance):
        """
        Метод движения автомобиля (изменяет координаты, в зависимости от направления и расстояния и
                                    количество денег в кассе автобуса)

        Args:
        distance (int): передаётся расстояние, на которое передвигается автомобиль
        """
        super().move(distance)
        self.__amount_money += self.__number_passengers * Bus.__fare * distance


# print('Автомобиль')
# car = Car([5, 5], 90)
# print(car.get_coordinates())
# car.move(5)
# print(car.get_coordinates())
# car.turn(90)
# car.move(5)
# print(car.get_coordinates())
#
# print('Автобус')
# bus = Bus([5, 5], 90)
# print(bus.get_coordinates(), bus.get_number_passengers(), bus.get_amount_money())
# bus.enter(1)
# bus.move(5)
# print(bus.get_coordinates(), bus.get_number_passengers(), bus.get_amount_money())
# bus.enter(1)
# bus.turn(90)
# bus.move(5)
# print(bus.get_coordinates(), bus.get_number_passengers(), bus.get_amount_money())
# bus.exit(1)
# bus.turn(90)
# bus.move(5)
# print(bus.get_coordinates(), bus.get_number_passengers(), bus.get_amount_money())