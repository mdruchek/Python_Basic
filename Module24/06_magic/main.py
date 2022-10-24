class Water:
    def __init__(self):
        print('класс "Вода"', end='')

    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(self, Ground):
            return Mud()
        else:
            return None


class Air:
    def __init__(self):
        print('класс "Воздух"', end='')

    def __add__(self, other):
        if isinstance(other, Fire):
            return Lightning()
        elif isinstance(other, Ground):
            return Dust()
        else:
            return None


class Fire:
    def __init__(self):
        print('класс "Огонь"', end='')
    def __add__(self, other):
        if isinstance(other, Ground):
            return Lava()
        else:
            return None


class Ground:
    def __init__(self):
        print('класс "Земля"', end='')


class Storm:
    def __init__(self):
        print('класс "Шторм"')

class Steam:
    def __init__(self):
        print('класс "Пар"')


class Mud:
    def __init__(self):
        print('класс "Грязь"')


class Lightning:
    def __int__(self):
        print('класс "Молния"')

class Dust:
    def __init__(self):
        print('класс "Пыль"')

class Lava:
    def __init__(self):
        print('класс "Лава"')


a = Water()
print(' плюс ', end='')
b = Fire()
print(' получился ', end='')
c = a + b
