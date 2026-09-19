
class Car:
    wheels = 4

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    

car1 = Car("Toyota", "Corolla")
car2 = Car("Tesla", "Model S")

def main():
    print(car1.wheels)
    print(car2.wheels)

    car1.wheels = 3

    print(car1.wheels)
    print(car2.wheels)


main()