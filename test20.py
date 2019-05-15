# 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？


h = 100
l=0
def num(n):
    global l,h
    for i in range(1,n+1):
        l += 1.5*h
        h /=2
    print(h,l)

num(10)
