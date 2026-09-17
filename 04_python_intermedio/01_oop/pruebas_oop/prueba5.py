class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self) -> int:
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def perimeter(self) -> int:
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.width + self.height)

    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


def create_rectangle() -> Rectangle:
    """Prompt the user to create a rectangle with positive integer dimensions."""
    while True:
        try:
            width = int(input("Enter the rectangle's width: "))
            height = int(input("Enter the rectangle's height: "))

            if width <= 0 or height <= 0:
                print("Please enter positive values only.\n")
                continue

            return Rectangle(width, height)

        except ValueError:
            print("Invalid input. Please enter integers only.\n")


def main():
    rectangle = create_rectangle()
    print(f"\nYou created: {rectangle}")
    print(f"Area: {rectangle.area()}")
    print(f"Perimeter: {rectangle.perimeter()}")


if __name__ == "__main__":
    main()
