# 从1-4之间 组合成多个不重复的三位数
for i in range(1,5,1):
    for j in range(1,5,1):
        for k in range(1,5,1):
            if(i!=k)and(i!=j)and(j!=k):
                print(i,j,k)