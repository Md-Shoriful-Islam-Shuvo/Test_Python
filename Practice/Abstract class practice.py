#Abstract class
from abc import ABC, abstractmethod

# Create the abstract base class
class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        """Process the payment."""
        pass
    @abstractmethod
    def payment_details(self):
        """Return payment details."""
        pass

    def validate(self, amount):
        if amount <= 0:
            return False
        return True

# Create concrete implementations
class CreditCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number
    def process_payment(self, amount):
        return f"Processing credit card payment of ${amount}"

    def payment_details(self):
        return f"Credit card: {maskked_number(self.card_number)}"

class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email
    def process_payment(self, amount):
        return f"Processing PayPal payment of ${amount}"
    def payment_details(self):
        return f"PayPal account: {self.email}"

def maskked_number(card_number):
        card_str = str(card_number)
        length = len(card_str)-4
        return '*' * length + card_str[length:]

# Test the implementations - DO NOT MODIFY THIS TEST CODE
cc = CreditCard("1234567890123456")
pp = PayPal("user@example.com")

# Process valid payments
if cc.validate(100):
    print(cc.process_payment(100))
    print(cc.payment_details())

if pp.validate(200):
    print(pp.process_payment(200))
    print(pp.payment_details())

# Try an invalid amount
if not pp.validate(0):
    print("Invalid payment amount")

# This would raise an error if uncommented:
# pm = PaymentMethod()  # Can't instantiate abstract class