# 输入某年某月某日，判断这一天是这一年的第几天？
# 以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：

# 程序源代码：

year = int(input('年：\n'))
month = int(input('月：\n'))
day = int(input('日：\n'))
# 输入月份之前的天数
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

thO = [1, 3, 5, 7, 8, 10, 12]
thZ = [4, 6, 9, 11]

if 0 < month <= 12:
    sum = months[month-1]
    if month in thO:
        if 0 < day <= 31:
            sum += day
        else:
            print(month, '月没有', day, '号')
    elif month in thZ:
        if 0 < day <= 30:
            sum += day
        else:
            print(month, '月没有', day, '号')
    else:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if 0 < day <= 29:
                sum += day
            else:
                print(month, '月没有', day, '号')
        else:
            if 0 < day <= 28:
                sum += day
            else:
                print(month, '月没有', day, '号')
    
else:
    print('输入月份有误')

print(year,'年',month,'月',day,'日是这一年的第',sum,'天')
