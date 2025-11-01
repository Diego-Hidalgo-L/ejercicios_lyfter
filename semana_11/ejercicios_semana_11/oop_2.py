
class Bus:
    max_passengers = 20
    total_passengers = 0

    def add_passengers(self, max_passengers, total_passengers):
        if total_passengers <= max_passengers:
            total_passengers += 1
            return total_passengers
        else:
            print("You have reached the maximum number of passengers allowed on the bus.")
    

    def subtract_passengers(self):
        total_passengers -= 1
        return total_passengers


my_bus = Bus()

passengers = my_bus.add_passengers()
print(passengers)