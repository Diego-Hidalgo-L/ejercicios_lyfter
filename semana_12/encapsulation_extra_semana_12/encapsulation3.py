
class BankAccount:
    def __init__(self):
        self.__balance = 0
    
    @property
    def balance(self):
        return self.__balance

    @balance.setter # Setter es por si quiero tener un método que modifique el atributo directamente y con validación. En este caso no es tan útil.
    def balance(self, amount):
        if amount > 0:
            self.__balance = amount
        else:
            print("Balance can't be negative.")

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit: {amount}. New balance: {self.__balance}.")
        else:
            print("Cannot deposit a negative amount.")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}. New balance: {self.__balance}.")
        else:
            print("Insufficient funds.")

account = BankAccount()

account.deposit(100)
account.withdraw(30)

print(account.balance)   # Should print 70

# account.balance = -20   # Should print error and not update