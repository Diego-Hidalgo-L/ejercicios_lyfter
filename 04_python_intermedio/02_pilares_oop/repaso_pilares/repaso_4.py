
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    def validate_amount(self, amount):
        if amount <= 0:
            raise ValueError("The payment must be positive")

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(PaymentMethod):
    def pay(self, amount):
        self.validate_amount(amount)
        print(f"Paid {amount} using Credit Card")


class PayPal(PaymentMethod):
    def pay(self, amount):
        self.validate_amount(amount)
        print(f"Paid {amount} using PayPal")


class Bitcoin(PaymentMethod):
    def pay(self, amount):
        self.validate_amount(amount)
        print(f"Paid {amount} using Bitcoin")


def main():
    payments = [
    CreditCard(),
    PayPal(),
    Bitcoin()
]
    try:
        for payment in payments:
            payment.pay(100)
    except ValueError as e:
        print(e)


main()