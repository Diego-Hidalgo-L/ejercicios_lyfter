
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius


    def get_area(self):
        area = math.pi * (self.radius ** 2)
        return area
    

    def get_circumference(self):
        circumference = 2 * math.pi * self.radius
        return circumference


my_circle = Circle(4)

my_circle_area = my_circle.get_area()

my_circle_circumference = my_circle.get_circumference()


print(f"My circle's area is: {my_circle_area}")

print(f"My circle's circumference is: {my_circle_circumference}")