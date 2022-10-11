def tpl_sort(_tuple):
    s = [True if i_value is int else False for i_value in _tuple]
    if False in [True if i_value % 1 == 0 else False for i_value in _tuple]:
        return _tuple
    else:
        return tuple(sorted(list(_tuple)))

#print(tpl_sort((6, 3, -1, 8, 4.2, 10, -5)))