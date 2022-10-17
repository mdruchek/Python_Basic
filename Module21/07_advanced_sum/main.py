def sum(*args, _sum=[0]):
    if len(args) == 1:
        args = args[0]
    for elem in args:
        if isinstance(elem, list):
            sum(elem)
        else:
            _sum[0] += elem
    return _sum[0]

#print(sum([[1, 2, [3]], [1], 3]))