def permutation(_list, number):
    _list.remove(number)
    _list.append(number)
    return 0

import random

qyantity_number = int(input('Количество чисел в списке: '))

list_before_compression = [random.randint(0, 2) for _ in range(qyantity_number)]
print('Список до сжатия: ', list_before_compression)

[permutation(list_before_compression, number)
  if number == 0
  else number
  for number
  in list_before_compression]

list_before_compression = [number for number in list_before_compression if number != 0]

print('Список после сжатия: ', list_before_compression)