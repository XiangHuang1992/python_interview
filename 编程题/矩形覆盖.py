"""矩形覆盖问题
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
问题分析：
n=1, 时， f(1) = 1
n=2, f(2) = 2
n=3, f(3) = f(3-1) + f(3-2)
...
n=n-1, f(n-1) = f(n-2) + f(n-3) + ... + f(1)
n=n,   f(n)   = f(n-1) + f(n-2) + ... + f(1)

f(n) - f(n-1) = f(n-2)
f(n) = f(n-1) + f(n-2)  
"""

# 递归
def fib1(n):
    if n <=2:
        return n
    else:
        return fib1(n-1) + fib1(n-2)
# 使用装饰器减少调用
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def fib2(n):
    if n <=2:
        return n
    else:
        return fib2(n-1) + fib2(n-2)

# 使用循环
def fib3(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a+b
    return b

# 使用位移操作
def fib4(n):
    if n<=2:
        return n 
    else:
        return 1<<(n-2)

print(fib1(5))
print(fib2(5))
print(fib3(5))
print(fib4(5))