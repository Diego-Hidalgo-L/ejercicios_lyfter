
class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        speed = 0

    def accelerate(self, amount):
        self.speed += amount
    
    def brake(self, amount):
        self.speed -= amount
        if self.speed < 0:
            self.speed = 0

    def __str__(self):
        return f"{self.brand} {self.model} - Speed: {self.speed} km/h"

car1 = Car("Toyota", "Corolla")

def main():
    car1.accelerate(50)
    car1.brake(30)
    print(car1)


main()