import time

print(time.timezone)  # 当前时区和UTC时间相差的秒数
print(time.altzone)  # 在有夏令时的情况下与UTC时间相差的秒数
print(time.time())  # 时间戳，返回的是时间元组
print(time.localtime())  # 返回当前时间
print(time.localtime().tm_hour)  # 返回当前时间的小时

t = time.localtime()
tt = time.asctime(t)
print(tt)  # 显示当前时间的正常字符串化之后的时间格式

print(time.ctime())  # 直接获取当前时间的字符串格式
print(time.mktime(time.localtime()))  # 返回时间戳，是time.time的反向

t1 = time.clock()  # t1是CUP时间
for i  in range(10):
    print(i)
    time.sleep(0.2)  # 程序休眠0.2秒
t2 = time.clock()  # t2是程序运行结束后的CUP时间
print(t2-t1)  # 用来计算程序运行快慢

# 字符串格式化
ft = time.strftime("%Y-%m-%d %H:%M",t)  # 将时间戳格式化为某种形式，中间有中文会出现问题
print(ft)
