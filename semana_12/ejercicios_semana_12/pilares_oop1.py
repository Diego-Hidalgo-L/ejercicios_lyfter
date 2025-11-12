
class BankAccount:
    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
        else:
            print("Insufficient funds.")

    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        super().__init__()
        self.__min_balance = min_balance

    def withdraw(self, amount):
        if self.get_balance() - amount >= self.__min_balance:
            super().withdraw(amount)
        else:
            print("Cannot withdraw: balance would drop below minimum.")


my_account = SavingsAccount(20)
my_account.deposit(100)
my_account.withdraw(50)  
my_account.withdraw(40)
