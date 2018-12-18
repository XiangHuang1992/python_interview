"""变态台阶问题
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法？

分析：
f(1) = 1
f(2) = f(2-1) + f(2-2)
f(3) = f(3-1) + f(3-2) + f(3-3)
......
f(n-1) = f(n-2) + f(n-3) + ... + f(0)
f(n) = f(n-1) + f(n-2) + ... + f(0)
两式相减得： f(n) - f(n-1) = f(n-1) 即： f(n) = 2*f(n-1)
"""
# 采用递归方式解决问题，效率较低
def fib(n):
    if n < 2:
        return n
    else:
        return 2*fib(n-1)

print(fib(5))

# 使用lambda表达式，效率较低

fib2 = lambda n: n  if n <2 else 2*fib2(n-1)

print(fib2(5))


# 使用位移进行操作

def fib3(n):
    if n < 2:
        return n
    else:
        return 1<<(n-1)

print(fib3(5))

# 使用循环

def fib4(n):
    a, b = 1, 2
    for _ in range(n):
        a, b = b, 2*a

    return b
print(fib4(5))

# 使用数学归纳
def fib5(n):
    if n <= 0:
        return 0
    else:
        return 2**(n-1)

print(fib5(5))