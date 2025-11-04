
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self):
        perimeter = 2 * (self.width + self.height)
        return perimeter


def create_rectangle():
    while True:
        try:
            width = int(input("Enter the rectangle's width: "))
            height = int(input("Enter the rectangles' height: "))

            if width <= 0 or height <= 0:
                print("\nPlease enter positive values only.")
            else:
                return Rectangle(width, height)

        except ValueError:
            print("\nInvalid input. Please enter integers only.")


def main():
    rectangle1 = create_rectangle()

    area = rectangle1.get_area()
    print("\n")
    print(f"The rectangle's area is: {area}")

    perimeter = rectangle1.get_perimeter()
    print(f"The rectangle's perimeter is: {perimeter}")


main()