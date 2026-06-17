
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


def create_rectangle():
    while True:
        try:
            width = float(input("Enter the rectangle's width: "))
            height = float(input("Enter the rectangle's height: "))

            if width < 0 or height < 0:
                print("Error: Please enter positive numbers only")
                continue

            return Rectangle(width, height)

        except ValueError:
            print("Error: Please enter numbers only")


def main():
    my_rectangle = create_rectangle()

    area = my_rectangle.get_area()
    perimeter = my_rectangle.get_perimeter()

    # Prints: 
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")


main()