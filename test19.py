# 一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数
from functools import reduce


def add(x, y):
    return x+y


def reduceNum(n):
    num = n
    asd = []
    for index in range(1, int(n)):
        if n % index == 0:
            asd.append(int(index))
            continue
    if reduce(add, asd) == num:
        print(num)


for count in range(2, 1001):
    reduceNum(count)

