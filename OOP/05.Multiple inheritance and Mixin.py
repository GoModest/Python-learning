#多继承的简单例子
class A1():
    def ap(self):
        print("我是A1")

class A2():
    def ap(self):
        print("我是A2")

class A3():
    def ap(self):
        print("我是A3")

class A_son(A1,A2,A3):
    pass

a = A_son()
a.ap()
print(A_son.__mro__)

#Mixin
#即将不同的功能方法分开在不同的类中，然后子类就可以继承多个父类来实现多个方法
class Look():#父类1
    def look(self):
        print("会看",end="")
        return

class Listen(): #父类2
    def listen(self):
        print("会听",end="")
        return

class Say(): #父类3
    def say(self):
        print("会说话",end="")
        return

class Swim(): #父类4
    def swim(self):
        print("会游泳",end="")
        return

class Human(Look,Listen,Say,Swim): #子类1
    pass

class Monkey(Look,Listen): #子类2
    pass

class Fish(Look,Listen,Swim): #子类3
    pass

human = Human()
monkey = Monkey()
fish = Fish()

print("人",end="")
human.listen()
human.look()
human.say()
human.swim()
print('\n'+"*"*20)
print("猴子",end="")
monkey.look()
monkey.listen()
print('\n'+"*"*20)
print("鱼",end="")
fish.listen()
fish.look()
fish.swim()
print('\n'+"*"*20)

print(dir(human))