# 利用递归方法求5!。

def num(n):
    if n == 1:
        return n
    else:
        return n*num(n-1)

print(num(5))