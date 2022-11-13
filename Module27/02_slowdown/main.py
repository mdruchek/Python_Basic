from time import sleep
from typing import Callable, Any
import functools


def sleep_func(func: Callable) -> Callable:
    """
    Декоратор, откладывает выполнение функции на 10 сек
    """
    @functools.wraps(func)
    def wrapper_func(*args, **kwargs) -> Any:
        print('Начало задержки.')
        sleep(10)
        result = func(*args, **kwargs)
        return result
    return wrapper_func


@sleep_func
def function() -> None:
    """
    Функция
    """
    print('Функция выполнена.')


function()
print(function.__doc__)
