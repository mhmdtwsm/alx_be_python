class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if self.account_balance != 0:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(self.account_balance)


harry = BankAccount(100)
harry.withdraw(50)


print(harry.display_balance())
