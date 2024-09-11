from exceptions import InsufficientFundsException

class Account:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        else:
            raise InsufficientFundsException
    
    def deposit(self, amount):
        if amount <= 0: #1 added positive value check
            raise ValueError("deposit must be a positive value")
        self.balance += amount
        return self.balance

