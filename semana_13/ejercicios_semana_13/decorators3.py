
from datetime import date 

class User:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        age = today.year - self.date_of_birth.year - ((today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))

        return age


def check_age(func):
    def wrapper(user):
        try:
            if user.age >= 18:
                return func(user)
            else:
                raise ValueError(f"ValueError: User {user.name} is underage ({user.age} years old).")
        except ValueError:
            print(f"ValueError: User {user.name} is underage ({user.age} years old).")

    return wrapper


@check_age
def is_of_age(user):
    print(f"The user '{user.name}' is of legal age ({user.age} years old).")


@check_age
def buy_beer(user):
    print(f"{user.name} bought a beer for $8.")


user_1 = User("Diego", date(1997, 5, 25))
print("\n")
is_of_age(user_1)
result = buy_beer(user_1)
print(result)
print("\n")


user_2 = User("Mateo", date(2014, 12, 19))
is_of_age(user_2)
buy_beer(user_2)
print("\n")