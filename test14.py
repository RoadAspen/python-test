# 将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。


def reduceNum(n):
    asd = [1]
    if isinstance(n, int) == False or n <= 0:  # 先判断n 是不是整数还是负数
        print('请输入一个正整数')
        exit(0)
    elif n in [1]:
        print('{}'.format(n))
    else:
        while n not in [1]:  # 循环保证递归
            for index in range(2, int(n+1)):
                if n % index == 0:
                    n /= index
                    asd.append(int(index))
                    if n == 1:
                        print(index)
                    else:
                        print('{}*'.format(index))
                    break
        print(asd)


reduceNum(100)
