def my_zip(*args):
    len_args = (len(arg) for arg in args)
    min_len_arg = min(len_args)
    args = ((elem for elem in arg) for arg in args)
    return [(list(arg)[index]
            for arg in args)
            for index in range(min_len_arg)]


# a = [1, 2, 3, 4, 5]
# b = {1: "s", 2: "q", 3: 4}
# x = (1, 2, 3, 4, 5)
# print(my_zip(a, b, x))
