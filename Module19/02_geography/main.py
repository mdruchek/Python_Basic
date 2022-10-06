number_countries = int(input('Количество стран: '))

counter = ['Первый', 'Второй', 'Третий']

country_list = [input('{}ая страна: '.format(counter[country_number][:4])).split()
                for country_number in range(number_countries)]

country_dict = {country[0]: country[1:] for country in country_list}

for index in range(3):
    city_found = False
    city = input('\n{} город: '.format(counter[index]))
    for country in country_dict:
        if city in country_dict[country]:
            print('Город {} расположен в стране {}.'.format(city, country))
            city_found = True
            break

    if not city_found:
        print('По городу {} данных нет.'.format(city))