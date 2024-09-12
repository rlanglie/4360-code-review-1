from message import Message
from exceptions import BankingException, InvalidAccountNumberException, TransferAmtLimitException, TransferNumberLimitException


message = Message()

class User:
    def __init__(self, name, accounts):
        self.name = name
        self.accounts = accounts
        self.session_transfers = 0

    def show_accounts(self):
        message.print("{:<20}{:<0}".format("Account Number", "Amount"))
        for key,val in self.accounts.items():
            balance = val.check_balance()
            message.print("{:<20}{:<0}".format(key, balance))

    
    def deposit(self, args):
        try:
            accountNumber = int(args[0])
            amount = int(args[1])
            account = self.accounts.get(accountNumber)
            
            if not account:
                raise InvalidAccountNumberException

            account.deposit(amount)
            return account.check_balance()
        except BankingException as e:
            message.print(e.message())
        except:
            message.print("An error occurred")

    def withdraw(self, args):
        try:
            accountNumber = int(args[0])
            amount = int(args[1])
            account = self.accounts.get(accountNumber) #12 added .get() to fix InvalidAccountNumberException

            if not account:
                raise InvalidAccountNumberException

            account.withdraw(amount)
            return account.check_balance()
        except BankingException as e:
            message.print(e.message())
        except:
            message.print("An error occurred")


    def transfer(self, args):
        try: #11 wrapped with try statement to allow exceptions to raise properly
            fromAccountNumber = int(args[0])
            toAccountNumber = int(args[1])
            amount = int(args[2])

            if (amount > 10000): #6 added transfer amount limit
                raise TransferAmtLimitException
            
            if (self.session_transfers >= 3): #7 added transfer number limit
                raise TransferNumberLimitException

            account1 = self.accounts.get(fromAccountNumber) #13 added .get() to fix InvalidAccountNumberException
            account2 = self.accounts.get(toAccountNumber) #13

            if (not account1) or (not account2):
                raise InvalidAccountNumberException

            account1.withdraw(amount)
            account2.deposit(amount)
            self.session_transfers += 1
        except BankingException as e:
            message.print(e.message())
        except:
            message.print("An error occurred")