class Person:
    def __init__(self,name, age, idcard):
        self.name = name
        self._age = age # 有一个下划线的变量名为protected，只能在父类和子类中访问，虽然也可以在类外部访问，但极不推荐
        self.__idcard = idcard # 有两个下划线的变量名为私有属性，只能在父类中访问

    # 注册 age 属性的 getter 方法，当访问 Person 实例的 age 属性时，下面的 age 方法就会自动调用
    @property
    def age(self):
        return self._age

    # 注册 age 属性的 setter 方法，当修改 Person 实例的 age 属性时，下面的 age 方法就会自动调用
    @age.setter
    def age(self,value):
        self._age = value

p1 = Person('张三',18, '1101')
print(p1.age)