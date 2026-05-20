
class BankAccount:
    def __init__(self, owner):
        self._owner = owner
        self._balance = 0
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("La cantidad a depositar debe ser positiva.")
        
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("La cantidad a retirar debe ser positiva.")

        if amount > self._balance:
            raise ValueError("Fondos insuficientes.")
        
        self._balance -= amount

    def get_balance(self):
        return self._balance


def main():
    acct = BankAccount("Diego")

    try:
        acct.deposit(500)
        acct.withdraw(-200)

        print(acct.get_balance())
    
    except ValueError as e:
        print(e)
        


main()
