#Bank Account Manager Challenge
class BankAccount:
    interest_rate = 0.02 # Class variable for interest rate
    def __init__(self,owner_name,balance):
        self.__owner_name = owner_name
        self.__balance = balance

    @property
    def owner_name(self):
        return self.__owner_name
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, new_balance):
        if new_balance < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = new_balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
            return False
        self.__balance += amount
        return True
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
            return False
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
            return False
        self.__balance -= amount
        return True
    def apply_interest(self):
        interest = self.__balance * BankAccount.interest_rate
        self.__balance += interest
        return interest
    def display_info(self):
        print(f"Account Owner: {self.__owner_name}, \nBalance: ${self.__balance:.2f}\nInterest Rate: {BankAccount.interest_rate*100:.2f}%")

# Example usage:
if __name__ == "__main__":
    account = BankAccount("John Doe", 1000.00)
    account.display_info()
    account.deposit(500)
    account.withdraw(200)
    interest = account.apply_interest()
    print(f"Interest applied: ${interest:.2f}")
    account.display_info()