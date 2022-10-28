class Property:
    """
    Базовый класс. Описывает имущество человека

    Args:
        worth (int): передаётся стоимость имущества
    """
    def __init__(self, worth):
        self.__worth = worth

    def get_worth(self):
        """
        Геттер для возврата стоимости

        :return __worth: стоимость
        :rtype __worth: int
        """
        return self.__worth

    def tax_calculation(self):
        """
        Метод расчета налогов на имущество
        """
        pass


class Apartment(Property):
    """
    Класс Квартира. Родитель: Property

    Args:
        worth (int): передаётся стоимость имущества
    """
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        """
        Метод расчета налогов на квартиру

        :return amount_tax: величина налога на квартиру
        :rtype float
        """
        amount_tax = self.get_worth() / 1000
        return amount_tax


class Car(Property):
    """
    Класс Машина. Родитель: Property

    Args:
        worth (int): передаётся стоимость имущества
    """
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        """
        Метод расчета налогов на квартиру

        :return amount_tax: величина налога на квартиру
        :rtype float
        """
        amount_tax = self.get_worth() / 200
        return amount_tax


class CountryHouse(Property):
    """
    Класс Машина. Родитель: Property

    Args:
        worth (int): передаётся стоимость имущества
    """
    def __init__(self, worth):
        super().__init__(worth)

    def tax_calculation(self):
        """
        Метод расчета налогов на квартиру

        :return amount_tax: величина налога на квартиру
        :rtype float
        """
        amount_tax = self.get_worth() / 500
        return amount_tax


money = int(input('Количество ваших денег: '))
price_apartment = int(input('Стоимость квартиры: '))
price_car = int(input('Стоимость машины: '))
price_country_house = int(input('Стоимость загородного дома: '))
apartment = Apartment(worth=price_apartment)
car = Car(worth=price_car)
country_house = CountryHouse(worth=price_country_house)
tax_apartment = apartment.tax_calculation()
tax_car = car.tax_calculation()
tax_country_house = country_house.tax_calculation()
sum_tax = tax_apartment + tax_car + tax_apartment

print('Налог на квартиру составит: {tax_apartment}\n'
      'Налог на машину составит: {tax_car}\n'
      'Налог на дачу составит: {tax_country_house}'.format(tax_apartment=tax_apartment,
                                                           tax_car=tax_car,
                                                           tax_country_house=tax_country_house))

if sum_tax > money:
    print('Вам не хватает {}'.format(sum_tax - money))