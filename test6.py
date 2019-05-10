# 斐波那契数列
# 斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

# 第一种方法
def fib(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return a

print(fib(10))

# 第二种方法，递归

def fin(n):
    if n==1 or n ==2:
        return 1
    return fin(n-1)+fin(n-2)

print(fin(10))
