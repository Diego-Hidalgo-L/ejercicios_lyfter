
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    def __str__(self):
        return self.__class__.__name__.lower()

    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    def calculate_area(self):
        return round(math.pi * (self.radius ** 2), 2)


class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_perimeter(self):
        return self.side * 4
    
    def calculate_area(self):
        return self.side ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height


def main():
    shapes = [
        Circle(3),
        Square(8),
        Rectangle(5, 8)
    ]

    for shape in shapes:
        print(f"The {shape}'s perimeter is: {shape.calculate_perimeter()}")
        print(f"The {shape}'s area is: {shape.calculate_area()}\n")


main()