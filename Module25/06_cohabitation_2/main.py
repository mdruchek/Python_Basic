from random import randint


class InhabitantsHouse:
    """
    Базовый класс: Обитатели дома
    """
    def __init__(self, name):
        self.__name = name
        self.__degree_satiety = 30

    def get_name(self):
        return self.__name

    def get_degree_satiety(self):
        return self.__degree_satiety

    def set_degree_satiety(self, degree_satiety):
        self.__degree_satiety = degree_satiety

    def check_into_house(self, house):
        self.__house = house

    def get_house(self):
        return self.__house

    def eat(self):
        """
        Метод 'Есть'
        """
        pass

    def action(self):
        self.__degree_satiety -= 10

    def checking_is_alive(self):
        """
        Метод "проверить жив ли обитатель"
        """
        if self.__degree_satiety > 0:
            return True
        return False


class People(InhabitantsHouse):
    """
    Класс Люди. Родитель: InhabitantsHouse
    """
    def __init__(self, name):
        super().__init__(name)
        self.__degree_happiness = 100

    def get_degree_happiness(self):
        return self.__degree_happiness

    def set_degree_happiness(self, degree_happiness):
        self.__degree_happiness = degree_happiness

    def petting_cat(self):
        """
        Метод "Гладить кота" (+5 к счастью людей)
        """
        super().action()
        self.__degree_happiness += 5
        print('{} погладил кота. Уровень счастья стал {}.'.format(self.get_name(),
                                                                  self.get_degree_happiness()))

    def eat(self, mean=30):
        """
        Метод "есть" (+ 30 еды, степень сытости растёт на 1 пункт за 1 пункт еды)
        """
        if self.get_house().get_fridge().get_products() > 0:
            if self.get_house().get_fridge().get_products() < 30:
                mean = self.get_house().get_fridge().get_products()
            self.set_degree_satiety(self.get_degree_satiety() + mean)
            self.get_house().get_fridge().give_products(mean)
            print('{} поел. Уровень сытости стал {}. '
                  'Еды в холодильнике стало {}.'.format(self.get_name(),
                                                        self.get_degree_satiety(),
                                                        self.get_house().get_fridge().get_products()))

    def checking_is_alive(self):
        """
        Метод "проверить жив ли человек"
        """
        if super().checking_is_alive() and self.__degree_happiness > 10:
            return True
        return False


class Cat(InhabitantsHouse):
    """
    Класс Кот. Родитель: InhabitantsHouse
    """
    __sum_food_cat_eat = 0

    def eat(self, mean=10):
        """
        Метод "есть" (+ 10 еды, степень сытости растёт на 2 пункта за 1 пункт еды)
        """
        if self.get_house().get_cat_food() > 0:
            if self.get_house().get_cat_food() < 10:
                mean = self.get_house().get_cat_food()
            self.set_degree_satiety(self.get_degree_satiety() + mean * 2)
            self.__sum_food_cat_eat += mean
            self.get_house().set_cat_food(self.get_house().get_cat_food() - mean)
            print('{} поел. Уровень сытости стал {}. '
                  'Еды кота стало {}.'.format(self.get_name(),
                                              self.get_degree_satiety(),
                                              self.get_house().get_cat_food()))

    def sleep(self):
        """
        Метод "спать"
        """
        super().action()
        print('{} поспал. Уровень сытости стал {}.'.format(self.get_name(),
                                                           self.get_degree_satiety()))

    def tear_up_wallpaper(self):
        """
        Метод "драть обои"
        """
        super().action()
        self.get_house().set_amount_dirt(self.get_house().get_amount_dirt() + 5)
        print('{} подрал обои. Уровень грязи стал {}.'.format(self.get_name(),
                                                              self.get_house().get_amount_dirt()))

    def get_sum_food_cat_eat(self):
        return self.__sum_food_cat_eat


class Husband(People):
    """
    Класс Муж. Родитель: People
    """
    def play(self):
        """
        Метод "играть"
        """
        super().action()
        self.set_degree_happiness(self.get_degree_happiness() + 20)
        print('{} поиграл. Уровень счастья {}.'.format(self.get_name(),
                                                       self.get_degree_happiness()))

    def go_work(self):
        """
        Метод "ходить на работу"
        """
        super().action()
        self.get_house().get_drawer().accept_money(150)
        print('{} схоил на работу. Количество денег стало {}.'.format(self.get_name(),
                                                                      self.get_house().get_drawer().get_money()))


class Wife(People):
    """
    Класс Жена. Родитель: People
    """
    def buy_groceries(self):
        """
        Метод "покупать продукты"
        """
        super().action()
        self.get_house().get_drawer().give_money(10)
        self.get_house().get_fridge().accept_products(100)
        print('{} купила продукты. Количество денег стало {}.'
              'Количество продуктов стало {}'.format(self.get_name(),
                                                     self.get_house().get_drawer().get_money(),
                                                     self.get_house().get_fridge().get_products()))

    def buying_food_for_cat(self):
        """
        Метод "покупать еду для кота"
        """
        super().action()
        self.get_house().get_drawer().give_money(50)
        self.get_house().set_cat_food(self.get_house().get_cat_food() + 90)
        print('{} купила еду для кота. Количество денег стало {}.'
              'Количество еды для кота {}'.format(self.get_name(),
                                                  self.get_house().get_drawer().get_money(),
                                                  self.get_house().get_cat_food()))

    def buy_fur_coat(self):
        """
        Метод "покупать шубу"
        """
        super().action()
        self.get_house().get_drawer().give_money(350)
        self.set_degree_happiness(self.get_degree_happiness() + 60)
        print('{} купила шубу. Количество денег стало {}.'
              'Количество счастья стало {}.'.format(self.get_name(),
                                                    self.get_house().get_drawer().get_money(),
                                                    self.get_degree_happiness()))

    def clean_house(self):
        """
        Метод "убирать дом"
        """
        super().action()
        self.get_house().set_amount_dirt(self.get_house().get_amount_dirt() - 100)
        print('{} убрала дом. Количество грязи стало {}.'.format(self.get_name(),
                                                                 self.get_house().get_amount_dirt()))


