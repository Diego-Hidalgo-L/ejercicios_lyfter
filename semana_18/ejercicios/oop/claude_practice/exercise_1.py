
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @property
    @abstractmethod
    def name(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

    def describe(self):
        print(f"Name: {self.name}")
        print(f"Area: {self.calculate_area()}")
        print(f"Perimeter: {self.calculate_perimeter()}")


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("The circle's radius must be positive")
        else:
            self.radius = radius
    
    @property
    def name(self):
        return "Circle"

    @classmethod
    def from_string(cls, my_str):
        radius = my_str.split(":")[1]
        return cls(float(radius))

    def calculate_area(self):
        return round(math.pi * (self.radius ** 2), 2)
    
    def calculate_perimeter(self):
        return round(2 * math.pi * self.radius, 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("The rectangle's sides must be positive")
        else:
            self.width = width
            self.height = height
    
    @property
    def name(self):
        return "Rectangle"
    
    @classmethod
    def from_string(cls, my_str):
        dimensions = my_str.split(":")[1]
        width, height = dimensions.split("x")
        return cls(float(width), float(height))

    def calculate_area(self):
        return self.width * self.height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise ValueError("All triangle sides must be positive")

        if (side1 + side2 <= side3 or 
            side1 + side3 <= side2 or
            side2 + side3 <= side1):
            raise ValueError("Invalid triangle")
        else:
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3

    @property
    def name(self):
        return "Triangle"

    @classmethod
    def from_string(cls, my_str):
        sides = my_str.split(":")[1]
        side1, side2, side3 = sides.split(",")
        return cls(float(side1), float(side2), float(side3))

    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return round(math.sqrt(s * (s-self.side1) * (s-self.side2) * (s-self.side3)), 2)

    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3


def total_area(*shapes):
    return sum(shape.calculate_area() for shape in shapes)


def main():
    try: # En este caso no es tan necesario porque estoy hardcoding valores válidos de cada Shape. Sería más necesario si este input fuera ingresado por el usuario.
        circ1 = Circle.from_string("circle:5")
        rect1 = Rectangle.from_string("rect:4x6")
        tri1 = Triangle.from_string("tri:3,4,5")
        shapes = [circ1, rect1, tri1]

        print("\nTotal area:")
        print(total_area(*shapes))

        for shape in shapes:
            print()
            shape.describe()
    
    except ValueError as e:
        print(f"Error: {e}")


main()