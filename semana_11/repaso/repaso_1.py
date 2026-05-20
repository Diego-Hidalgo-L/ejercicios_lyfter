
class Square:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return self.side * 4


def main():
    my_square = Square(5)
    
    print(my_square.get_area())
    print(my_square.get_perimeter())


main()