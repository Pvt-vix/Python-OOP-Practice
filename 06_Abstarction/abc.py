from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass # no implementation, just a placeholder for subclasses to implement

class Circle(Shape):
    def area(self, radius):
        print(f"Area of Circle: {3.14 * radius * radius}")

class Square(Shape):
    def area(self, side):
        print(f"Area of Square: {side * side}")

shape1 = Circle()
shape1.area(5)

shape2 = Square()
shape2.area(4)
