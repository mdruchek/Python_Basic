from abc import ABC, abstractmethod
import math


class Shape2D(ABC):
    """
    Базовый абстрактный класс '2D-фигура'

    Attributes:
        _area (float): площадь треугольника
        _perimeter (float): периметр треугольника
    """
    @abstractmethod
    def __init__(self) -> None:
        self._area = None
        self._perimeter = None

    @property
    def _get_area(self) -> float:
        """
        Геттер для возврата площади фигуры

        :return _area: площадь фигуры
        :rtype _area: float
        """
        return self._area

    @property
    def _get_perimeter(self) -> float:
        """
        Геттер для возврата периметра фигуры

        :return _perimeter: периметр фигуры
        :rtype _perimeter: float
        """
        return self._perimeter

    @abstractmethod
    def _finding_area_figure(self) -> None:
        """
        Абстрактный класс для нахождения площади фигуры

        """
        pass

    @abstractmethod
    def _finding_perimeter_figure(self) -> None:
        """
        Абстрактный для нахождения периметра фигуры

        """
        pass


class Triangle(Shape2D):
    """
    Класс 'Треугольник', родитель: Shape2D

    Args:
        triangle_base (float): основание треугольника
        triangle_height (float): высота треугольника

    Attributes:
        _base (float): основание треугольника
        _height (float): высота треугольника
        _area (float): площадь треугольника
        _perimeter (float): периметр треугольника
    """
    def __init__(self, triangle_base: float, triangle_height: float) -> None:
        super().__init__()
        self._base = triangle_base
        self._height = triangle_height

    def _finding_area_figure(self) -> None:
        """
        Метод для расчёта площади треугольника
        """
        self._area = self._base * self._height / 2

    def _finding_perimeter_figure(self) -> None:
        """
        Метод для расчёта периметра треугольника
        """
        self._perimeter = self._base + 2 * (math.sqrt((self._base / 2) ** 2 + self._height ** 2))


class Square(Shape2D):
    """
    Класс 'Квадрат', родитель: Shape2D

    Args:
        square_side (float): сторона кватдрата

    Attributes:
        _side (float): сторона квадрата
        _area (float): площадь квадрата
        _perimeter (float): периметр квадрата
    """
    def __init__(self, square_side: float) -> None:
        super().__init__()
        self._side = square_side

    def _finding_area_figure(self) -> None:
        """
        Метод для расчёта площади квадрата
        """
        self._area = self._side ** 2

    def _finding_perimeter_figure(self) -> None:
        """
        Метод для расчёта периметра квадрата
        """
        self._perimeter = self._side * 4


class Shape3D(ABC):
    """
    Базовый абстрактный класс '3D-фигура'

    Attributes:
        _surface (list): список содержащий 2D-фигуры, из которых состоит 3D-фигура
        _surface_area (float): площадь поверхности 3D-фигуры
    """
    @abstractmethod
    def __init__(self) -> None:
        self._surface = list()
        self._surface_area = 0

    @property
    def surface_area(self) -> float:
        """
        Геттер для возврата площади поверхности фигуры
        :return _syrface_area: площадь поверхности фигуры
        :rtype _surface_area: float
        """
        return self._surface_area

    def calculation_surface_area(self) -> None:
        """
        Метод для расчёта площади поверхности
        """
        for shape in self._surface:
            self._surface_area += shape._get_area


class Pyramid(Shape3D, Square, Triangle):
    """
    Класс Пирамида. Родительли: Shape3D, Square, Triangle
    
    Args:
        square_side (float): сторона квадрата
        triangle_base (float): основание треугольника
        triangle_height (float): высота треугольника

    Attributes:
        _surface (list): список содержащий 2D-фигуры, из которых состоит 3D-фигура
        _surface_area (float): площадь поверхности 3D-фигуры
    """
    def __init__(self, square_side: float, triangle_base: float, triangle_height: float) -> None:
        super().__init__()
        square = Square(square_side=square_side)
        square._finding_area_figure()
        square._finding_perimeter_figure()
        self._surface.append(square)

        for _ in range(4):
            triangle = Triangle(triangle_base=triangle_base, triangle_height=triangle_height)
            triangle._finding_area_figure()
            triangle._finding_perimeter_figure()
            self._surface.append(triangle)


class Cube(Shape3D, Square):
    """
    Класс Куб. Родители: Shape3D, Square

    Args:
        square_side (float): сторона квадрата

    Attributes:
        _surface (list): список содержащий 2D-фигуры, из которых состоит 3D-фигура
        _surface_area (float): площадь поверхности 3D-фигуры
    """
    def __init__(self, square_side: float) -> None:
        super().__init__()
        for _ in range(6):
            square = Square(square_side=square_side)
            square._finding_area_figure()
            square._finding_perimeter_figure()
            self._surface.append(square)


# my_cube = Cube(square_side=1)
# my_cube.calculation_surface_area()
# print(my_cube.surface_area)
