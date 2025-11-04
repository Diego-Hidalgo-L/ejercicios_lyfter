
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}.")
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance: {self.balance}.")
            return True   # Helps if later your code depends on whether the withdrawal succeeded.
        else:
            print("Error. Insufficient funds.")
            return False   # Helps if later your code depends on whether the withdrawal succeeded.

my_acct = BankAccount("Diego")

def main():
    my_acct.deposit(50)
    my_acct.withdraw(30)
    print(f"Your balance is: {my_acct.balance}")


main()