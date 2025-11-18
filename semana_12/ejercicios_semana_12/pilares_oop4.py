
class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    @property
    def show_name(self):
        return self.__name

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, amount):
        if amount <= 0:
            print("El salario no puede ser negativo.")
        else:
            self.__salary = amount
    
    def promote(self, percentage):
        if percentage <= 0:
            print("El porcentaje debe ser positivo.")
        else:
            new_salary = self.__salary * (1 + percentage)
            self.salary = new_salary


employee = Employee("Ana", 1000)
employee.promote(0.1)

print(employee.salary)
print(employee.show_name)