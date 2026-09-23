
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Some generic animal sound.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Woof!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Meow!")

dog1 = Dog("Rex")
dog1.speak()

cat1 = Cat("Mimi")
cat1.speak()

