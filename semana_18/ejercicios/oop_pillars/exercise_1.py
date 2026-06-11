
class BankAccount:
    def __init__(self):
        self.balance = 0
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        else:
            self.balance -= amount


class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        super().__init__()
        self.min_balance = min_balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds")
        elif self.balance - amount < self.min_balance:
            print("Balance cannot go below minimum balance ($100)")
        else:
            super().withdraw(amount)


my_acct = SavingsAccount(100)

def main():
    my_acct.deposit(300)
    my_acct.withdraw(500)
    my_acct.deposit(100)
    print(my_acct.balance)


main()