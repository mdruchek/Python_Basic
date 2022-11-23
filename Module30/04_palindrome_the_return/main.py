from collections import Counter
from typing import List


if __name__ == '__main__':
    """
    Функция для проверки строки на полиндром
    """
    def can_be_poly(str_is_poly: str) -> bool:
        counter: Counter = Counter()
        for symbol in str_is_poly:
            counter[symbol] += 1
        not_even_number: List[str] = list(filter(lambda item: counter[item] % 2 != 0, counter))
        if len(str_is_poly) % 2 == 0 and len(not_even_number) == 0 or len(str_is_poly) % 2 != 0 and len(not_even_number) == 1:
            return True
        return False



    print(can_be_poly('abcba'))
    print(can_be_poly('abbbc'))
    print(can_be_poly('abba'))
    print(can_be_poly('abca'))
