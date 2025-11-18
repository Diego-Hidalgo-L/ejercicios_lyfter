
from datetime import date 

class User:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        return self.age

    @age.setter
    def age(self):
        today = date.today()
        self.age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

    def check_age(func):
        def wrapper(self, user):
            if self.age >= 18:
                func(user)
            else:
                print(f"Error: The user '{self.name}' is younger than 18 years old.")
        
        return wrapper

    @check_age
    def is_of_age(self):
        print(f"The user '{self.name}' is of legal age.")
    
    @check_age
    def buy_beer(self):
        print(f"{self.name} bought a beer for $8.")


user_1 = User("Diego", date(1997, 5, 25))
user_1.is_of_age(user_1)
user_1.buy_beer(user_1)
# print(user_1.age)

user_2 = User("Mateo", date(2014, 12, 19))
user_2.is_of_age(user_2)
user_2.buy_beer(user_2)
# print(user_2.age)