#抽象类的实现

import abc

class Dog(metaclass=abc.ABCMeta):
    #定义一个抽象方法
    @abc.abstractmethod
    def bark(self):
        pass

    @abc.abstractclassmethod #在python3.3之后不推荐有抽象类方法
    def run(cls):
        pass

    @abc.abstractstaticmethod #在python3.3之后不推荐有抽象静态方法
    def eat():
        pass

class Corgi(Dog):

#只有抽象类的三个抽象方法全都实现后才能进行实例化
    def bark(self):
        print("汪汪汪")

    def run(cls):
        print("gogogo")
    def eat():
        print("miamiamia")


dou_dou = Corgi()
dou_dou.bark()
