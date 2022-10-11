import random

original_list = [random.randint(1, 10) for _ in range(10)]
new_list = zip([(i_value) for i_key, i_value in enumerate(original_list)
                if i_key % 2 == 0],
               [(i_value) for i_key, i_value in enumerate(original_list)
                if i_key % 2 != 0])

print('Оригинальный список: {}'.format(original_list))
print('Новый список: {}'.format([i_value for i_value in new_list]))