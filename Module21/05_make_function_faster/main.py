def calculating_math_func(data, faktorial = dict()):
    result = 1
    if data not in faktorial:
        for index in range(1, data + 1):
            result *= index
        faktorial[data] = result
    else:
        result = faktorial[data]
    result = faktorial[data] / data ** 3
    result = result ** 10
    return result
