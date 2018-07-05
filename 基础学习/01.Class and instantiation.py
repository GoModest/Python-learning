'''
定义一个学生类，用来形容学生
'''

#定义一个空的类
class Student():
    pass
#此处pass必须有

#定义一个对象
mingming = Student()

#定义一个类，用来描述听python的类
class PythonStudent():
    #用None给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    #注意
    #def的层级
    #系统会默认给一个self参数
    def doHomework(self):
        print("我在做作业")
        return


#实例化
liujiao = PythonStudent()

print(liujiao.age)
print(liujiao.course)
liujiao.doHomework()