import datetime
from typing import Callable


def logging(func: Callable) -> Callable:
    """
    Декоратор логирования
    """
    print('Имя функции: {}'.format(func.__name__))
    print(func.__doc__)

    try:
        func()
    except Exception as exc:
        log_error = 'Имя функции: {name_func}\n' \
                    'Ошибка: {error}\n' \
                    '{date_time}\n\n'.format(name_func=func.__name__,
                                             error=exc,
                                             date_time=datetime.datetime.now())

        with open('function_errors.log', 'a', encoding='utf8') as log_file:
            log_file.write(log_error)
    return func


@logging
def divide_by_zero() -> None:
    """
    Функция с делением на ноль.
    """
    1 / 0


@logging
def type_error() -> None:
    """
    Функция с ошибкой типа
    """
    1 + 'q'


divide_by_zero()
type_error()
