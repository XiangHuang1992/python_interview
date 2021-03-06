"""
一个台阶总共有n级，如果一次可以跳1级，也可以跳2级。求总共有多少总跳法，并分析算法的时间复杂度。
"""
"""
分析：
1. 首先来考虑最简单的情况。如果说只有1级台阶，那么显然只有一种跳法。如果有两级台阶，那么则有两种跳法。
2. 现在来考虑一般情况。把n级台阶的跳法看成是n的函数，记为f(n)
"""


# 使用递归，效率比较低
def Selution(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    else:
        return Selution(n-1)+Selution(n-2)


# 使用lambda表达式，实际上也是递归，效率较低，比普通函数效率高一些
#print(Selution(5))
fib = lambda n: n if n<=2 else fib(n-1) + fib(n-2)

#print(fib(5))

# 使用循环代替递归，比上面低方法时间效率有来较大的提升
def fib2(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return b

print(fib2(5))

# 使用位移操作,该方式效率最高
def fib3(n):
    if n <= 2:
        return n
    else:
        return 1<<(n-2)
print (fib3(5))

def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap

@memo
def fib4(n):
    if n<2:
        return 1
    else:
        return fib4(n-1) + fib4(n-2)

print(fib4(5))

if __name__ == '__main__':
    from timeit import Timer
    t1 = Timer("Selution(10)", "from __main__ import Selution")
    t2 = Timer("fib(10)", "from __main__ import fib")
    t3 = Timer("fib2(10)", "from __main__ import fib2")
    t4 = Timer("fib3(10)", "from __main__ import fib3")
    t5 = Timer("fib4(10)", "from __main__ import fib4")

    print(t1.timeit(1000000)) 
    print(t2.timeit(1000000)) 
    print(t3.timeit(1000000))
    print(t4.timeit(1000000))
    print(t5.timeit(1000000))
    """时间效率测试结果如下
    在n为10的情况下
    20.047603069106117
    18.299409351078793
    0.9879354480654001
    0.2027504441794008
    0.26944803493097425
    """
