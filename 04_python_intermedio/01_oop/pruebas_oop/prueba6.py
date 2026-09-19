class Car:
    speed = 0  # class attribute

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")

car1.speed += 50
print(car2.speed) 
