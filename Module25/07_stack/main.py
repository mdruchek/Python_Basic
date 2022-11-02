class DuplicationTaskAndPriority(Exception):
    """
    Класс: Дублирование задачи и приоритета. Родитель: Exception
    """
    pass


class Stack:
    """
    Класс: Стэк
    """
    def __init__(self):
        self.__stack_list = []

    def adding_element(self, element):
        """
        Метод добавления элемента в стек

        :param element: елемент который добавляется в стек
        :type element: list
        """
        self.__stack_list.append(element)

    def deleting_element(self):
        """
        Метод удаления элемента из стека

        :return: удаляемый элемент, либо False если стек пуст
        """
        if self.__stack_list:
            return self.__stack_list.pop()
        return False


class TaskManager:
    """
    Класс менеджер задач (сортирует задачи по приоритету)
    """
    def __init__(self):
        self.count = 0
        self.__stack1 = Stack()
        self.__stack2 = Stack()
        self.max_priority = 0

    def __str__(self):
        self.str_return = ''
        self.print_task()
        return self.str_return

    def definition_empty_and_full_stack(self):
        """
        Метод проверки какой из стеков пустой, а какой нет

        :return filled_stack, empty_stack: заполненный стек, пустой стек
        :rtype filled_stack, empty_stack: екземпляр класса Stack, екземпляр класса Stack,
        """
        filled_stack = None
        empty_stack = None
        temp1 = self.__stack1.deleting_element()
        temp2 = self.__stack2.deleting_element()
        if not temp1 and not temp2:
            filled_stack = self.__stack1
            empty_stack = self.__stack2
        if temp1 and not temp2:
            self.__stack1.adding_element(temp1)
            filled_stack = self.__stack1
            empty_stack = self.__stack2
        if not temp1 and temp2:
            self.__stack2.adding_element(temp2)
            filled_stack = self.__stack2
            empty_stack = self.__stack1
        if temp1 and temp2:
            self.__stack1.adding_element(temp1)
            self.__stack2.adding_element(temp2)
            if int(temp1[0]) > int(temp2[0]):
                filled_stack = self.__stack1
                empty_stack = self.__stack2
            if temp2[0] > temp1[0]:
                filled_stack = self.__stack2
                empty_stack = self.__stack1
        return filled_stack, empty_stack

    def print_task(self):
        """
        Метод формирования строки для __str__
        """
        filled_stack, empty_stack = self.definition_empty_and_full_stack()
        temp = filled_stack.deleting_element()
        if temp:
            temp[0] = str(temp[0])
            self.str_return += '{}{}'.format(' '.join(temp), '\n')

            self.print_task()
            filled_stack.adding_element(temp)
        else:
            return

    def new_task(self, task, priority):
        """
        Метод добавления новой задачи

        :param task: задача
        :type task: str

        :param priority: приоритет
        :type priority: int
        """
        filled_stack, empty_stack = self.definition_empty_and_full_stack()
        temp = filled_stack.deleting_element()
        if temp:
            if priority <= int(temp[0]):
                if priority == temp[0]:
                    try:
                        for i_task in temp:

                            if task == i_task:
                                raise DuplicationTaskAndPriority
                        temp[len(temp) - 1] = '{}{}'.format(temp[len(temp) - 1], ';')
                        temp.append(task)
                    except DuplicationTaskAndPriority:
                        print('Дублирование задачи и приоритета!')
                filled_stack.adding_element(temp)
                if priority != temp[0]:
                    filled_stack.adding_element([priority, task])
            else:
                empty_stack.adding_element(temp)
                self.new_task(task, priority)
                filled_stack.adding_element(self.__stack2.deleting_element())
        else:
            filled_stack.adding_element([priority, task])

    def del_task(self, task_del):
        """
        Метод удаления задачи

        :param task_del: задача, которую нужно удалить
        :type task_del: str
        """
        filled_stack, empty_stack = self.definition_empty_and_full_stack()
        temp = filled_stack.deleting_element()
        i_task_del = None
        for i_task, task in enumerate(temp):
            if i_task != 0:
                if task_del in task:
                    i_task_del = i_task
        if i_task_del:
            temp.pop(i_task_del)
            if temp[len(temp) - 1].endswith(';'):
                temp[len(temp) - 1] = temp[len(temp) - 1][:len(temp[len(temp) - 1]) - 1]
            if len(temp) > 1:
                filled_stack.adding_element(temp)
        else:
            empty_stack.adding_element(temp)
            self.del_task(task_del)
            filled_stack.adding_element(empty_stack.deleting_element())


manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
manager.new_task("сдать дз", 2)
manager.new_task("помыть посуду", 4)
print(manager)

manager.del_task("поесть")
print(manager)

manager.del_task("помыть посуду")
print(manager)

manager.del_task("отдохнуть")
print(manager)

manager.new_task("отдохнуть", 1)
print(manager)

