
class BankAccount:
    def __init__(self):
        self.__balance = 0
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Cannot deposit a negative amount.")
    
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance

account = BankAccount()

# account.deposit(100)
# account.withdraw(40)
# print(account.get_balance())  # Expected: 60
# print(f"New balance: {self.__balance}")

# account.deposit(-20)          # Should give an error
# account.withdraw(1000)        # Should give an error
# print(f"New balance: {self.__balance}")

# print(account.__balance)      # Should raise an AttributeError
