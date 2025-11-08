
class MusicPlayerMixin:
    def play_music(self, song):
        return f"Playing {song}"

class GPSMixin:
    def navigate_to(self, location):
        return f"Navigating to {location}."
    
class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def drive(self):
        return f"Driving the {self.brand}."

class SmartCar(MusicPlayerMixin, GPSMixin, Car):    # Mixins usually come before the main class so they override defaults (if needed).
    pass

my_car = SmartCar("Tesla")

print(my_car.drive())
print(my_car.navigate_to("Rhode Island"))
print(my_car.play_music("Broadview - Slow Pulp"))
