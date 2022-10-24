import random


class Drawer:
    def __init__(self):
        self.money = 0

    def give_money_away(self, how_many):
        if self.money > 0:
            self.money -= how_many

    def accept_money(self, how_many):
        self.money += how_many

    def return_amount_money(self):
        return self.money


class Fridge:
    def __init__(self):
        self.food = 50

    def give_away_food(self, how_many):
        if self.food > 0:
            self.food -= how_many

    def take_food(self, how_many):
        if self.food <= 70:
            self.food += how_many

    def return_amount_food(self):
        return self.food


class House:
    def __init__(self):
        self.drawer = Drawer()
        self.fridge = Fridge()
        self.dwellers = []

    def settle_guest(self, dweller):
        print('{} заселился в дом.'.format(dweller.name))
        self.dwellers.append(dweller)

    def dweller_is_alive(self):
        retired_dwellers = set()
        for dweller in self.dwellers:
            if not dweller.is_alive():
                print('{} покинул дом.'.format(dweller.name))
                retired_dwellers.add(dweller)
        self.dwellers = list(set(self.dwellers) - retired_dwellers)

    def return_count_dwellers(self):
        return len(self.dwellers)


class Human:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.degree_satiety = 50
        house.settle_guest(self)

    def eat(self):
        print('{} ест.'.format(self.name), end=' ')
        self.house.fridge.give_away_food(10)
        self.degree_satiety += 10
        print('Чуство сытости {}.'.format(self.degree_satiety))

    def work(self):
        print('{} работает'.format(self.name), end=' ')
        self.house.drawer.accept_money(10)
        self.degree_satiety -= 15
        print('Чуство сытости {}. Денег в тумбочке {}.'
              .format(self.degree_satiety, self.house.drawer.return_amount_money()))

    def play(self):
        print('{} играет.'.format(self.name), end=' ')
        self.degree_satiety -= 10
        print('Чуство сытости {}.'.format(self.degree_satiety))

    def go_to_grocery_store_for_food(self):
        print('{} идёт в магазин за едой.'.format(self.name), end=' ')
        if 0 < self.house.drawer.return_amount_money() < 10:
            how_many = self.house.drawer.return_amount_money()
        else:
            how_many = 10
        self.house.drawer.give_money_away(how_many)
        self.house.fridge.take_food(how_many)
        print('Денег в тумбочке {}. Еды в холодильнике {}.'
              .format(self.house.drawer.return_amount_money(), self.house.fridge.return_amount_food()))

    def what_to_do(self):
        cube = random.randint(1, 6)
        if self.degree_satiety < 20:
            self.eat()
        elif self.house.fridge.return_amount_food() < 10:
            self.go_to_grocery_store_for_food()
        elif self.house.drawer.return_amount_money() < 50:
            self.work()
        elif cube == 1:
            self.work()
        elif cube == 2:
            self.eat()
        else:
            self.play()

    def is_alive(self):
        if self.degree_satiety > 0:
            return True
        return False


house = House()
human1 = Human('Артем', house)
human2 = Human('Марина', house)
number_day = 0
while number_day < 365 and house.return_count_dwellers() > 0:
    number_day += 1
    print('\nДень {}'.format(number_day))
    number_dweller = random.randint(1, house.return_count_dwellers())
    house.dwellers[number_dweller - 1].what_to_do()
    house.dwellers[len(house.dwellers) - number_dweller].what_to_do()
    house.dweller_is_alive()
