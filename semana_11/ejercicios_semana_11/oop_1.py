
class Circle:
    radius = 4

    def get_area(self):
        area = 3.14 * (self.radius ** 2)
        return area


my_circle = Circle()

my_circle_area = my_circle.get_area()

print(my_circle_area)