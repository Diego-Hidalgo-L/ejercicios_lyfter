
class Engine:
    def __init__(self, kind):
        self.kind = kind

class Wheel:
    def __init__(self, brand):
        self.brand = brand

class Car:
    def __init__(self, engine, wheels):
        self.engine = engine
        self.wheels = wheels

    def car_summary(self):
        print(f"Engine type: {self.engine.kind}.")
        print("Wheel brands:")
        for wheel in self.wheels:
            print(wheel.brand)


engine1 = Engine("V6")
wheel1 = Wheel("Michelin")
wheel2 = Wheel("Michelin")
wheel3 = Wheel("Pirelli")
wheel4 = Wheel("Pirelli")

car1 = Car(engine1, [wheel1, wheel2, wheel3, wheel4])

car1.car_summary()
