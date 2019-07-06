"""python的函数参数传递
在pythpn中，对象有可变对象和不可变对象，可变对象：list，dict，set。不可变对象：string，tuples，numbers

当一个引用传递给函数的时候，函数自动复制一份引用，这个函数里的引用和外边的引用没有关系。
所以，当把引用指向了一个不可变对象，在函数返回的时候，外面的值不会改变。

当引用指向了一个可变对象，对它的操作就跟定位了指针地址一样，在内存中进行了修改，所以，外部同样发生改变。
"""

# numbers是不可变类型
a = 1

def fun(a):
    print("func_in", id(a))  # func_in 4562129696
    a = 2
    print("re-point", id(a), id(2)) # re-point 4562129728 4562129728

print("func_out", id(a), id(1)) # func_out 4562129696 4562129696

fun(a)
print(a) # 1


# python中，list是可变类型
b = []

def fun(b):
    print("func_in", id(b)) # func_in 4391024008
    b.append(1)

print("func_out", id(b)) # func_out 4391024008
fun(b)
print(b)  # [1]


# 字符串是不可变类型
# 它是不可变的,所以，无法改变字符串的内容
c = 'huangxiang'

def fun(c):
    print("func_in", id(c))
    c = 'xiang'

fun(c)
print(c)

def try_to_change_string_reference(the_string):
    print('got', the_string) # got It was many and many a year ago 
    the_string = 'In a kingdom by the sea'
    print('set to', the_string) # set to In a kingdom by the sea

outer_string = 'It was many and many a year ago '

print('before, outer_string =', outer_string) # before, outer_string = It was many and many a year ago 
try_to_change_string_reference(outer_string)
print('after, outer_string = ', outer_string) # after, outer_string =  It was many and many a year ago 


def try_to_change_list_contents(the_list):
    print('got', the_list) # got ['one', 'two', 'three']
    the_list.append('four') # 使用list的方法改变list的值，并且外部同样生效
    print('change to', the_list) # change to ['one', 'two', 'three', 'four']

outer_list = ['one', 'two', 'three']

print('before, outer_list = ', outer_list)  # before, outer_list =  ['one', 'two', 'three']
try_to_change_list_contents(outer_list) 
print('after, outer_list = ', outer_list) #  after, outer_list =  ['one', 'two', 'three', 'four']

"""参数传递通过值传递
1. 传入的参数实际上是对象的引用
2. 一些数据类型是可变的，一些数据类型是不可变的

将一个可变对象传递给一个方法，这个方法会获得对同一个对象的引用，我们可以改变它的值。但是如果我们把它重新引用另外一个对象，外部将无法感知，完成操作之后，外部对象仍然指向原始对象。所以我们可以看到下面的the_list的值没有改变。
"""
def try_to_change_list_reference(the_list):
    print('got', the_list) # got ['we', 'like', 'proper', 'english']
    the_list = ['and', 'we', 'can', 'not', 'lie'] # 重新指向了另一个引用
    print('set to', the_list) # set to ['and', 'we', 'can', 'not', 'lie']

outer_list2 = ['we', 'like', 'proper', 'english']

print('before, outer_list2 = ', outer_list2) # before, outer_list2 =  ['we', 'like', 'proper', 'english']
try_to_change_list_reference(outer_list2)
print('after, outer_list2 = ', outer_list2) # after, outer_list2 =  ['we', 'like', 'proper', 'english']