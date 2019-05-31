# 练习函数调用。


def hello_world():
    print('hello world')


def three():
    for i in range(3):
        hello_world()


three()
