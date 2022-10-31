from random import randint


class InhabitantsHouse:
    """
    Класс: Обитатели дома

    Args:
        name (str): имя
    """
    def __init__(self, name):
        self.__name = name
        self.__degree_satiety = 30

    def get_name(self):
        """
        Геттер для возврата имени

        :return __name: имя
        :rtype __name: str
        """
        return self.__name

    def get_degree_satiety(self):
        """
        Геттер для возврата уровня сытости

        :return __degree_satiety: стоимость
        :rtype __degree_satiety: int
        """
        return self.__degree_satiety

    def set_degree_satiety(self, degree_satiety):
        """
        Сеттер для изменения уровня сытости

        :param degree_satiety: уровень сытости
        :type degree_satiety: int
        """
        self.__degree_satiety = degree_satiety

    def check_into_house(self, house):
        """
        Метод заселения в дом

        :param house: екземпляр класса House
        :type house: House
        """
        self.__house = house

    def get_house(self):
        """
        Геттер для возврата объекта дом

        :return __house: дом
        :rtype __house: House
        """
        return self.__house

    def eat(self):
        """
        Метод 'Есть'
        """
        pass

    def action(self):
        """
        Метод любого действия, кроме есть
        """
        self.__degree_satiety -= 10

    def checking_is_alive(self):
        """
        Метод "проверить жив ли обитатель"

        :rtype: bool
        """
        if self.__degree_satiety > 0:
            return True
        return False


class People(InhabitantsHouse):
    """
    Класс Люди. Родитель: InhabitantsHouse

    Args:
        name (str): имя
    """
    def __init__(self, name):
        super().__init__(name)
        self.__degree_happiness = 100

    def get_degree_happiness(self):
        """
        Геттер для возврата уровня счастья

        :return __degree_happiness: уровень счастья
        :rtype __degree_happiness: int
        """
        return self.__degree_happiness

    def set_degree_happiness(self, degree_happiness):
        """
        Сеттер для изменения уровня счастья

        Args:
        degree_happiness (int): уровень счастья
        """
        self.__degree_happiness = degree_happiness

    def petting_cat(self):
        """
        Метод "Гладить кота" (+5 к счастью людей, -10 от сытости)
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

    Args:
        name (str): имя
    """
    def eat(self, mean=10):
        """
        Метод "есть" (+ 10 еды, степень сытости растёт на 2 пункта за 1 пункт еды)
        """
        if self.get_house().get_cat_food() > 0:
            if self.get_house().get_cat_food() < 10:
                mean = self.get_house().get_cat_food()
            self.set_degree_satiety(self.get_degree_satiety() + mean * 2)
            self.get_house().set_cat_food(self.get_house().get_cat_food() - mean)
            self.get_house().counting_sum_cat_food(mean)
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


class Husband(People):
    """
    Класс Муж. Родитель: People

    Args:
        name (str): имя
    """
    def play_computer_games(self):
        """
        Метод "играть"
        """
        super().action()
        self.set_degree_happiness(self.get_degree_happiness() + 20)
        print('{} поиграл. Уровень счастья {}.'.format(self.get_name(),
                                                       self.get_degree_happiness()))

    def go_work(self, money=250):
        """
        Метод "ходить на работу"
        """
        super().action()
        self.get_house().get_drawer().accept_money(money)
        print('{} схоил на работу. Количество денег стало {}.'.format(self.get_name(),
                                                                      self.get_house().get_drawer().get_money()))


class Wife(People):
    """
    Класс Жена. Родитель: People

    Args:
        name (str): имя
    """
    def buy_groceries(self, products=130):
        """
        Метод "покупать продукты"
        """
        super().action()
        if self.get_house().get_drawer().get_money() < products:
            products = self.get_house().get_drawer().get_money()
        self.get_house().get_drawer().give_money(products)
        self.get_house().get_fridge().accept_products(products)
        print('{} купила продукты. Количество денег стало {}.'
              'Количество продуктов стало {}'.format(self.get_name(),
                                                     self.get_house().get_drawer().get_money(),
                                                     self.get_house().get_fridge().get_products()))

    def buying_food_for_cat(self, food_cat=90):
        """
        Метод "покупать еду для кота"
        """
        super().action()
        if self.get_house().get_drawer().get_money() < food_cat:
            food_cat = self.get_house().get_drawer().get_money()
        self.get_house().get_drawer().give_money(food_cat)
        self.get_house().set_cat_food(self.get_house().get_cat_food() + food_cat)
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
        self.get_house().counting_number_fur_coats()
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


