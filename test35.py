# 文本颜色设置。


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# print(123)

# 装饰器
def document_func(func):
    def new_func(*arg):
        print(func.__name__)
        print(func.__doc__)
        return func(*arg)
    return new_func


@document_func
def doud(*arg):
    print(arg)

# new_doud = document_func(doud)

 
doud(1, 2, 3, 4)
