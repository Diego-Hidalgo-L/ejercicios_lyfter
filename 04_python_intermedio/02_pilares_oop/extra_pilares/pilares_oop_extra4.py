
class Animal:
    def move(self):
        return "Animal is moving."


class Mammal(Animal):
    def move(self):
        return "Mammal is walking."


class Bird(Animal):
    def move(self):
        return "Bird is flying."


class Bat(Mammal, Bird):
    pass


batty = Bat()

print(batty.move())

print(Bat.__mro__)