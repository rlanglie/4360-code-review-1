from exceptions import BankingException, InsufficientFundsException, PositiveAmountException

class Account:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        try: #14 wrapped with try statement to allow exceptions to raise properly
            if self.balance >= amount:
                self.balance -= amount
                return self.balance
            else:
                raise InsufficientFundsException
        except BankingException as e:
            message.print(e.message())
        except:
            message.print("An error occurred")

    
    def deposit(self, amount):
        if amount <= 0: #1 added positive value check
            raise PositiveAmountException
        self.balance += amount
        return self.balance

