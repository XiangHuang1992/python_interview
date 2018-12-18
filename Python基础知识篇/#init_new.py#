# -*- coding: utf-8 -*-
"""
Python中__init__和__new__的区别
"""


class Person():
    """
    __init__最普通的用法，但__init__并不是实例化一个类是第一个被调用的方法，当使用Person(name, age)这样的表达式来实例化一个类时，最
    先调用的方法其实是__new__
    """
    """
    在Python3.6当中，__new__方法调用时，传递了除cls之外的参数都会报错。在python2.*中第一种定义方法是不会出问题的。
    所以我们应该明白__new__是用来生成实例，而__init__是用来初始化实例的。
    __new__通常用于控制一个生成实例的过程，它是一个类级别的方法。
    __init__通常用于初始化一个实例，控制这个初始化的过程，比如添加一些属性等。做一些额外的操作。发生在类实例被创建之后，它是实例级别的
    方法。

    __new__和__init__方法用来一起构造对象，__init__不可以返回非None的值，否则会引发TypeError异常。

    super(currentclass, cls).__new__(cls[, ...])调用超类的__new__方法创建类的一个新的实例。如果__new__返回cls的一个实例，那么__init__
    方法将以__init__(self[, ...])的方式调用，cls是新的实例，其他的参数和传递给__new__的一样。
    如果__new__返回的不是cls的实例，那么新实例的__init__方法将不会调用。
    """

    # def __new__(cls, name, age):
    # def __new__(cls, *args, **kwargs):
    def __new__(cls, name, age):
        print('__new__ called')
        # return super(Person, cls).__new__(cls, name, age)
        return super().__new__(cls)
        # return super(Person, cls).__new__(cls)

    def __init__(self, name, age):
        print('__init__ called')
        self.name = name
        self.age = age

    def __str__(self):
        return '<Person: %s(%s)>' % (self.name, self.age)

    """
    什么是__new__方法呢？？__new__方法虽然接受的参数和__init__一样，但__init__是在类实例创建之后调用。而__new__方法正是创建这个实例类
    的方法。
    """


if __name__ == '__main__':
    huangxiang = Person('Huangxiang', 26)
    print(huangxiang)
