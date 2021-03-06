# 函数式编程（FunctionalProgramming)
- 基于lambda演算的一种编程方式
    - 程序中只有函数
    - 函数可以作为参数，同样可以作为返回值
    - 纯函数式编程语言：LISP，Hsskell
- Python函数式编程知识借鉴函数式编程语言的一些特点，可以理解成一半函数式一半Python
- 内容：
    - 高阶函数
    - 返回函数
    - 匿名函数
    - 装饰器
    - 偏函数
    
## lambda表达式
- 函数可以最大程度复用代码，但是
    - 如果函数很小就会很啰嗦
    - 如果函数被调用次数少，则会造成浪费
    - 对于阅读者来说会打断思路
- lambda表达式（匿名函数）：
    - 一个表达式，函数体相对简单
    - 不是一个代码块，仅仅是一个表达式
    - 可以有参数，有多个参数也可以，用逗号隔开
- 语法：

        stm = lambda x,y,z: x+y+z
        # 其中xyz是三个参数，冒号后面是运算方式
        print(stm(1,2,3))  # 结果是1+2+3，即6
        
## 高级函数
- 把函数作为参数使用的函数，叫高阶函数
    - 函数的名称就是一个变量
    - 所以函数就可以作为一个参数传递给函数
- 系统高阶函数：map
    - 原意就是映射，即把集合或者列表中的元素，每个元素都按照一定规则进行操作，生成一个新的列表或者集合
    - map函数是喜用提供的具有映射功能的函数，返回值是一个迭代对象
    - 使用：

            l1 = range(10)  # 一个列表
            f = lambda n : n * 10  # 一个函数，返回  参数乘以10 的结果
    
            l2 = map(f,l1)  # 调用map把列表l1中的所有值乘以10，这里的l2是map类型不是list
            for i in l2:  # map类型可迭代，遍历l2获取其中的值
                print(i)
            
- 系统高阶函数：reduce
    - 原意是归并，缩减
    - 把一个可迭代的对性爱观念最后归并成一个结果
    - 对于作为参数的函数要求：必须有两个参数，必须有返回结果
    - 需要导入functools包
    - 使用：
            
            from functools import reduce  # 导入reduce
            def myAdd(x,y):
                return x+y  # 一个函数，两个参数并且有返回值
            rst = reduce(myAdd, [1,2,3,4,5,6])  # 使用reduce，得到一个列表中所有值的和
            print(rst)
    
