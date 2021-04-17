from abc import abstractmethod, ABC

"""
Other method to do in Python before v3.4 is:
    from abc import abstractmethod, ABCMeta
    class Shape(metaclass=ABCMeta)
"""
class Shape(ABC):
    @abstractmethod
    def printArea(self):
        return 0

class Rectangle(Shape):
    type = "Rectangle"
    sides = 4
    def __init__(self):
        self.length = 6
        self.breadth = 7
    def printArea(self):
        return self.length * self.breadth

rect1 = Rectangle()
print(rect1.printArea())