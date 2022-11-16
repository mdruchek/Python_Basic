import datetime


class Date:
    """
    Класс Дата для проверки даты на существование и инвертирования строки в собственный экземпляр

    Args:
        day (int): день
        month (int): месяц
        year (int): год

    Atributes:
        __day (int): день
        __month (int): месяц
        __year (int): год
    """
    def __init__(self, day: int, month: int, year: int) -> None:
        self.__day = day
        self.__month = month
        self.__year = year

    def __str__(self) -> str:
        return 'День: {day}    Месяц: {month}   Год: {year}'.format(day=self.__day, month=self.__month, year=self.__year)

    @classmethod
    def from_string(cls, date_str: str) -> 'Date':
        """
        Метод класса для конвертирования строки в собственный экземпляр

        :param date_str: дата в формате строки
        :type date_str: str
        :return: экземпляр класса Date
        :rtype: Date
        """
        date_lst = date_str.split('-')
        return cls(day=int(date_lst[0]), month=int(date_lst[1]), year=int(date_lst[2]))

    @classmethod
    def is_date_valid(cls, date_str: str) -> bool:
        """
        Метод класса для проверки корректности даты

        :param date_str: дата в формате строки
        :type date_str: str
        :return: bool
        :rtype: bool
        """
        try:
            date_lst = date_str.split('-')
            datetime.date(int(date_lst[2]), int(date_lst[1]), int(date_lst[0]))
            return True
        except:
            return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
