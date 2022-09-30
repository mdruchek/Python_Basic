import random

first_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
second_team = [round(random.uniform(5, 10), 2) for _ in range(20)]
winners = [first_team[i_result]
           if first_team[i_result] > second_team[i_result]
           else second_team[i_result]
           for i_result in range(20)]

print('Первая команда: ', first_team)
print('Вторая команда: ', second_team)
print('Победители тура: ', winners)