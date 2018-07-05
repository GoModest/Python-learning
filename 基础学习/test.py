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
魔术方法实例
'''
