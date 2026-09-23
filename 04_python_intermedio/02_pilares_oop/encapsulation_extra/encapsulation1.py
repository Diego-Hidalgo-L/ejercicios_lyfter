
class Person:
    def __init__(self, age):
        self.__age = age
    
    def get_age(self):
        return self.__age


person1 = Person(35)

print(person1.__age)

print(person1.get_age())