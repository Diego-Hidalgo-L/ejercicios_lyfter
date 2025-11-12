
class Camera:
    def take_photo(self):
        return "Photo taken!"

class Phone:
    def call(self, number):
        return f"Calling {number}..."

class SmartPhone(Camera, Phone):
    def __init__(self, name):
        self.name = name

phone1 = SmartPhone("iPhone DIEGO")

print(phone1.call("8893-1411"))
print(phone1.take_photo())
