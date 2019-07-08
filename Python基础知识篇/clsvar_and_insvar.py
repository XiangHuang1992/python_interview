# _*_ coding: utf-8 _*_
"""
# Created on 七月-08-19 16:31
# @version: v0.1
# @filename: clsvar_and_insvar.py
# @author: ferdinand
"""

__author__ = "huangxiang"

"""类变量和实例变量
类变量：可在类的所有实例之间共享的值（也就是说，它们不是单独分配给实例的）。
实例变量：每个实例单独拥有的变量。
"""


class Test:
    num_of_instance = 0

    def __init__(self, name):
        self.name = name
        Test.num_of_instance += 1


if __name__ == "__main__":
    print(Test.num_of_instance)  # 0
    t1 = Test("huangxiang")
    print(Test.num_of_instance)  # 1
    t2 = Test("hujinli")
    print(t1.name, t1.num_of_instance)  # huangxiang 2
    print(t2.name, t2.num_of_instance)  # hujinli 2


"""python自省
自省就是面向对象的语言所写的程序在运行时，所能知道的对象的类型。简单一句就是运行时能获得对象的类型。比如type(),dir(),hasattr(),isinstance()
"""

a = [1, 2, 3]
b = {"a": 1, "b": 2, "c": 3}
c = True
print(type(a), type(b), type(c))  # <class 'list'> <class 'dict'> <class 'bool'>
print(isinstance(a, list))  # True


"""Python中单下划线和双下划线
__foo__: 一种约定，python内部的名字，用来区别其他用户自定义的命名，以防冲突。
_foo:一种约定，用来制定变量私有，程序员用来制定私有变量的一种方式。不能用from moudle import导入，
其它方面和共有变量一样访问。python并没有真正的私有化，使用这样的方式，就是向使用者说明，该变量或者方法，你不应该尝试去直接去使用它。

__foo:这个有真正的意义，解析器用_classname__foo来代替这个名字，以区别和其他类相同的命名，它无法像公有成员一样直接访问，通过.类名__xxx的方式访问。
"""