class Drawer:
    """
    Класс Тумбочка.
    """
    def __init__(self):
        self.__money = 100
        self.__sum_money = 0

    def get_money(self):
        return self.__money

    def accept_money(self, money):
        """
        Метод принять деньги
        """
        self.__money += money
        self.__sum_money += money

    def give_money(self, money):
        """
        Метод отдать деньги
        """
        self.__money -= money

    def get_sum_money(self):
        return self.__sum_money


class Fridge:
    """
    Класс Холодильник.
    """
    def __init__(self):
        self.__products = 50
        self.__sum_products = 0

    def get_products(self):
        return self.__products

    def accept_products(self, products):
        """
        Метод принять продукты
        """
        self.__products += products

    def give_products(self, products):
        """
        Метод отдать продукты
        """
        self.__products -= products
        self.__sum_products += products

    def get_sum_products(self):
        return self.__sum_products


class House:
    """
    Класс Дом.
    """
    def __init__(self):
        self.__drawer = Drawer()
        self.__fridge = Fridge()
        self.__cat_food = 30
        self.__amount_dirt = 0
        self.__inhabitants_house_list = []

    def get_inhabitants_house_list(self):
        return self.__inhabitants_house_list

    def get_drawer(self):
        return self.__drawer

    def get_fridge(self):
        return self.__fridge

    def get_cat_food(self):
        return self.__cat_food

    def get_amount_dirt(self):
        return self.__amount_dirt

    def set_cat_food(self, food):
        self.__cat_food = food

    def set_amount_dirt(self, amount_dirt):
        self.__amount_dirt = amount_dirt

    def move_into_house(self, inhabitant_house):
        print('В дом заселился {}.'.format(inhabitant_house.get_name()))
        self.__inhabitants_house_list.append(inhabitant_house)

    def evict_from_house(self, inhabitant_house):
        print('Из дома выселился {}.'.format(inhabitant_house.get_name()))
        self.__inhabitants_house_list.remove(inhabitant_house)


class LifeInHouse:
    def __init__(self, house):
        self.__house = house

    def create_new_life(self, inhabitant_house):
        self.__house.move_into_house(inhabitant_house)
        inhabitant_house.check_into_house(self.__house)

    def get_house(self):
        return self.__house

    def pass_one_day(self):
        for inhabitant in self.__house.get_inhabitants_house_list():
            if inhabitant.checking_is_alive():
                what_to_do = randint(1, 6)
                if isinstance(inhabitant, People) and inhabitant.get_degree_satiety() < 25 and self.__house.get_fridge().get_products() > 0:
                    inhabitant.eat()
                elif isinstance(inhabitant, Cat) and inhabitant.get_degree_satiety() < 25 and self.__house.get_cat_food() > 0:
                    inhabitant.eat()
                elif self.__house.get_fridge().get_products() < 10 and isinstance(inhabitant, Wife):
                    inhabitant.buy_groceries()
                elif self.__house.get_cat_food() < 10 and isinstance(inhabitant, Wife):
                    inhabitant.buying_food_for_cat()
                elif self.__house.get_amount_dirt() > 100 and isinstance(inhabitant, Wife):
                    inhabitant.clean_house()
                elif self.__house.get_drawer().get_money() < 50 and isinstance(inhabitant, Husband):
                    inhabitant.go_work()
                elif isinstance(inhabitant, Wife) and self.__house.get_drawer().get_money() > 350:
                    inhabitant.buy_fur_coat()
                elif what_to_do == 1 and isinstance(inhabitant, Husband):
                    inhabitant.go_work()
                elif what_to_do == 2 and self.__house.get_fridge().get_products() > 0:
                    inhabitant.eat()
                elif what_to_do == 3 and isinstance(inhabitant, People):
                    inhabitant.petting_cat()
                else:
                    if isinstance(inhabitant, Husband):
                        inhabitant.play()
                    if isinstance(inhabitant, Wife):
                        inhabitant.petting_cat()
                    if isinstance(inhabitant, Cat):
                        inhabitant.tear_up_wallpaper()
                if self.__house.get_amount_dirt() > 90 and isinstance(inhabitant, People):
                    inhabitant.set_degree_happiness(inhabitant.get_degree_happiness() - 10)
            else:
                self.__house.evict_from_house(inhabitant)
        self.__house.set_amount_dirt(self.__house.get_amount_dirt() + 5)


life_in_house = LifeInHouse(House())
life_in_house.create_new_life(Husband('Петя'))
life_in_house.create_new_life(Wife('Лена'))
life_in_house.create_new_life(Cat('Барсик'))
life_in_house.create_new_life(Cat('Мурзик'))
life_in_house.create_new_life(Cat('Васька'))
for day in range(366):
    print('\nДень {}.'.format(day))
    life_in_house.pass_one_day()
print('______________')
print('Итоги за год:')
print('Заработано денег: {}'.format(life_in_house.get_house().get_drawer().get_sum_money()))
print('Съедено еды людьми: {}'.format(life_in_house.get_house().get_fridge().get_sum_products()))
print('Съедено еды котами: {}'.format(life_in_house.get_house()))