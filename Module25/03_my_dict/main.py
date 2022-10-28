class MyDict(dict):
    '''
    Класс MyDict. Родитель: dict
    '''
    def get(self, key):
        '''
        Переопределённый геттер возврата значения ключа (если ключа не существует - возвращает 0)

        :param key: ключ словаря
        :return: значение ключа или ноль
        '''
        if key in self:
            return self[key]
        return 0

# b = dict([(1, 1), (2, 4)])
#
# print(b)
# print(b.get(1))
# print(b.get(5))
#
# a = MyDict([(1, 1), (2, 4)])
#
# print(a)
# print(a.get(1))
# print(a.get(5))
