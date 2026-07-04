form abc import ABC, abstractmethod

# 抽象类是一种不能直接实例化的类，它通常作为“规范”，让子类去继承，并实现其中定义的抽象方法
class MustRun(ABC):

    @abstractmethod
    def run(self):
        pass

class Person(MustRun):

    def run(self):
        print('running')