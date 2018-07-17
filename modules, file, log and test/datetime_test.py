import datetime
import time

print(datetime.date(2017,12,3))  # 返回一个理想的日期
print(datetime.date(2018,1,3).year)  # 日期的年份
print(datetime.time(17,26,23))  #返回一个理想的时间
print(datetime.datetime(2018,12,12,12,12,12))  # 返回一个理想的日期+时间
print(datetime.timedelta(days=1))  # 一个时间差，可以与其它时间进行运算

from datetime import datetime  # 导入datetime里面的datetime类
print(datetime(2018,12,3))  # 返回一个理想的日期
print(datetime.utcnow())  # 返回UTC标准日期时间
print(datetime.now())  # 返回当前日期时间
print(datetime.today())  # 返回今天的日期时间
print(datetime.fromtimestamp(time.time()))  # 返回一个时间戳对应的日期时间

import timeit

code_one = '''
sum = []
for i in range(100):
    sum.append(i)
'''
s='''
def code_two(num):
    sum = []
    for i in range(num):
        sum.append(i)
'''
t1 = timeit.timeit(stmt='[i for i in range(100)]',number=10000)
t2 = timeit.timeit(stmt=code_one,number=10000)
t3 = timeit.timeit(stmt=s,setup=s+"num=100",number=10000)
print(t1,t2,t3)

# 上面的内容作用是对比两段代码的运行速度
# 其中stmt是代码块，number是执行次数
# stmt也可以是一个函数，如果函数存在参数，需要加上 setup来设置环境