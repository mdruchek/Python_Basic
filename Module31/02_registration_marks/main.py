import re


if __name__ == '__main__':
    numbers = r'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'
    pattern = r'[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]{2}\d{2,3}'
    print('Список номеров частных автомобилей: {}'.format(re.findall(pattern, numbers)))
    pattern = '[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}'
    print('Список номеров такси: {}'.format(re.findall(pattern, numbers)))