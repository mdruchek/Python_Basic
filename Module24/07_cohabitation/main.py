import random


class Drawer:
    def __init__(self):
        self.money = 0

    def give_money_away(self):
        if self.money > 0:
            self.money -= 10

    def accept_money(self):
        self.money += 30

    def return_amount_money(self):
        print('Количество денег в тумбочке {}.'.format(self.money))
        return self.money


class Fridge:
    def __init__(self):
        self.food = 50

    def give_away_food(self):
        if self.food > 0:
            self.food -= 10

    def take_food(self):
        if self.food <= 70:
            self.food += 30

    def return_amount_food(self):
        print('Количество еды в холодильнике {}.'.format(self.food))
        return self.food


class House:
    def __init__(self):
        self.drawer = Drawer()
        self.fridge = Fridge()
        self.dwellers = []

    def settle_guest(self, dweller):
        print('{} заселился в дом.'.format(dweller.name))
        self.dwellers.append(dweller)

    def evict_guest(self, dweller):
        print('{} покинул дом.'.format(dweller.name))
        self.dwellers.remove(dweller)


class Human:
    def __init__(self, name, house):
        self.name = name
        self.house = house
        self.degree_satiety = 50
        house.settle_guest(self)

    def eat(self):
        print('{} ест.'.format(self.name))
        self.house.fridge.give_away_food()

    def work(self):
        print('{} работает'.format(self.name))
        self.house.drawer.accept_money()

    def play(self):
        print('{} играет.'.format(self.name))
        self.degree_satiety -= 10

    def go_to_grocery_store_for_food(self):
        print('{} идёт в магазин за едой.'.format(self.name))
        self.house.drawer.give_money_away()
        self.house.fridge.take_food()

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
while number_day < 365