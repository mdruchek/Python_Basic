import os

def dirs_search(path, number_directories=0, number_files=0, sum_size_file=0):
    for elem in os.listdir(path):
        if os.path.isdir(os.path.join(path, elem)):
            number_directories += 1
            number_directories, number_files, sum_size_file = dirs_search(os.path.join(path, elem), number_directories, number_files, sum_size_file)
        else:
            number_files += 1
            sum_size_file += os.path.getsize(os.path.join(path, elem))/1024
    return number_directories, number_files, sum_size_file


path = os.path.abspath(os.path.join('..', '..', 'Module14'))
number_directories, number_files, size_dir = dirs_search(path)
print('Размер каталога (в Кб): {}\n'
      'Количество подкаталогов: {}\n'
      'Количество файлов: {}'.format(size_dir,
                                     number_directories,
                                     number_files))
