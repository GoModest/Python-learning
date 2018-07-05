#构造函数

class Animal():
    def __init__(self):
        print("Animal")
    pass

class Mammal(Animal):
    def __init__(self):
        print("mammal")
    pass

class Dog (mammal):
    #__init__就是构造函数
    #每次实例化的时候，第一个被调用
    #因为主要工作是进行初始化
    def __init__(self):
        print("I am init in Dog")

class Cat(mammal):
    pass


big_yellow = Dog()
# big_yellow 是Dog的对象实例化，其中有一个构造函数，就不向上查找
small_cat = Cat()
# small_cat 是Cat的对象实例化，但是其中没有构造函数，向上查找到Mammal中有一个构造函数，调用。
#如果构造函数中需要传入参数，则实例化对象中也要传入参数