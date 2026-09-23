
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self._name = name
    
    def get_name(self):
        return self._name

    @abstractmethod
    def calculate_salary(self):
        pass


class SalariedEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self._monthly_salary = monthly_salary

    def calculate_salary(self):
        return self._monthly_salary


class HourlyEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        self._hours_worked = hours_worked
        self._hourly_rate = hourly_rate
    
    def calculate_salary(self):
        return self._hours_worked * self._hourly_rate


def main():
    employees = [
    SalariedEmployee("Ana", 3000),
    HourlyEmployee("Luis", 120, 15),
    SalariedEmployee("Marta", 3500),
]
    
    for employee in employees:
        print(f"{employee.get_name()} earns {employee.calculate_salary()}")


main()