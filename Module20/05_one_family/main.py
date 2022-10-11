families = {
    'Сидоров Никита': 35,
    'Сидорова Алина': 34,
    'Сидоров Павел': 10,
    'Иванов Иван': 18,
    'Иванова Мария': 18,
    'Иванов Радомир': 0
}

surname = input('Введите фамилию: ')
print()
[print(i_key, i_value) for i_key, i_value in families.items() if i_key.startswith(surname)]