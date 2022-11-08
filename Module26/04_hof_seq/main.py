from collections.abc import Iterable


class QHofstadter:
    """
    Класс QHofstadter: для формирования последовательности Q Хофштадтера

    Arg:
        list_ (list): список с двумя начальными значениями последовательности
    """
    def __init__(self, list_: list) -> None:
        self.list_ = list_[:]


    def __iter__(self) -> Iterable:
        return self

    def __next__(self) -> None:
        if self.list_[0] != 1 or self.list_[1] != 1:
            raise StopIteration
        else:
            self.list_.append(self.list_[len(self.list_) - self.list_[-1]] + self.list_[len(self.list_) - self.list_[-2]])

    def print_q_hofstadter(self) -> None:
        """
        Метод печати сформированной последовательности
        """
        print(self.list_)


# q = QHofstadter([1, 1])
# q_iter = q.__iter__()
# for _ in range(20):
#     q_iter.__next__()
# q.print_q_hofstadter()
