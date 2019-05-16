# 一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
a = int(input('输入一个五位数：'))
x = str(a)
l = len(x)
flag = True
for i in range(l//2):
    if x[i] != x[-i-1]:
        flag = False
if flag:
    print('%10s是回文数' % (a))
else:
    print('%20s不是回文数' % (a))

