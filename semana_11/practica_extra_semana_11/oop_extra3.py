
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.__balance = 0  # __ Makes the attribute private.

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}.")
    
    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}.")
            return True   # Helps if later your code depends on whether the withdrawal succeeded.
        else:
            print("Error. Insufficient funds.")
            return False   # Helps if later your code depends on whether the withdrawal succeeded.
    
    def get_balance(self):  # getter
        return self.__balance
    
    def set_balance(self, amount):
        if amount >= 0:
            self.__balance = amount
        else:
            print("Balance cannot be negative.")

my_acct = BankAccount("Diego")

def main():
    my_acct.deposit(50)
    my_acct.withdraw(10)
    my_acct.__balance = 1000000
    print(my_acct.get_balance())



main()