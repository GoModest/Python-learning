#私有

class Dog():
    color = "black"
    __bark = "wangwangwang"


big_yellow = Dog()
# print(big_yellow.bark) #bark是私有成员，不允许访问
print(big_yellow.color) #color是共有成员，可以访问

print(Dog.__dict__)

print(big_yellow._Dog__bark)
#👆通过__dict__找到这个被改了名的成员，强制访问。不建议。


print("*"*20)


#继承
class Person():
    name = "NoName"
    age = 0
    _live = "火"
    def sleep(self):
        print("sleepZZZZZZZzzzzz")

class Teacher(Person):
    name = "xiaowang"
    pass
    def sleep(self):
        super().sleep() #对于父类中sleep方法的扩充
        # Person.sleep #也可以对父类中方法进行扩充
        print("老师睡觉被骂") #子类的扩充内容

p = Person()
p.sleep()
print("--"*20)
t = Teacher()
print(t.name)#子类修改了父类中的成员值
t.sleep() #子类调用父类方法，是已扩充的方法
print(t._live) #子类可以调用父类中的 受保护成员



