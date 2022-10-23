import random


class Unit:
    def __init__(self, name, index, health = 100):
        self.name = name
        self.health = health
        self.index = index

    def skip_beat(self):
        if self.health > 0:
            self.health -= 20

    def is_alive(self):
        if self.health > 0:
            return True
        return False


class FightUnit:
    def __init__(self, count):
        self.count = count
        self.units = [Unit('воин', index) for index in range(1, count + 1)]

    def attack(self):
        who_is_attacking = self.units[random.randint(0, len(self.units) - 1)]
        potential_victim = self.units.copy()
        potential_victim.remove(who_is_attacking)
        whom_is_attacking = potential_victim[random.randint(0, len(potential_victim) - 1)]
        whom_is_attacking.skip_beat()
        print('Атаковал {name_who}{index_who},'
              'у {name_whom}{index_whom} осталось {health_whom} здоровья'.format(name_who=who_is_attacking.name,
                                                                                 index_who=who_is_attacking.index,
                                                                                 name_whom=whom_is_attacking.name,
                                                                                 index_whom=whom_is_attacking.index,
                                                                                 health_whom=whom_is_attacking.health))
        if not whom_is_attacking.is_alive():
            self.units.remove(whom_is_attacking)

    def is_stopped(self):
        if len(self.units) == 1:
            return True
        return False

    def print_results(self):
        if len(self.units) == 1:
            print('Победитель {}{}'.format(self.units[0].name,
                                            self.units[0].index))
        else:
            print('Битва ещё не закончилась.')


fight = FightUnit(2)
while not fight.is_stopped():
    fight.attack()
else:
    fight.print_results()