from abc import ABC, abstractmethod


class AbstractParent(ABC):
    # дописати метод і реалізувати його в mother

    @abstractmethod
    def hello_friend(self):
        raise NotImplementedError

    @abstractmethod
    def one_additional_method_that_zveres_asked_to_add(self):
        print("I have added additional method to abstact class")


class Mother(AbstractParent, ABC):

    def one_additional_method_that_zveres_asked_to_add(self):
        print("This additional method is called from mother class ")

    def __init__(self, age):
        self.age = age
        print("mother constructor")

    @staticmethod
    def do_work():
        print("I'm working")

    def do_housework(self):
        print("listening music")


class Father(AbstractParent, ABC):
    def play_guitar(self):
        print("father is playing guitar")

    def __init__(self):
        print("father constructor")

    def do_housework(self):
        print("sitting on the sofa and fdrink beer")


class Daughter(Mother, Father):
    def __init__(self, age = 0):
        Father.__init__(self)
        Mother.__init__(self, age=age)

    @staticmethod
    def do_work():
        print("I'm working like a horse")

    def hello_friend(self):
            print("daughter say hello")


class Friend:
    pass


def greet_mother(mother : Mother):
    print("hello mother!!!!!!")
    mother.do_work()


def greet_father(father : Father):
    print("time for beer!!!!!!")
    father.play_guitar()


if __name__ == '__main__':
    daughter = Daughter()
    # mother.do_work()

    # change object class
    # daughter.__class__ = Friend

    greet_mother(daughter)
    greet_father(daughter)
    daughter.hello_friend()
    daughter.do_housework()

    for x in [daughter]:
        x.do_housework()

    # list
    povtorka_list = ["mathan_2", "pragramach_2", "superprise"]

    # tuple
    vasian = ("11 years", 12, 3.14, daughter)

    # set (тільки унікальні)
    my_set = {23, 11, 10, "call"}

    # frozen set
    another_set = frozenset(["di_", "mi", "do"])

    # dictionary
    my_dict = {1: "first", "2": 123, (1, 2, 3): "tuple_as_a_key"}
