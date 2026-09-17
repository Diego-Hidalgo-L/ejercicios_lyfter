
import datetime

class Person:
    name: str #public
    _date_of_birth: datetime #protected
    __sex: str # private

    def __init__(self, name, date_of_birth, sex):
        self.name = name
        self._date_of_birth = date_of_birth
        self.__sex = sex

class Worker(Person):
	def print_date_of_birth(self):
		print(self._date_of_birth)

	def print_sex(self):
		print(self.__sex)

my_person = Person("Juan", "2003/02/02", "Male")
print(my_person.name) # -> Juan
print(my_person._date_of_birth) # -> error, ya que _date_of_birth es un atributo protegido
print(my_person.__sex) # -> err or, ya que __sex es un atributo privado

my_worker = Worker("Joan", "1984/05/06", "Female")
my_worker.print_date_of_birth() # -> 1984/05/06
my_worker.print_sex() # -> error, ya que __sex es un atributo privado