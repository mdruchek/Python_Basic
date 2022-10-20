import os


def write_file(path_file):
    file = open(path_file, 'w', encoding='utf8')
    file.write(text)
    file.close()


def text_editor(text, save_path, file_name):
    save_path = os.path.abspath(os.path.join('/', os.path.sep.join(save_path)))
    if os.path.exists(save_path):
        path_file = os.path.join(save_path, '{}.txt'.format(file_name))
        if os.path.exists(path_file):
            question = input('Вы действительно хотите перезаписать файл? ')
            if question.lower() == 'да':
                write_file(path_file)
                print('Файл успешно перезаписан!')
            else:
                return
        else:
            write_file(path_file)
            print('Файл успешно сохранён!')

        file = open(path_file, 'r', encoding='utf8')
        file_data = file.read()
        print('Содержимое файла:\n{}'.format(file_data))
        file.close()

    else:
        print('Данная директория не существует!')
        return


text = input('Введите строку: ')
save_path = input('Куда хотите сохранить документ? Введите последовательность папок (через пробел): ').split(' ')
file_name = input('Введите имя файла: ')
text_editor(text, save_path, file_name)