
import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_area(self):
        return round(math.pi, 2) * (self.radius ** 2)
    

my_circle = Circle(4)

def main():
    area = my_circle.get_area()
    print(f"My circle's area: {area}")


main()