class Child(People):
    """
    Класс Ребенок. Родитель: People

    Args:
        name (str): имя
    """
    def play_with_toys(self):
        """
        Метод "играть в игрушки"
        """
        super().action()
        self.get_house().set_amount_dirt(self.get_house().get_amount_dirt() + 5)
        self.set_degree_happiness(self.get_degree_happiness() + 20)
        print('{} поиграл. Уровень счастья {}.'
              'Уровень грязи стал {}'.format(self.get_name(),
                                             self.get_degree_happiness(),
                                             self.get_house().get_amount_dirt()))


class Drawer:
    """
    Класс Тумбочка (Тумбочка хранит деньги).
    """
    def __init__(self):
        self.__money = 100
        self.__sum_money = 0

    def get_money(self):
        """
        Геттер для возврата количества денег в тумбочке

        :return __money: деньги
        :rtype __money: int
        """
        return self.__money

    def get_sum_money(self):
        """
        Геттер для возврата суммарного количества денег положенных в тумбочку

        :return __sum_money: деньги
        :rtype __sum_money: int
        """
        return self.__sum_money

    def accept_money(self, money):
        """
        Метод принять деньги

        :param money: деньги
        :type money: int
        """
        self.__money += money
        self.__sum_money += money

    def give_money(self, money):
        """
        Метод отдать деньги

        :param money: деньги
        :type money: int
        """
        self.__money -= money


class Fridge:
    """
    Класс Холодильник (Холодильник хранит продукты).
    """
    def __init__(self):
        self.__products = 50
        self.__sum_products = 0

    def get_products(self):
        """
        Геттер для возврата количества продуктов в холодильнике

        :return __products: продукты
        :rtype __products: int
        """
        return self.__products

    def get_sum_products(self):
        """
        Геттер для возврата общего количества продуктов

        :return __sum_products: суммарное количество продуктов
        :rtype __sum_products: int
        """
        return self.__sum_products

    def accept_products(self, products):
        """
        Метод принять продукты

        :param products: количество продуктов
        :type products: int
        """
        self.__products += products

    def give_products(self, products):
        """
        Метод отдать продукты
        """
        self.__products -= products
        self.__sum_products += products


