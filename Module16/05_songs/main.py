violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]

quantity_songs = int(input('Сколько песен выбрать? '))
summ_time = 0
for number_song in range(quantity_songs):
    song = input(f'Название {number_song + 1} -й песни: ')
    for i_song in range(len(violator_songs)):
        if song == violator_songs[i_song][0]:
            summ_time += violator_songs[i_song][1]
            break
print('\nОбщее время звучания песен: ', round(summ_time, ' минуты'))
