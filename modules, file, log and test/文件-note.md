# 文件
- 长久保持信息的一种数据集合
- 常用操作
    - 打开关闭（文件一旦打开就必须关闭）
    - 读写
    - 查找


## 打开特定位置的文件
        
        file_path = 'C:\Users\Ramon\Evernote\Dict\user.dic'
        with open(file_path) as f:
        ...
    
## open函数
- open 函数负责打开文件，带有很多参数
    - 第一个参数：必须有，文件的路径和名称
    - mode：表明文件的打开方式
        - r:以只读方式打开
        - w:写方式打开，会覆盖以前的内容。如果没有会创建一个。
        - x:创建方式打开，如果文件已经存在，报错
        - a:append方式，以追加的方式对文件内容进行写入
        - b:binary方式，二进制方式写入
        - t：文本方式打开
        - +r：可读写
        
## with语句
- with语句使用的技术是一种称为上下管理协议的技术（contextManagementProtocol)
- 自动判断文件的作用域，自动关闭不再使用的打开的文件句柄。
        
        with open('file_name', 'r') as f:
            content = f.read()
            print(content)
            
## 按行读取 readline
        
        content_line = f.readline() # 把每行作为一个元素储存在一个列表中
        while content_line:#使用循环语句读取所有行
            print(content_line,end='')
            content_line = f.readline()
## 按list打开:list能用打开的文件作为参数，把文件内每一行内容作为一个元素
        
        l = list(f)
        for line in l:
            print(line)
            
        #或者应该用更方便的方式
        for line in f:
            print(line)
            
## read():
- 按字符读取，允许输入参数决定读取几个字符
- 如果没有指定参数，从当前位置读取到结尾
- 否则从**当前位置**读取指定个数字符

# seek(offset, from)
- 移动文件的读取位置
- from的范围
    - 0：从文件的开头开始偏移
    - 1：从文件当前位置开始
    - 2：从文件末尾开始偏移
- 移动的单位是字节（byte），一个汉字由若干个字节构成

## tell 用来显示文件读写指针的当前位置
- tell返回的数字单位是byte

## 文件的写操作 write
- write（str）：把字符串写入文件
- writelines（str）：把字符串按行写入文件
- 区别：
    - write函数参数只能是字符串
    - writelines参数可以是字符串也可以list格式，元素之间无换行
    
## split() 方法：以空格和换行符将字符串拆分成多个部分，并将这些部分都储存到一个列表中    

# pickle-持久化：txt格式
- 把程序运行中的信息保存在磁盘上
- 反序列化：序列化的逆过程
- pickle.dump,pickle.load
- json与pickle相似，json格式

# shelve-持久化：db文件
- 类似字典，用kv对保存数据，存取方式跟字典也类似
- open，close必须成对出现
- 不止创建一个文件，还包括其它文件
- 特点：
    - 不支持多个应用并行写入：为了解决这个问题，open的时候可以使用flag=r
    - 写回问题：使用writeback=True强制写回，当改变文件的值时，将改变保存在文件中。