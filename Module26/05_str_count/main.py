import os
from collections.abc import Iterable


def gen_file_traversal(path: str) -> Iterable:
    """
    Генератор проходит по папкам дирректории, возвращая имена файлов с расширением *.py
    :param path: дирректория
    :type path: str
    :return: имена файлов с расширением *.py
    :rtype: str
    """
    for dir in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir)):
            for dir2 in gen_file_traversal(os.path.join(path, dir)):
                yield dir2
        else:
            if dir.endswith('.py'):
                yield os.path.join(path, dir)


def gen_passing_through_lines(path: str) -> Iterable:
    """
    Генератор для подсчёта строк исключая комментарии и пустые строки
    :param path: абсалютный путь файла
    :type path: str
    :return count_line: количество строк в файле
    :rtype int:
    """
    for file_py in gen_file_traversal(path):
        count_line = 0
        with open(file_py, 'r', encoding='utf8') as file:
            quotation_mark_number = 0
            for line in file:

                if line.startswith('"""') or line.startswith("'''"):
                    quotation_mark_number += 1
                if not line.lstrip('/t ').startswith('\n') and line[0] not in '#\'\"' and (quotation_mark_number == 0 or quotation_mark_number % 2 == 0):
                    count_line += 1

        yield count_line


def counting_rows_def(path: str) -> int:
    """
    Функция подсчета общего количества строк во всех файлах *.py
    :param path: дирректория
    :type path: str
    :return sum_line: суммарное количество строк
    :rtype sum_line: int
    """
    sum_line = 0
    for count in gen_passing_through_lines(path):
        sum_line += count
    return sum_line

#print(counting_rows_def(os.path.abspath(os.path.join('..', '..', 'Module14'))))