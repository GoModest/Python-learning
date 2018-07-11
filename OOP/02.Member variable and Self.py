#只有在对象中改变成员变量的值后，才改变成员变量的id
#首先定义一个类，这个类里面有name和age两个参数
class Student():
    name = "ming"
    age = 19

print(Student.__dict__) #打印出Student这个类里面的所有参数和方法

one = Student() #对象的实例化，但one里面没有赋值


print(one.__dict__)#打印出one这个对象实例化的所有参数和方法
print(Student.name)
print(id(one.age),id(Student.age))#检测对象实例化和类实例化的id是否相同

one.age = 22 #给对象one的参数age赋值

print(one.__dict__)
print(one.age)
print(id(one.age),id(Student.age))#赋值之后再检测对象实例化和类实例化的id是否相同

print("*"*20)

#self的作用---还没有完全理解

class Teacher ():
    name = "dana"
    age = 23

    def say(self):
        self.name = "yaona"
        self.age = 19
        print("Hello,my name is {}.".format(self.name))
        print("I am {} years old.".format(self.age))

    #如果没有self，说明这个函数是绑定类的，即只有类里面有这个函数
    def sayAgain():
        print(__class__.name)
        print(__class__.age) #这两行想要在绑定类的方法内部访问该类的成员
        print("Hello,nice to see you again.")


class Teacher2():
    name21 = "xiao"
    age23 = 22


t = Teacher()
t.say()
Teacher.sayAgain() #而不能是 t.sayAgagin()

print("*"*20)
Teacher.say(Teacher2)  #这样也可以，这叫做鸭子模型，但这部分还需要再查资料理解一下
