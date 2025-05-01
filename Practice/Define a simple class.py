class BankAccount:
    # Add class attribute here
    bank_name='Python National Bank'
    # Add the methods here
    def depositer(self,ammount):
        self.balance+=ammount
    def transactions(self,withdraw):
        self.balance-=withdraw
    
# Create an account and test your methods
my_account = BankAccount()
my_account.balance = 0  # Starting balance
ammount=100
# Make transactions
my_account.depositer(ammount)
my_account.transactions(30)

# Print the final balance
print(f"Current balance: ${my_account.balance}")