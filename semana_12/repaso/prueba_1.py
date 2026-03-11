
class Vehicle:
    is_on = False
    wheel_number = 0

    def turn_on(self):
        self.is_on = True
        print(f"Vehicle with {self.wheel_number} wheels is on.")

    def turn_off(self):
        self.is_on = False
        print(f"Vehicle with {self.wheel_number} wheels is off.")


class Car(Vehicle):
    wheel_number = 4


class Bike(Vehicle):
    wheel_number = 2


my_car = Car()
my_car.turn_on()
my_car.turn_off()

my_bike = Bike()
my_bike.turn_on()
my_bike.turn_off()