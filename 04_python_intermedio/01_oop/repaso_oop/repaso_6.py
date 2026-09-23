
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0
    
    def __str__(self):
        return f"Cuenta de {self.owner} - Balance: ${self.balance}."
    
    def deposit(self, amount):
        self.balance += amount
        

    def withdraw(self, amount):
        if amount > self.balance:
            return "Fondos insuficientes."
        
        self.balance -= amount


def main():
    my_acct = BankAccount("Diego")

    my_acct.deposit(700)
    my_acct.withdraw(200)
    print(my_acct)


main()