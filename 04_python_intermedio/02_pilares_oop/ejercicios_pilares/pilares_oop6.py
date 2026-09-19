
from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand, year):
        self._brand = brand
        self._year = year
    
    @abstractmethod
    def get_info(self):
        pass


class Car(Vehicle):
    def __init__(self, brand, year, doors):
        super().__init__(brand, year)
        self.doors = doors
    
    def get_info(self):
        return f"{self._brand} ({self._year}) - {self.doors} doors."

    def __str__(self):
        return self.get_info()


class Motorcycle(Vehicle):
    def __init__(self, brand, year, kind):
        super().__init__(brand, year)
        self.kind = kind

    def get_info(self):
        return f"{self._brand} ({self._year}) - Kind: {self.kind}."
    
    def __str__(self):
        return self.get_info()


vehicle1 = Car("Toyota", 2020, 4)
print(vehicle1)

vehicle2 = Motorcycle("Yamaha", 2022, "Sports")
print(vehicle2)