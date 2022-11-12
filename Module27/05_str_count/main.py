from typing import Any, Callable
import functools


def counter(func: Callable) -> Any:
    """
    Декоратор для счета количества вызовов функции
    """
    @functools.wraps(func)
    def wrapper() -> None:
        wrapper.count += 1
        print('Счётчик вызова функции: {}'.format(wrapper.count))
        func()
    wrapper.count = 0
    return wrapper


@counter
def function() -> None:
    """Функция"""
    print('Функция выполнена.')


for _ in range(5):
    function()
    print()
