
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32
    
    def to_kelvin(self):
        return self.celsius + 273.15


def main():
    temp = Temperature(25)

    print(f"{temp.celsius}°C en Fahrenheit: {temp.to_fahrenheit()}")
    print(f"{temp.celsius}°C en Kelvin: {temp.to_kelvin()}")


main()