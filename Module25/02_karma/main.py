from random import randint


class KillError(Exception):
    """
    Класс KillError. Родитель: Exception
    """
    pass


class DrunkError(Exception):
    """
    Класс DrunkError. Родитель: Exception
    """
    pass


class CarCrashError(Exception):
    """
    Класс  CarCrashError. Родитель: Exception
    """
    pass


class GluttonyError(Exception):
    """
    Класс  GluttonyError. Родитель: Exception
    """
    pass


class DepressionError(Exception):
    """
    Класс  DepressionError. Родитель: Exception
    """
    pass


def one_day():
    """
    функция 'один день'. Описывает один день человека

    Atributes:
        exceptions (list): собственные исключения
        amount_karma (int): карма текущего дня

    :return amount_karma: карма текущего дня
    :type amount_karma: int

    :raise exceptions: список пользовательских исключений
    """
    exceptions = [KillError, DrunkError, CarCrashError, GluttonyError, DepressionError]
    amount_karma = randint(1, 7)
    if randint(1, 10) == 1:
        raise exceptions[randint(0, 4)]
    return amount_karma


KARMA = 500
current_karma = 0
while current_karma < KARMA:
    crime = None
    with open('karma.log', 'a', encoding='utf8') as karma_file:
        try:
            current_karma += one_day()
        except KillError:
            crime = 'Kill'
        except DrunkError:
            crime = 'Drunk'
        except CarCrashError:
            crime = 'CarCrash'
        except GluttonyError:
            crime = 'Gluttony'
        except DepressionError:
            crime = 'Depression'
        if crime:
            karma_file.write('{}\n'.format(crime))
print('Вы достигли просветления! Поздравляем!')