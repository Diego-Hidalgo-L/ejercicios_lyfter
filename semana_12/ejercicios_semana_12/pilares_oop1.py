
class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        self.balance -= amount
    
class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        self.min_balance = min_balance
    
