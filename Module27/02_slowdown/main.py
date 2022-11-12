from time import sleep
from typing import Callable


def sleep_func(func: Callable) -> Callable:
    """
    Декоратор, откладывает выполнение функции на 10 сек
    """
    print('Начало задержки.')
    sleep(10)
    return func


@sleep_func
def function() -> None:
    """
    Функция
    """
    print('Функция выполнена.')


function()

print(function.__doc__)
