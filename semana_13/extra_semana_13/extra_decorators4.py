
from functools import wraps

def require_positive(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            all_params = args[1:]
            all_params += tuple(kwargs.values())

            for param in all_params:
                if param <= 0:
                    print("Invalid input. Please enter positive parameters only.")
                    return
            return func(*args, **kwargs)

        return wrapper


class BankAccount:
    def __init__(self):
        self.__balance = 0

    @require_positive
    def deposit(self, amount):
        self.__balance += amount

    @require_positive
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance


my_account = BankAccount()

my_account.deposit(500)
print(my_account.get_balance())