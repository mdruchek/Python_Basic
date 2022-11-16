import math

class MyMath:
    """
    Класс для расчёта математических функций
    """
    @classmethod
    def circle_len(cls, radius: float) -> float:
        """
        Метод класса для расчёта длины окружности
        :param radius: радиус окружности
        :type radius: float
        :return: длина окружности
        :rtype: float
        """
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        """
        Метод класса для расчёта площади круга
        :param radius: радиус окружности
        :type radius: float
        :return: площадь круга
        :rtype: float
        """
        return math.pi * radius ** 2

    @classmethod
    def cube_vl(cls, edge: float) -> float:
        """
        Метод класса для расчёта объёма куба
        :param edge: ребро куба
        :type edge: float
        :return: объём куба
        :rtype: float
        """
        return edge ** 3

    @classmethod
    def sphere_sq(cls, radius: float) -> float:
        """
        Метод класса для расчёта площади поверхности сферы
        :param radius: радиус сферы
        :type radius: float
        :return: площадь поверхности сферы
        :rtype: float
        """
        return 4 * math.pi * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
