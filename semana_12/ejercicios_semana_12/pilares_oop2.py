
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def calculate_perimeter(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return "This is a circle."
    
    def calculate_perimeter(self):
        return 2 * 3.14 * self.radius

    def calculate_area(self):
        return 3.14 * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "This is a rectangle."
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def calculate_area(self):
        return self.width * self.height


class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def __str__(self):
        return "This is a square"

    def calculate_perimeter(self):
        return 4 * self.side
    
    def calculate_area(self):
        return self.side ** 2