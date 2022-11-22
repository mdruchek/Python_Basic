from typing import Callable
import functools


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """
    Декоратор, позволяет другому декоратору принимать произвольные аргументы
    """
    def decorator_maker(*args, **kwargs):
        @functools.wraps(decorator)
        def decorator_wrapper(func):
            return decorator(func, *args, **kwargs)
        return decorator_wrapper
    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    """
    Другой декоратор
    """
    args_decorator = args
    kwargs_decorator = kwargs

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Переданные арги и кварги в декоратор: {}, {}'.format(args_decorator,
                                                                    kwargs_decorator))
        result = func(*args, **kwargs)
        return result
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет,", text, num)


decorated_function("Юзер", 101)
