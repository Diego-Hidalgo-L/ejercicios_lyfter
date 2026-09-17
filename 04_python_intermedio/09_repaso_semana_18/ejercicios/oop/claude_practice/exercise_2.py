
class BankAccount:
    def __init__(self, owner):
        self.__owner = owner
        self.__balance = 0
        self.__transaction_history = []
        self._deposit_tracking = 0

    @property
    def owner(self):
        return self.__owner

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print("Amount cannot be negative or equal to zero (0)")
        else:
            self.__balance += amount
            self.__transaction_history.append(f"Deposit: ${amount} (Balance: {self.balance})")
            self._deposit_tracking += 1
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Amount cannot be negative or equal to zero (0)")
        elif amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdraw: ${amount}")
    
    def transfer(self, amount, other_account):
        if amount <= 0:
            print("Amount cannot be negative or equal to zero (0)")
        elif amount > self.__balance:
            print("Insufficient funds")
        else:
            self.__balance -= amount
            other_account.deposit(amount)
            self.__transaction_history.append(f"Transfer: ${amount} to {other_account.owner}")

    def print_statement(self):
        for index, transaction in enumerate(self.__transaction_history):
            print(f"Transaction {index + 1} -> {transaction}")


class SavingsAccount(BankAccount):
    def __init__(self, owner, min_balance):
        super().__init__(owner)
        self.__min_balance = min_balance

    @property
    def interest_rate(self):
        return 0.05
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Amount cannot be negative or equal to zero (0)")
        elif self.balance - amount < self.__min_balance:
            print("Cannot go below the minimum balance")
        else:
            super().withdraw(amount)
    
    def apply_interest(self):
        self._BankAccount__balance += (self.balance * self.interest_rate)


class PremiumAccount(SavingsAccount):
    @property
    def interest_rate(self):
        return 0.08
    
    def add_bonus(self):
        if self._deposit_tracking > 0 and self._deposit_tracking % 5 == 0:
            self._BankAccount__balance += 10
            self._BankAccount__transaction_history.append(f"Bonus: $10 (Balance: {self.balance})")

    def deposit(self, amount):
        super().deposit(amount)
        self.add_bonus()


save1 = SavingsAccount("Diego", 25)

prem1 = PremiumAccount("Mateo", 100)

prem1.deposit(200)
prem1.deposit(50)
prem1.deposit(100)
prem1.deposit(25)
prem1.deposit(25)

prem1.transfer(150, save1)

prem1.print_statement()
save1.print_statement()