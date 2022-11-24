import re
from typing import List


if __name__ == '__main__':
    phone_numbers: List[str] = ['9999999999', '999999-999', '99999x9999']
    pattern: str = r'[89]\d{9}'
    numerals_text = ['первый', 'второй', 'третий']
    for index, number in enumerate(phone_numbers):
        print('{} номер:'.format(numerals_text[index]), end=' ')
        if re.search(pattern, number):
            print('всё в порядке')
        else:
            print('не подходит')
