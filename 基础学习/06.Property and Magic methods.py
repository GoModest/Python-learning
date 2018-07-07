# property的使用


class Student():
    '''
    这是类的文档
    目的是为了让传入的age都是以整数形式显示
    '''
    def fget(self):
        return self._age
    def fset(self,age):
        self._age = int(age) #修改age为整数
        return

    age = property(fget,fset,"使用了property") #使用方法

ming = Student()
ming.name = "小明"
ming.age = 19.3

print(ming.age)

print("*"*20)

print(Student.__name__)
print(Student.__doc__)
print(Student.__bases__)
print(Student.__dict__)

'''
魔术方法实例-基本用法
'''
class Magic():

    def __init__(self):
        pass

    def __getattr__(self, item):
        print("没有成员{}".format(item))
        pass

    def __setattr__(self, key, value):
        super().__setattr__(key,value)

    def __gt__(self, other):
        return len(self) > len(other)

m1 = Magic()
m1.name = "张三" #对成员属性进行设置时调用
print(m1.name)
m2 = Magic()
m2.name = "赵四"
print(m1.name>m2.name) #成员比较时调用__gt__方法
print(m1.name2) #调用一个不存在的成员时调用__getattr__方法
