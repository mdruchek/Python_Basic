from typing import Any, Callable
import functools


def counter(func: Callable) -> Any:
    """
    Декоратор для счета количества вызовов функции
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        wrapper.count += 1
        print('Счётчик вызова функции: {}'.format(wrapper.count))
        result = func(*args, **kwargs)
        return result
    wrapper.count = 0
    return wrapper


@counter
def function() -> None:
    """Функция"""
    print('Функция выполнена.')


for _ in range(5):
    function()
    print()
