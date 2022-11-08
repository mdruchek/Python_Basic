def pairwise_multiplication() -> None:
    """
    Генератор перемножает попарно списки и ищет реультат, равный 56

    :return: строка из трёх чисел (что перемножается и результат)
    :rtype: строка
    """
    list_1 = [2, 5, 7, 10]
    list_2 = [3, 8, 4, 9]
    to_find = 56
    for x in list_1:
        for y in list_2:
            result = x * y
            yield '{x} {y} {result}'.format(x=x, y=y, result=result)
            if result == to_find:
                print('Found!!!')
                return

# a = pairwise_multiplication()
# for q in a:
#     print(q)