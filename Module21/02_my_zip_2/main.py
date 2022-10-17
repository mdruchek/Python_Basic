def my_zip(*args, list_tuples=[]):
    for i_args in args:
        return list_tuples.append(my_zip(i_args))


a = [{"x": 4}, "b", "z", "d"]

b = (10, {20,}, [30], "z")

r = my_zip(a, b)
print(r)
