import itertools
from typing import List


if __name__ == '__main__':
    symbols: List = [sym for sym in range(10)]
    for item in itertools.combinations_with_replacement(symbols, 4):
        print(item)
