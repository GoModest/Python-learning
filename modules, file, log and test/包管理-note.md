# 模块
# 1. 模块基本概念
- 一个模块就是一个包含python代码的文件，后缀是 .py 
- 为什么要用模块
    - 程序太大，编写维护非常不方便，需要拆分
    - 模块可以增加代码重复利用的方式
    - 当做明明空间使用，避免命名冲突
- 模块的规范，最好在模块中编写以下内容
    - 函数（单一功能）
    - 类（相似功能的组合，或者类似业务模块）
    - 测试代码
- 使用模块，import时相当于复制粘贴
    - 假如模块名称直接以数字开头，需要借助importlib
    - 语法 
       `import module_name`
        `module_name.funciton_name`
        `module_name.class_name`
    
    - import模块可以用 as起一个别名
        - 导入的同时给模块起一个别名
        - 其余用法不变
        - `import abc as p`
    - 导入模块的一部分: `from module_name import func_name`,`from module_name import class_name`
    - 导入模块中的所有内容：`from module_name import *`
- 使用 `if __name__ == '__main__':`
    - 可以有效避免模块代码被导入的时候被动执行的问题
    - 建议所有程序的入口都以此代码为入口

# 2.模块的搜索路径和储存
- 模块的搜索路径：加载模块的时候，系统会在哪些地方寻找此模块
- 系统默认的模块搜索路径
    
        import sys
        sys.path
- 添加搜索路径

        sys.path.append(dir)
- 模块的加载顺序
    1. 搜索内存中已经加载好的模块
    2. 搜索python的内置模块
    3. 搜索sys.path路径
    
    
    
# 包
- 包是一个组织管理代码的方法，包里面存放的是模块
- 用于将模块包含在一起的文件夹就是包
- 包中肯定有一个 `__init__.py`文件，包里面可以有子包，子包里面也必须有`__init__.py`文件
- 包的导入操作
    - import package_name
        - 直接导入一个包，只有`__init__.py`中的内容
        - 使用方法是:
            
                package_name.func_name
                package_name.class_name.func_name()
    
    - import package_name.module_name
        - 导入包中某一个具体的模块，不包括`__init__.py`
    - from ... import ...
        - 和上面的用处相同
    - from package import *
        - 导入当前包 `__init__.py`文件中所有的函数和类
    - from package.module import *
        - 导入包中指定模块的所有内容
    - 在开发环境中经常会使用其它模块，可以在当前包中直接导入其它模块中的内容
        - import 完整的包或者模块的路径
- `__all__`的使用
    - 管理在使用`from package import *`的时候，可以导入的内容
    - 如果`__init__.py`中没有`__all`，那么就直接导入其中所有内容
    - 如果有`__call__`，那么就只导入它指定的内容,而不载入`__init__.py`的内容
        - `__all__ = ['module1','class1','package1'...]`