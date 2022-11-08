import os
from  collections.abc import Iterable


def gen_files_path(dir: str, path: str = os.path.abspath(os.path.sep)) -> Iterable:
    """
    Функция для поиска директории и дальнейшего вывода путей файлов, которые в ней находятся

    :param dir: директория, файлы которой необходимо вывести
    :type dir: str
    :param path: директория, в которой осуществляется поиск
    :type path: str
    :return: путь файла
    :rtype: str
    """
    for elem in os.listdir(path):
        if os.path.isdir(os.path.join(path, elem)):
            if elem == dir:
                for (root, dirs, files) in os.walk(os.path.join(path, elem)):
                    for file in files:
                        yield os.path.join(root, file)
            for elem2 in gen_files_path(dir, os.path.join(os.path.abspath(path), elem)):
                yield elem2
