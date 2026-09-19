
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("Meow")


animals = [Dog(), Cat(), Dog()]

for animal in animals:
    animal.speak()
    

