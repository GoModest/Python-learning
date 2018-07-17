import os

print(os.getcwd())  # 获取当前的工作目录
os.chdir(r'C:\Users\Ramon\PycharmProjects\Python')  # 更改工作路径
dl = os.listdir(r'C:\Users\Ramon\PycharmProjects\Python')  # 返回一个目录中所有子目录和文件的名称列表
print(dl)

print('*'*20)

#os.makedirs(r'c:/xinjian')  # 新建文件夹
#os.remove(r'd:/123')  # 删除文件

print('*'*20)

os.system('dir')  # 运行系统shell命令，返回：打开一个终端页面内容
get = os.getenv("PATH")
print(get)  # 获取指定系统的环境变量值
#exit()  #退出当前程序

print("--"*20)

print(os.curdir)  # 操作系统用于引用当前目录的常量字符串
print(os.getcwd())
print(os.pardir)  # 作系统用于引用父亲目录的常量字符串
print(os.getcwd())
print(os.sep)  # 当期那系统的路径分隔符
print(os.linesep)  # 当前系统的换行符号（windows:"\r\n",linux:"\n"）
print(os.name)  # 当前系统名称