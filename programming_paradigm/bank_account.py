class BankAccount:

    def __init__(self, account_balance):
        self.account_balance = account_balance
        self.balance = 0

    def deposit(self, amount):
        self.account_balance += amount
        return self.account_balance
    
    def withdraw(self, amount):
        if self.account_balance > amount:
            self.account_balance -= amount
            return True
        else:
            return False
        
    def display_balance(self):
        print('='*50)
        print(f"The remaining balance on your account is {self.account_balance}")
        print('='*50)
