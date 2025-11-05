class Person:
    def __init__(self, name):
        self.name = name


class Bus:
    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.passengers = []

    def add_passenger(self, passenger):
        if len(self.passengers) < self.max_passengers:
            self.passengers.append(passenger)
            print(f"{passenger.name} has been added to the bus.")
        else:
            print("The bus is full!")

    def remove_passenger(self, passenger):
        if passenger in self.passengers:
            self.passengers.remove(passenger)
            print(f"{passenger.name} has been removed from the bus.")
        else:
            print(f"{passenger.name} was not found on the bus.")


person1 = Person("John")
person2 = Person("Mary")
person3 = Person("Paul")

bus1 = Bus(10)

def main():
    bus1.add_passenger(person1)
    bus1.add_passenger(person2)
    bus1.add_passenger(person3)
    bus1.remove_passenger(person1)


main()