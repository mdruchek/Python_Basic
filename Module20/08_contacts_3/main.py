def print_dict():
    print('Текущий словарь контактов: {}'.format(contacts))


def add_contact(name, telephone):
    contacts[name] = telephone
    print_dict()


def search(surname):
    return [print(i_key[0], i_key[1], i_value)
            for i_key, i_value in contacts.items() if surname in i_key]


contacts = dict()
while True:
    action = input('Введите номер действия:\n'
                   ' 1. Добавить контакт\n'
                   ' 2. Найти человека\n')
    if action == '1':
        name_surname = tuple(input('Введите имя и фамилию нового контакта (через пробел): ').split())
        if name_surname in contacts:
            print('Такой человек уже есть в контактах.')
            print_dict()
        else:
            telephone = int(input('Введите номер телефона: '))
            add_contact(name_surname, telephone)
    if action == '2':
        surname = input('Введите фамилию для поиска: ').title()
        if True in [True for i_key in contacts if surname in i_key]:
            search(surname)
        else:
            print('Такой фамилии в контактах нет.')