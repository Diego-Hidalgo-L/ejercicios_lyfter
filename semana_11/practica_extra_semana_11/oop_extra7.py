
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Some generic animal sound.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        # print("Woof!")    # Si dejo este print, se printea antes del animal.speak() de abajo.
        return "Woof!"      # return es mejor para "testable and reusable code".

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        # print("Meow!")    # Si dejo este print, se printea antes del animal.speak() de abajo.
        return "Meow!"      # return es mejor para "testable and reusable code".


animals = [Dog("Rex"), Cat("Mimi"), Dog("Buddy"), Cat("Luna")]

for animal in animals:
    print(f"{animal.name} goes '{animal.speak()}'")