
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year

    @abstractmethod
    def get_info(self):
        pass

    def __str__(self):
        return self.get_info()


class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors
    
    def get_info(self):
        return f"This is a {self._brand} {self.__class__.__name__.lower()} from the year {self._year} and it has {self.doors} doors."


class Motorcycle(Vehicle):
    def __init__(self, brand, year, style):
        super().__init__(brand, year)
        self.style = style
    
    def get_info(self):
        return f"This is a {self._brand} {self.style} {self.__class__.__name__.lower()} from the year {self._year}."


def main():
    vehicles = [
        Car("Toyota", 2020, 4),
        Motorcycle("Yamaha", 2022, "sport")
    ]

    for vehicle in vehicles:
        print(vehicle)


main()