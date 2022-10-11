def is_prime(number):
    prime_bool = True
    if number == 0 or number == 1:
        return False
    for divider in range(2, number):
        if number % divider == 0:
            prime_bool = False
    return prime_bool


def _isinstance(iterable_object):
    if isinstance(iterable_object, dict):
        return iterable_object.items()
    else:
        return iterable_object


def crypto(iterable_object):
    return [symbol
            for index, symbol in enumerate(_isinstance(iterable_object))
            if is_prime(index)]


#print(crypto([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
