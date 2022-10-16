def sum(*args, _sum=[0]):
    if (isinstance(args, tuple) and len(args) == 1) or isinstance(args[0], list):
        args = args[0]
    for elem in args:
        if isinstance(elem, list):
            sum(elem, _sum[0])
        else:
            _sum[0] += elem
    return _sum[0]

#print(sum((1, 2, 3, 4, 5)))