"""python的函数参数传递
"""

a = 1

def fun(a):
    print("func_in", id(a))  # func_in 4562129696
    a = 2
    print("re-point", id(a), id(2)) # re-point 4562129728 4562129728

print("func_out", id(a), id(1)) # func_out 4562129696 4562129696

fun(a)
print(a) # 1


b = []

def fun(b):
    print("func_in", id(b)) # func_in 4391024008
    b.append(1)

print("func_out", id(b)) # func_out 4391024008
fun(b)
print(b)  # [1]

