from datetime import datetime
import time
from typing import Callable
import functools


def log(func: Callable, date_format: str, class_) -> Callable:
    """
    Декоратор логирования
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        correct_date_format = ''.join(['%' + symbol if symbol.isalpha() else symbol for symbol in date_format])
        time_start = time.time()
        print("- Запускается '{class_name}.{method_name}'. "
              "Дата и время запуска: {datetime}".format(class_name=class_.__name__,
                                                        method_name=func.__name__,
                                                        datetime=datetime.today().strftime(correct_date_format)))
        result = func(*args, **kwargs)

        working_hours = round(time.time() - time_start, 3)
        print("- Завершение '{class_name}.{method_name}', "
              "время работы = {working_hours}s".format(class_name=class_.__name__,
                                                       method_name=func.__name__,
                                                       working_hours=working_hours))
        return result
    wrapper.date_format = date_format
    return wrapper


def log_methods(date_format: str) -> Callable:
    """
    Декорирование всех методов класса
    """
    def decorator_method(cls):
        for method in dir(cls):
            if method.startswith('__') is False:
                cur_method = getattr(cls, method)
                decor_method = log(cur_method, date_format, cls)
                setattr(cls, method, decor_method)
        return cls
    return decorator_method


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
