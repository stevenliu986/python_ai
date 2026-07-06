"""
迭代器：
    迭代器协议：
    1. 能被 __iter__ 接受
    2. 能被 __next__ 一步步取值
"""

class Person:
    def __init__(self, name,age,gender,address):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address

    def __iter__(self):
        return PersonIterator(self)

class PersonIterator:
    def __init__(self, person):
        # 将外部传进来的数据保存好
        self.person = person
        # 设置迭代器的初始状态
        self.index = 0
        # 配置好要遍历的内容
        self.attrs = [person.name,person.age, person.gender,person.address]

    # 迭代器的 __iter__ 方法会返回自身
    def __iter__(self):
        return self

    # 每次调用 __next__ 会根据当前的状态返回下一个元素
    def __next__(self):
        # 如果指针的位置超出范围，就抛出StopIteration异常
        if self.index >= len(self.attrs):
            raise StopIteration
        # 获取要返回的内容
        value = self.attrs[self.index]
        # 更新迭代器的位置(指针位置)
        self.index += 1
        # 返回 value
        return value

p1 = Person('John',18, 'male', 'NSW')
for item in p1:
    print(item)

# 方法二
class People:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.__index = 0
        self.__attrs = [name,age,gender]

    def __iter__(self):
        self.__index = 0
        return self

    def __next__(self):
        if self.__index >= len(self.__attrs):
            raise StopIteration
        value = self.__attrs[self.__index]
        self.__index += 1
        return value

p2 = People('Tom', 34, 'male')
for item in p2:
    print(item)