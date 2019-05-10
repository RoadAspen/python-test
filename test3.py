# 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？

# 分析
# 1.假设 一个x ，如果 x + 100 = n² ， x + 100 + 168 = m²， 求 x.
# 2. m²-n² = 168 = （m+n）（m-n）.
# 3. 设置 m+n = i, m-n = j. i*j = 168  .  m = (i+j)/2. n = (i-j)/2. 所以 i 和 j 同是偶数或者同是奇数。
# 4. i>=2 ,所以 1<j<(168/2)+1 = 85

for i in range(1, 85, 1):
    if 168 % i == 0:
        j = 168/i
        if i > j and (i+j) % 2 == 0 and (i-j) % 2 == 0:
            m = (i+j)/2
            n = (i-j)/2
            x = n*n-100
            print(x)