class House:
    """
    Класс Дом.
    """
    def __init__(self):
        self.__drawer = Drawer()
        self.__fridge = Fridge()
        self.__cat_food = 30
        self.__sum_cat_food = 0
        self.__amount_dirt = 0
        self.__inhabitants_house_list = []
        self.__number_fur_coats = 0

    def get_inhabitants_house_list(self):
        """
        Геттер для возврата списка обитателей дома

        :return __inhabitants_house_list: обитатели дома
        :rtype __inhabitants_house_list: list
        """
        return self.__inhabitants_house_list

    def get_drawer(self):
        """
        Геттер для возврата экземпляра класса "Drawer"

        :return __drawer: экземпляр класса тумбочка
        :rtype __drawer: Drawer
        """
        return self.__drawer

    def get_fridge(self):
        """
        Геттер для возврата экземпляра класса "Холодильник"

        :return __fridge: экземпляр класса "Fridge"
        :rtype __fridge: Fridge
        """
        return self.__fridge

    def get_cat_food(self):
        """
        Геттер для возврата количества еды для кота

        :return __cat_food: количество еды для кота
        :rtype __cat_food: int
        """
        return self.__cat_food

    def get_amount_dirt(self):
        """
        Геттер для возврата количества грязи

        :return __amount_dirt: количество грязи
        :rtype __amount_dirt: int
        """
        return self.__amount_dirt

    def get_sum_cat_food(self):
        """
        Геттер для возврата суммарного количества еды для кота

        :return __sum_cat_food: суммарное количество еды для кота
        :rtype __sum_cat_food: int
        """
        return self.__sum_cat_food

    def get_number_fur_coats(self):
        """
        Геттер для возврата суммарного количества купленных шуб

        :return __number_fur_coats: суммарное количество купленных шуб
        :rtype __number_fur_coats: int
        """
        return self.__number_fur_coats

    def set_cat_food(self, cat_food):
        """
        Сеттер для изменения количества еды для кота

        :param cat_food: еда для кота
        :type cat_food: int
        """
        self.__cat_food = cat_food

    def set_amount_dirt(self, amount_dirt):
        """
        Сеттер для изменения уровня грязи

        :param amount_dirt: уровень грязи
        :type amount_dirt: int
        """
        self.__amount_dirt = amount_dirt

    def move_into_house(self, inhabitant_house):
        """
        Метод заселить в дом обитателя

        :param inhabitant_house: обитатель дома
        :type inhabitant_house: InhabitantsHouse
        """
        print('В дом заселился {}.'.format(inhabitant_house.get_name()))
        self.__inhabitants_house_list.append(inhabitant_house)

    def evict_from_house(self, inhabitant_house):
        """
        Метод выселить из дома обитателя

        :param inhabitant_house: обитатель дома
        :type inhabitant_house: InhabitantsHouse
        """
        print('Из дома выселился {}.'.format(inhabitant_house.get_name()))
        self.__inhabitants_house_list.remove(inhabitant_house)

    def counting_sum_cat_food(self, mean):
        """
        Метод подсчёта суммарного количества еды для кошек

        :param mean: еда для кошек
        :type mean: int
        """
        self.__sum_cat_food += mean

    def counting_number_fur_coats(self):
        """
        Метод подсчёта суммарного количества шуб
        """
        self.__number_fur_coats += 1


class LifeInHouse:
    """
    Класс "Жизнь в доме"

    Args:
        house (House): екземпляр класса House
    """
    def __init__(self, house):
        self.__house = house

    def create_new_life(self, inhabitant_house):
        """
        Метод "создать новую жизнь"

        :param inhabitant_house: обитатель дома
        :type inhabitant_house: InhabitantsHouse
        """
        self.__house.move_into_house(inhabitant_house)
        inhabitant_house.check_into_house(self.__house)

    def get_house(self):
        """
        Метод возврата екземпляра класса "House"

        :return __house: дом
        :rtype __house: House
        """
        return self.__house

    def pass_one_day(self):
        """
        Метод "один день"
        """
        for inhabitant in self.__house.get_inhabitants_house_list():
            if inhabitant.checking_is_alive():
                what_to_do = randint(1, 6)
                if isinstance(inhabitant, People) and inhabitant.get_degree_satiety() < 25 and self.__house.get_fridge().get_products() > 0:
                    inhabitant.eat()
                elif isinstance(inhabitant, Cat) and inhabitant.get_degree_satiety() < 25 and self.__house.get_cat_food() > 0:
                    inhabitant.eat()
                elif self.__house.get_fridge().get_products() < 20 and isinstance(inhabitant, Wife) and self.__house.get_drawer().get_money() > 0:
                    inhabitant.buy_groceries()
                elif self.__house.get_cat_food() < 30 and isinstance(inhabitant, Wife) and self.__house.get_drawer().get_money() > 0:
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
                        inhabitant.play_computer_games()
                    if isinstance(inhabitant, Wife):
                        inhabitant.petting_cat()
                    if isinstance(inhabitant, Child):
                        inhabitant.play_with_toys()
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
life_in_house.create_new_life(Child('Федя'))
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
print('Съедено еды котами: {}'.format(life_in_house.get_house().get_sum_cat_food()))
print('Куплено шуб: {}'.format(life_in_house.get_house().get_number_fur_coats()))