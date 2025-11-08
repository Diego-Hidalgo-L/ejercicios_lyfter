
from abc import ABC, abstractmethod

class Walkable(ABC):
    @abstractmethod
    def walk(self):
        pass


class Speakable(ABC):
    @abstractmethod
    def speak(self):
        pass


class RobotDog(Walkable, Speakable):
    def __init__(self, name):
        self.name = name
    
    def walk(self):
        return f"{self.name}, the robot dog, is walking."
    
    def speak(self):
        return f"Woof! I am {self.name}, the robot dog."


robot_dog = RobotDog("Alfie")

print(robot_dog.walk())
print(robot_dog.speak())