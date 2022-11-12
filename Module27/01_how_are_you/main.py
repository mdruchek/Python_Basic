from typing import Callable, Any
import functools


def how_are_you(func: Callable) -> Any:
    """Декоратор"""
    @functools.wraps(func)
    def wrapper_func() -> None:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        func()
    return wrapper_func


@how_are_you
def test() -> None:
    """Функция"""
    print('<Тут что-то происходит...>')


test()
