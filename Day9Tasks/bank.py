''' Bank Account System (Class, Object, Constructor)
A bank wants to manage customer accounts. Create a BankAccount class with a
constructor to initialize account number and balance. Implement methods to deposit,
withdraw, and display balance.'''

class BankAccount:
    def __init__(self,account,balance):
        self.account=account
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposit:",amount)
    def withdraw(self,amount):
        self.balance-=amount
        print("withdraw:",amount)
    def display(self):
        print("Account:",self.account)
        print("Balance:",self.balance)

s=BankAccount(12345,3456)
s.deposit(10000)
s.withdraw(5000)
s.display()   