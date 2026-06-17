
class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, person):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(person)
            print(f"{person.name} has been added to the bus.")
        else:
            print("The bus is full!")

    def remove_passenger(self, person):
        if person in self.passengers:
            self.passengers.remove(person)
            print(f"{person.name} has been removed from the bus")
        else:
            print(f"{person.name} was not found one the bus")


person1 = Person("Peter")
person2 = Person("Paul")
person3 = Person("Mary")

bus1 = Bus(10)

def main():
    bus1.add_passenger(person1)
    bus1.add_passenger(person2)
    bus1.add_passenger(person3)
    bus1.remove_passenger(person2)


main()