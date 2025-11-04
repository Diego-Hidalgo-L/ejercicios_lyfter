
class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <=0:
            raise ValueError("Please enter positive values only.")
        else:
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
            width = int(input("\nEnter the rectangle's width: "))
            height = int(input("Enter the rectangle's height: "))

            return Rectangle(width, height)

        except ValueError as e:
            print(f"\nError: {e}")


def main():
    rectangle1 = create_rectangle()
    # rectangle2 = Rectangle(5, 3)

    area = rectangle1.get_area()
    print(f"\nThe rectangle's area is: {area}.")

    perimeter = rectangle1.get_perimeter()
    print(f"The rectangle's perimeter is: {perimeter}.\n")


main()