# 输入三个整数x, y, z，请把这三个数由小到大输出。

# 问题分析： 排序。输出一个排序过后的列表。

# 第一种方法
x = int(input('第一个整数：'))
y = int(input('第二个整数：'))
z = int(input('第三个整数：'))

l = [x,y,z]
l.sort()

print(l)


#第二种方法
k = []
for i in range(0,3,1):
    g = int(input('输入一个值：'))
    k.append(g)
k.sort()

print(k)