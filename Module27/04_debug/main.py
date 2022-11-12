from typing import Callable
import functools


def debug(func: Callable) -> Callable:
    """
    Декоратор для вывода информации о функции
    """
    @functools.wraps(func)
    def wrapped(*args, **kwargs) -> None:
        age_return = None
        if kwargs:
            if kwargs.get('name'):
                name_return = 'name={}'.format(repr(kwargs['name']))
            if kwargs.get('age'):
                age_return = 'age={}'.format(kwargs['age'])
        if args:
            name_return = repr(args[0])
            if len(args) == 2:
                age_return = args[1]

        if not age_return:
            print('Вызывается {func_name}({name})'.format(func_name=func.__name__,
                                                          name=name_return))
        else:
            print('Вызывается {func_name}({name}, {age})'.format(func_name=func.__name__,
                                                                 name=name_return,
                                                                 age=age_return))
        return_func = func(*args, **kwargs)
        print('{func_name} вернула значение {meaning}'.format(func_name=repr(func.__name__),
                                                              meaning=repr(return_func)))
        print(return_func)
        print()
    return wrapped


@debug
def greeting(name: str, age: int = None) -> str:
    """
    Функция
    :param name: Имя
    :type name: str
    :param age: возраст
    :type age: int
    :return: Приветствие
    :rtype: str
    """
    if age:
        return "Ого, {name}! Тебе уже {age} лет, ты быстро растёшь!".format(name=name, age=age)
    else:
        return "Привет, {name}!".format(name=name)


greeting("Том")
greeting("Миша", age=100)
greeting(name="Катя", age=16)
