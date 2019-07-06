"""python metaclass
元类是类的类。类定义了类的实例（对象）。类是元类的实例。
"""

a = 1
print(type(a)) 
print(type(type))  # type就是一个元类。type本身就是一个类

def make_hook(f):
    f.is_hook = 1
    return f

class MyType(type):
    def __new__(mcls, name, bases, attrs):

        if name.startwith('None'):
            return None
        
        newattrs = {}

        for attrname, attrvalue in attrs.iteritems():
            if getattr(attrvalue, 'is_hook', 0):
                newattrs['__%s__' % attrname] = attrvalue
            else:
                newattrs[attrname] = attrvalue
        
        return super(MyType, mcls).__new__(mcls, name, bases, newattrs)
    
    def __init__(self, name, bases, attrs):
        super(MyType, self).__init__(name, bases, attrs)

        print("Would register class %s now." % self)

    def __add__(self, other):
        class AutoClass(self, other):
            pass
        
        return AutoClass
    
    def unregister(self):
        print("Would unregister class %s now." % self)


class MyObject:
    __metaclass__ = MyType


class NoneSample(MyObject):
    pass


print(type(NoneSample), repr(NoneSample))

class Example(MyObject):
    def __int__(self, value):
        self.value = value
    
    @make_hook
    def add(self, other):
        return self.__class__(self.value + other.value)

Example.unregister()

inst = Example(10)

print(inst + inst)