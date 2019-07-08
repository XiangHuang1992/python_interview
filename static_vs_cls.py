# _*_ coding: utf-8 _*_
"""
# Created on 七月-08-19 11:22
# @version: v0.1
# @filename: static_vs_cls.py
# @author: ferdinand
"""

__author__ = "huangxiang"


class A:
    def foo(self, x):
        print("executing foo(%s, %s)" % (self, x))

    @classmethod
    def class_foo(cls, x):
        print("executing class_foo(%s, %s)" % (cls, x))

    @staticmethod
    def static_foo(x):
        print("executing static_foo(%s)" % x)


a = A()

a.foo(1)  # executing foo(<__main__.A object at 0x10fdb5eb8>, 1)

a.class_foo(1)  # executing class_foo(<class '__main__.A'>, 1)

a.static_foo(1)  # executing static_foo(1)

print(a.foo)  # <bound method A.foo of <__main__.A object at 0x10d373eb8>>

print(a.class_foo)  # <bound method A.class_foo of <class '__main__.A'>>

print(a.static_foo)  # <function A.static_foo at 0x10e70fd08>


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f"Pizza({self.ingredients})"

    @classmethod
    def margherita(cls):
        return cls(["mozzarella", "tomatoes"])

    @classmethod
    def prosciutto(cls):
        return cls(["mozzarella", "tomatoes", "ham"])


print(Pizza.margherita())
print(Pizza.prosciutto())
