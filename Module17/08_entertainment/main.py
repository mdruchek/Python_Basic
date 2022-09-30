import random

def throw(number_throws, quantity_sticks):
    left = random.randint(1, quantity_sticks)
    right = random.randint(left, quantity_sticks)
    print('Бросок ', number_throws)
    print('Сбиты палки с номера ', left, ' по номер ', right)
    return [left, right]


quantity_sticks = int(input('Количество палок: '))
quantity_throws = int(input('Количество бросков: '))
graphics = ''

throws = [throw(i_throws, quantity_sticks) for i_throws in range(1, quantity_throws + 1)]
sticks = ['|' for _ in range(quantity_sticks)]
for throw in range(quantity_throws):
    sticks = [('.' if throws[throw][0] - 2 < stick < throws[throw][1] or sticks[stick] == '.' else '|') for stick in range(quantity_sticks)]
for simbol in sticks:
    graphics += simbol

print('\nРезультат:', graphics)

