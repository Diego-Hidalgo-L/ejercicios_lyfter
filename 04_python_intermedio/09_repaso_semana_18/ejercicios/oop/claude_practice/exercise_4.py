
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @property
    def is_adult(self):
        return self.age >= 18


class Bus:
    person: Person

    def __init__(self, route_number, max_passengers, current_stop):
        self.route_number = route_number
        self.max_passengers = max_passengers
        self.current_stop = current_stop
        self.__passengers = []

    @property
    def passenger_count(self):
        return len(self.__passengers)

    @property
    def is_full(self):
        return self.passenger_count >= self.max_passengers

    def board(self, person):
        if self.is_full:
            print("The bus is full")
        elif not person.is_adult:
            print("The passenger is not an adult (18+)")
        else:
            self.__passengers.append(person)

    def board_group(self, *people):
        for person in people:
                if self.is_full:
                    print(f"{person.name} did not board because the bus is full")
                elif not person.is_adult:
                    print(f"{person.name} can't board the bus because they're not an adult (18+)")
                else:
                    self.__passengers.append(person)
                    print(f"{person.name} boarded the bus")
    
    def get_off(self, person_name):
        for index, person in enumerate(self.__passengers):
            if person.name == person_name:
                self.__passengers.pop(index)
                return f"{person.name} was removed from the bus"
        
        raise ValueError(f"The passenger {person_name} was not found on the bus")

    def next_stop(self, stop_name):
        self.current_stop = self.stop_name
        print(f"Next stop is: {stop_name}")
    
    def manifest(self):
        print(f"Current stop: {self.current_stop}")
        print("Passengers:")
        for passenger in self.__passengers:
            print(passenger.name)


class BusFleet:
    bus: Bus

    def __init__(self):
        self.buses = []
    
    def add_bus(self, bus):
        self.buses.append(bus)
    
    def find_bus_with_space(self):
        for bus in self.buses:
            if not bus.is_full:
                return bus
    
    def total_passengers(self):
        return sum(bus.passenger_count for bus in self.buses)
    
    def fleet_report(self):
        print()
        for bus in self.buses:
            print(f"Route number: {bus.route_number}")
            print(f"Current stop: {bus.current_stop}")
            print(f"Passenger count: {bus.passenger_count}")
            print(f"Max passengers: {bus.max_passengers}")