from typing import Dict, List
import requests
import json
from functools import reduce


if __name__ == '__main__':


    rec_links = requests.get('https://www.breakingbadapi.com/api/')

    rec_death = requests.get(json.loads(rec_links.text)['deaths'])
    data: List[Dict] = json.loads(rec_death.text)
    max_death: Dict = reduce(lambda max_, dict_: dict_ if dict_['number_of_deaths'] > max_['number_of_deaths'] else max_,
                             data, data[0])
    print('Максимальное количество смертей({number_death}) '
          'произошло в {episode} эпизоде.'.format(number_death=max_death['number_of_deaths'],
                                                  episode=max_death['episode']))
    with open('my_test.json', 'w') as file:
        json.dump(max_death, file, indent=4)
