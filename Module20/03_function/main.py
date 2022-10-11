def slicer(_tuple, element):
    element_first = None
    element_second = None
    for index, i_element in enumerate(_tuple):
        if i_element == element:
            if element_first is None:
                element_first = index
                continue
            if element_second is None:
                element_second = index + 1
                continue
    if element not in _tuple:
        return tuple()
    else:
        return _tuple[element_first: element_second]

#print(slicer((1, 2, 3, 4, 5, 6, 7, 8, 2, 2, 9, 10), 2))