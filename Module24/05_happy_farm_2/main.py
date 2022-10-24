class Potato:
    maturity_dict = {0: 'не взошла', 1: 'взошла', 2: 'цветёт', 3: 'зрелая'}

    def __init__(self, index):
        self.index = index
        self.maturity = 0

    def growth(self):
        if self.maturity < 3:
            self.maturity += 1

    def is_ripe(self):
        if self.maturity == 3:
            return True
        return False

    def info_maturity(self):
        return self.maturity

    def print_maturity(self):
        print('Картошка {} {}.'.format(self.index, self.maturity_dict[self.info_maturity()]))


class PotatoGarden:
    def __init__(self, count):
        self.potatoes = [Potato(index) for index in range(1, count + 1)]

    def growing_potatoes_garden(self):
        print('Картошка растёт.')
        for potato in self.potatoes:
            potato.growth()

    def print_maturity_garden(self):
        for potato in self.potatoes:
            potato.print_maturity()

    def are_all_ripe(self, print_printing):
        for potato in self.potatoes:
            if not potato.is_ripe():
                if print_printing:
                    print('Картошка ещё не созрела!\n')
                return False
        else:
            if print_printing:
                print('Вся картошка созрела. Можно собирать!\n')
            return True

    def harvesting(self):
        self.potatoes = []


class Farmer:
    gardens = []

    def __init__(self, name, garden):
        self.name = name
        self.gardens.append(garden)

    def harvesting(self):
        mature_gardens = []
        if self.are_all_ripe(False):
            for index_garden, garden in enumerate(self.gardens):
                    mature_gardens.append(index_garden)
            for index_mature_gardens in mature_gardens:
                self.gardens.pop(index_mature_gardens)
            print('Картошка собрана. Отличный урожай!')

    def care_garden(self):
        print('Фермер ухаживает за грядкой.')
        for garden in self.gardens:
            garden.growing_potatoes_garden()

    def maturity_check(self):
        for garden in self.gardens:
            garden.print_maturity_garden()

    def are_all_ripe(self, print_printing):
        return garden.are_all_ripe(print_printing)


garden = PotatoGarden(5)
farmer = Farmer('Паша', garden)
while not farmer.are_all_ripe(True):
    farmer.care_garden()
    farmer.maturity_check()

else:
    farmer.harvesting()
    garden.harvesting()