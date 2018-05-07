"""
单例模式是一种常用的软件设计模式。该模式的主要目的是确保某一个类只有一个实例存在，当你希望在整个系统中，
某一个类只能出现一个实例的时候，单例对象就能派上用场。

在Python中，可以通过以下方式来实现单例模式。
"""

# 使用模块来实现单例模式
"""
Python的模块就是天然的单例模式，因为模块在第一次导入时，会生成pyc文件，当第二次导入的时候，会直接加载pyc文件，
而不会再执行模块代码。我们只需要把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。
"""

# mysingleton.py
class My_Singleton():
    def foo(self):
        pass

my_sigleton = My_Singleton()

# 在其他模块中调用
#from mysingleton import my_sigleton
#my_sigleton.foo()


#**********************************************************************************************

# 使用__new__
# 为了使类只能出现一个实例，我们可以使用__new__来控制实例的创建过程

class Singleton():
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        rerurn cls._instance

class MyClass(Singleton):
    a = 1


#**********************************************************************************************

# 使用装饰器
# 装饰器可以动态的修改一个类或函数的功能。我们可以使用装饰器来装饰某个类，使其只能生成一个类实例。

from functools import wraps

def singleton(cls):
    instances = {}
    @wraps(cls)
    def getInstance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return getInstance

@singleton
class MyClass():
    a = 1



#************************************************************************************************
# 使用元类metaclass
"""
元类可以控制类的创建过程，它主要做三件事情：
1. 拦截类的创建
2. 修改类的定义
3. 返回修改后的类
"""
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

# Python2
class MyClass(object):
    __metaclass__ = Singleton

# python3
class MyClass(metaclass=Singleton):
    pass
