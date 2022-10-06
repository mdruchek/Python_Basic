violator_songs = {
    'World in My Eyes': 4.86,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.9,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.20,
    'Policy of Truth': 4.76,
    'Blue Dress': 4.29,
    'Clean': 5.83
}

counter = ['первой', 'второй', 'третьей']

quantity = int(input('Сколько песен выбрать? '))

sum_time = 0
for count in range(quantity):
    song = input('Название {} песни: '.format(counter[count]))
    sum_time += violator_songs[song]

print('\nОбщее время звучания песен: {} минуты'.format(round(sum_time, 2)))