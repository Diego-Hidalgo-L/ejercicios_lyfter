
class Dog:

    def __init__(self, name):
        self.name = name

    @classmethod
    def create_puppy(cls):
        return cls("Puppy")
    
    
dog = Dog.create_puppy()
print(dog.name)