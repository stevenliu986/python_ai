"""
1. python中的with主要用于管理程序中需要“成对出现的操作”。例如：
    上锁/解锁
    打开/关闭
    借用/归还
2. 最终目标：编码者只管做具体的事，“进入”和“离开”的事由python来自动处理
3. 语法格式：
    with 能得到一个上下文管理器的表达式 as 变量:
        具体的事1
        具体的事2
        具体的事3
        ...
4. 上下文管理器协议：
    a. __enter__方法：with 中的代码执行 “之前” 调用 ，其返回值会赋值给 as 后的变量。
    b. __exit__方法：with 中的代码执行 “结束后” 调用 (无论 with 中是否会出现异常都会调用）。
5. 当 with 中的代码发生异常时：__exit__方法的返回值规则如下：
    a. 返回“真”：表示异常已经被处理，异常不会被继续抛出。
    b. 返回“假”：表示异常没有处理，异常会被继续抛出。
"""

# 声明一个Person类，使其遵循上下文管理器协议
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f'{self.name} is {self.age} years old')

    def __enter__(self):
        print('————————进入逻辑————————')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('————————退出逻辑————————')
        print(exc_type) # 异常类型
        print(exc_val)  # 异常对象
        print(exc_tb)   # 异常追踪信息

with Person('John', 25) as p1:
    p1.speak()