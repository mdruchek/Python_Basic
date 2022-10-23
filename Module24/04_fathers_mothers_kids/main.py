
class Parent:
    def __init__(self, name, age, gender, childrens = []):
        self.name = name
        self.age = age
        self.gender = gender
        self.childrens = childrens

    def return_information_about_yourself(self):
        return self.name, self.age, self.gender

    def calm_child_down(self, children):
        if children.return_condition() > 1:
            children.calm_down()


    def feed_children(self, children):
        if children.return_hanger() > 1:
            children.eating()


class Children:
    condition_dict = {0: 'спокоен', 1: 'слегка возбуждён', 2: 'капризный', 3: 'плачет', 4: 'истерика'}
    hunger_dict = {0: 'только поел', 1: 'слегка голоден', 2: 'голоден', 3: 'очень голоден'}
    def __init__(self, name, age, gender, condition = 0, hunger = 0):
        self.name = name
        self.age = age
        self.gender = gender
        self.condition = condition
        self.hunger = hunger

    def eating(self):
        self.hunger = 0

    def calm_down(self):
        self.condition = 0

    def return_condition(self):
        return self.condition

    def return_hanger(self):
        return self.hunger