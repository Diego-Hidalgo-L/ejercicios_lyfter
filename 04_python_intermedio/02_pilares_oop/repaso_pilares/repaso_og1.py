
class BankAccount:
    def __init__(self):
        self.__balance = 0
    
    def _validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("La cantidad a depositar o retirar debe ser positiva.")
    
    def deposit(self, amount):
        self._validate_amount(amount)
        self.__balance += amount

    def withdraw(self, amount):
        self._validate_amount(amount)

        if amount > self.__balance:
            raise ValueError("Fondos insuficientes.")
        
        self.__balance -= amount
    
    def get_balance(self):
        return self.__balance


class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        super().__init__()
        self.__min_balance = min_balance
    
    def withdraw(self, amount):
        if self.get_balance() - amount < self.__min_balance:
            raise ValueError("No se pueden hacer retiros que hagan que el balance quede por debajo del balance mínimo.")
        
        super().withdraw(amount)


def main():
    try:
        my_account = SavingsAccount(20)
        my_account.deposit(100)
        my_account.withdraw(50)  
        my_account.withdraw(40)
    except ValueError as e:
        print(e)


main()