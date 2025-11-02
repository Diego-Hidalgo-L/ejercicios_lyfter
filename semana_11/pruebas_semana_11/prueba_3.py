
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
    

    def is_bigger_than(self, other_circle):
        if self.get_area() > other_circle.get_area():
            return True
        else:
            return False


circle1 = Circle(5)

circle2 = Circle(3)

result = circle1.is_bigger_than(circle2)
print(result)