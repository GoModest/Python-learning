import random

print(random.random())  # 生成一个0-1之间的随机小数


# choice方法可以从一个序列中随机选择一个值，并返回这个值
l = [str(i)+"ming" for i in range(10)]
ras = random.choice(l)
print(ras)

random.shuffle(l)  # 把一个列表顺序打乱，原地打乱，return None
print(l)

print(random.randint(0,100))  # 返回一个[a,b]的整数
