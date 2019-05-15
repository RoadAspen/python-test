# 求1+2!+3!+...+20!的和。


def jiecheng(num):
    if isinstance(num, int):
        count = 1
        for i in range(1,num+1):
            count *= i
        return count
    else:
        print('请输入一个正整数')

all=0
for j in range(1,21):
   all +=jiecheng(j)
print(all) 