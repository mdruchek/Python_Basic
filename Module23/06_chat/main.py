def registration(name):
    with open('secret.txt', 'a', encoding='utf8') as secret:
        print('Регистрация:')
        password = input('Введите пароль: ')
        if len(password) < 6 and (password.isdigit() or password.isalpha()):
            raise TypeError

        secret.write('{} {}\n'.format(name, password))
        chat_open(name)


def viewing_chat():
    try:
        with open('chat.txt', 'r', encoding='utf8') as chat_fail:
            print('*******ЧАТ********')
            for line in chat_fail:
                print(line, end='')
            print('*****************')
    except FileNotFoundError:
        print('В чате нет сообщений.')


def sending_message(name):
    with open('chat.txt', 'a', encoding='utf8') as chat_file:
        chat_file.write('{}: {}\n'.format(name, input('{}: '.format(name))))


def chat_open(name):
    print('Привет {}!'.format(name))
    print('Выберите действие:\n'
          '1. Просмотреть текущий текст чата.\n'
          '2. Отправить сообщение.')
    action = input()
    if action == '1':
        viewing_chat()
    elif action == '2':
        sending_message(name)
    else:
        raise ValueError


def checking_name_registered_users(name):
    users = dict()
    with open('secret.txt', 'r', encoding='utf8') as secret:
        for user in secret:
            name_password = user.split()
            b = name_password[0]
            c = name_password[1]
            users[name_password[0]] = name_password[1]
        if name in users.keys():
            password = input('Введите пароль: ')
            if users[name] == password:
                chat_open(name)
            else:
                raise PermissionError
        else:
            registration(name)


while True:
    try:
        name = input('Введите имя: ').capitalize()
        if not name.isalpha():
            raise NameError
        else:
            checking_name_registered_users(name)
            #chat_open(name)
    except NameError:
        print('Имя должно содержать только буквы')
    except TypeError:
        print('Пароль должен содержать не менее 6 символов и состоять из'
              'букв и цифр.')
    except PermissionError:
        print('Пароль не верный')
    except ValueError:
        print('Действие не верное')

