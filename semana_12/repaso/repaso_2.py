
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

        # Otra opción menos Pythonic:
        # return round(math.pi * (self.radius ** 2, 2))


shapes = [
    Rectangle(4, 5),
    Circle(3),
    Rectangle(2, 10)
]

for shape in shapes:
    print(shape.area())

    # Pythonic printing para solo 2 puntos decimales:
    # print(f"{shape.area():.2f}")
