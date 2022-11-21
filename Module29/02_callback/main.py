import functools
from typing import Optional, Callable


app = dict()


def callback(_func: Optional[Callable] = None, *, route: str = None, ) -> Callable:
    """
    Декоратор для реализации callback функции
    """
    def decorator_function(func) -> Callable:
        app[route] = func
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    if _func:
        return decorator_function(_func)
    else:
        return decorator_function


@callback(route='//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')