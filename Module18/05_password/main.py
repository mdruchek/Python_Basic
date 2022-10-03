while True:
    password = input('Придумайте пароль: ')
    numbers = [simbol for simbol in password if simbol.isdigit()]
    if len(password) >= 8 and not password.islower() and len(numbers) >= 3:
        break
    print('Пароль ненадёжный. Попробуйте ещё раз.')

print('Это надёжный пароль!')