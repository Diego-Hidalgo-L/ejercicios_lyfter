
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        area = 3.14 * (self.radius ** 2)
        return area


my_circle = Circle(4)

def main():
    my_circle_area = my_circle.get_area()
    print(f"My circle's area is: {my_circle_area}")


main()