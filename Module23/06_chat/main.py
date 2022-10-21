import os


def registration():
    with open('secret.txt', 'a', encoding='utf8') as secret:
        name = input('Введите имя: ')
        if not name.isalpha():
            raise NameError
        password = input('Введите пароль: ')
        if len(password) < 6 and (password.isdigit() or password.isalpha()):
            raise TypeError

        secret.write('{} {}\n'.format(name, password))


def checking_name_registered_users(name):
    users = dict()
    with open('secret.txt', 'r', encoding='utf8') as secret:
        for user in secret:
            name_password = user.split()
            users[name_password[0]] = users[name_password[1]]
        if name in users.keys():
            chat_open(name)
