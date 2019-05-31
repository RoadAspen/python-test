# 创建一个类

class Animal():
    
    def __init__(self,weight):
        self.weight = weight

    def drink(self):
        print('xiaomao yao chi yu')
dog = Animal(80)

print(dog.weight)

dog.drink()

print(id(dog))