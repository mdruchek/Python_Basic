from collections.abc import Iterable


class LinkedList:
    """
    Класс "Связанный список": создаёт односвязанный список
    """
    def __init__(self) -> None:
        self.len_list = 0
        with open('list.txt', 'w', encoding='utf8'):
            pass

    def __iter__(self) -> Iterable:
        self.i_iter = 0
        self.file_list = open('list.txt', 'r', encoding='utf8')
        return self

    def __next__(self) -> str:
        self.i_iter += 1
        if self.i_iter > self.len_list:
            self.file_list.close()
            raise StopIteration
        else:
            return self.file_list.readline()[:-1]
    def __str__(self) -> str:
        with open('list.txt', 'r', encoding='utf8') as file:
            list_ = file.read()
            list_ = list_[: len(list_) - 1]
            return '[{}]'.format(list_.replace('\n', ' '))

    def append(self, elem: (str, int)) -> None:
        """
        Метод добавления элемента в список

        :param elem: добавляемый элемент
        :type elem: int, str
        """
        with open('list.txt', 'a', encoding='utf8') as file:
            file.write('{}\n'.format(elem))
        self.len_list += 1

    def get(self, index: int) -> str:
        """
        Метод чтения элемента по индексу

        :param index: индекс элемента
        :type index: int
        :return elem: элемент списка
        :rtype elem: str
        """
        count = 0
        with open('list.txt', 'r', encoding='utf8') as list_file:
            for elem in list_file:
                count += 1
                if count == index + 1:
                    return elem

    def remove(self, index: int) -> None:
        """
        Метод удаления элемента по индексу

        :param index: индекс элемента
        :type index: int
        """
        with open('list.txt', 'r+', encoding='utf8') as list_file, open('temp.txt', 'w+', encoding='utf8') as temp_file:
            count = 0
            for line in list_file:
                count += 1
                if count != index + 1:
                    temp_file.write(line)

        with open('list.txt', 'w+', encoding='utf8') as list_file, open('temp.txt', 'r+', encoding='utf8') as temp_file:
            for line in temp_file:
                list_file.write(line)

        self.len_list -= 1


my_list = LinkedList()
my_list.append(10)
my_list.append(20)
my_list.append(30)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)