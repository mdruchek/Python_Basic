from collections.abc import Iterable


class SquaresNumbersIter:
    """
    Класс Итератор квадратов чисел

    Args:

        number (int): число
    """
    def __init__(self, number: int) -> None:
        self.count = 0
        self.number = number

    def __iter__(self) -> Iterable:
        self.count = 0
        return self

    def __next__(self) -> int:
        self.count += 1
        if self.count > self.number:
            raise StopIteration
        else:
            return self.count ** 2


def square_numbers_generator(number: int) -> Iterable[int]:
    """
    Генератор квадратов чисел от 1 до number

    :param number: число
    :type number: int

    :return: квадрат числа
    :rtype: int
    """
    for i_number in range(1, number + 1):
        yield i_number ** 2


# number = int(input('Введите число: '))
# squares_iter = SquaresNumbersIter(number)
# for square in squares_iter:
#     print(square, end= ' ')
#
# print()
#
# squares_gen = square_numbers_generator(number)
# for square in squares_gen:
#     print(square, end=' ')
#
# print()
#
# squares_list_compl = (num ** 2 for num in range(1, number + 1))
# for square in squares_list_compl:
#     print(square, end=' ')
