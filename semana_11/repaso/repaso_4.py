
class CPU:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name

class RAM:
    def __init__(self, gb):
        self.gb = gb
    
    def __str__(self):
        return str(self.gb)

class Storage:
    def __init__(self, gb):
        self.gb = gb
    
    def __str__(self):
        return str(self.gb)

class Monitor:
    def __init__(self, size):
        self.size = size
    
    def __str__(self):
        return str(self.size)

class Keyboard:
    def __init__(self, brand):
        self.brand = brand
    
    def __str__(self):
        return self.brand

class Computer:
    def __init__(self, name, cpu, ram, storage, monitor, keyboard):
        self.name = name
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.monitor = monitor
        self.keyboard = keyboard

    def __str__(self):
        return f"Computer: {self.name} - CPU: {self.cpu} - RAM: {self.ram}GB - Storage: {self.storage}GB."


def main():
    name = "Diego's MacBook Pro"
    cpu = CPU("Apple M5")
    ram = RAM(16)
    storage = Storage(512)
    monitor = Monitor("14-inch")
    keyboard = Keyboard("Apple")

    computer = Computer(name, cpu, ram, storage, monitor, keyboard)
    print(computer)


main()