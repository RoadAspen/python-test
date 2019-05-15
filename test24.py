#有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
l = []
j = []
k = []
for i in range(0,20):
    if i == 0 or i==1:
        k.append(i+2)
        j.append(i+1)
    else :
        k.append(k[i-1]+j[i-1])
        j.append(k[i-1])
    l.append('%s/%s' % (k[i], j[i]))

print(l)
