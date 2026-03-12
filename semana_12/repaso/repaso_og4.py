
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    
    @property
    def name(self):
        return self.__name
    
    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, amount):
        if amount <= 0:
            raise ValueError("El salario no puede ser menor o igual que 0.")
        
        self.__salary = amount
    
    def promote(self, percentage):
        if percentage <= 0:
            raise ValueError("El porcentaje del aumento debe ser positivo.")
        
        self.__salary *= (1 + percentage / 100)


def main():
    try:
        employee = Employee("Ana", 1000)
        employee.promote(10)

        print(f"{employee.name}'s salary is: ${employee.salary}")
    except ValueError as e:
        print(e)


main()