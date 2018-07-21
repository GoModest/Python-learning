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

print("*"*20)

from os import path  # 导入path模块

print(path.abspath("."))  # 返回绝对路径
print(path.basename(r"modules, file, log and test\.idea\.name"))  # 获取路径中的文件名

bd = "modules, file, log and test\.idea"
fn = ".name"
p = path.join(bd,fn)  # 将多个路径合并成一个路径
print(p)

t = path.split(r"modules, file, log and test\.idea\.name")
print(t)
# 将路径切割为文件夹部分和文件部分

print(path.isdir(r"modules, file, log and test\.idea\.name"))
# 检测是否是目录

print(path.exists(r"modules, file, log and test\.idea\.name"))
# 检测文件或目录是否存在






import  shutil

rst = shutil.copy(r"download\123.txt", "456.txt")
print(rst)
# 把一个文件从一个路径拷贝到另外一个路径，拷贝的同时可以重命名
# 还有一个copy2方法，特点在于复制时可以尽量保留元数据

rst = shutil.copyfile(r"download\123.txt", "456.txt")
print(rst)
# 把一个文件的内容拷贝中另外一个文件中,覆盖拷贝

#shutil.move(r"download\123.txt",'.')  # 把一个文件移动到其它路径


"""归档和压缩"""
shutil.make_archive(r"download\压缩",'zip','download')
shutil.unpack_archive('download\压缩.zip','download')


"""zipfile模块使用"""
import zipfile

zf = zipfile.ZipFile(r'download\xxx.zip')  # 创建一个zipfile对象，表示一个zip文件
print(zf.getinfo("123.txt"))  # 返回某个zip对象中某个文件的信息
print(zf.namelist())  # 获取zipfile对象中所有文件的名称列表
zf.extractall()  # 解压zipfile中所有文件到某个目录