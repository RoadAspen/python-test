# 暂停一秒输出。

# 使用time 的 sleep 函数
import time

myD = {1: 'a', 2: 'b'}
for key, value in dict.items(myD):
    print(key, value)
    time.sleep(1)  # 暂停 1 秒
