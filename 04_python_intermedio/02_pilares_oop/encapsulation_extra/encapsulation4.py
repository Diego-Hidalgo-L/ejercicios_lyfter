
class Car:
    def __init__(self, max_speed):
        self.__speed = 0
        self.__max_speed = max_speed
    
    def accelerate(self, amount):
        new_speed = self.__speed + amount
        if new_speed > self.__max_speed:
            self.__speed = self.__max_speed
            print(f"Speed: {self.__speed} (Can't exceed the speed limit).")
        else:
            self.__speed = new_speed
            print(f"Speed: {self.__speed}")
    
    def brake(self, amount):
        if amount > self.__speed:
            self.__speed = 0
            print(f"Speed: {self.__speed}")
        else:
            self.__speed -= amount
            print(f"Speed: {self.__speed}")
    
    def get_speed(self):
        return self.__speed


my_car = Car(180)

my_car.accelerate(50)   # speed: 50
my_car.accelerate(200)  # speed: 180 (not 250)
my_car.brake(30)        # speed: 150
my_car.brake(500)       # speed: 0

print(my_car.get_speed())  # Should print 0 at the end

print(my_car.__speed)      # Should raise an AttributeError