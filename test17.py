# 输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

import string
inp = input('输入一行字符：')

letters = 0
space = 0
digit = 0
others = 0

i = 0
while i < len(inp):
    c = inp[i]
    i+=1
    if c.isalpha():
        letters+=1
    elif c.isspace():
        space+=1
    elif c.isdigit():
        digit+=1
    else:
        others+=1
print('char = {0} ,space = {1} ,digit = {2},others = {3}'.format(letters,space,digit,others))