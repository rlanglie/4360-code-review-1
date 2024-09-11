from message import Message
from exceptions import BankingExcpetion, InvalidAccountNumberException


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
        except BankingExcpetion as e:
            message.print(e.message())
        except:
            message.print("An error occurred")

    def withdraw(self, args):
        try:
            accountNumber = int(args[0])
            amount = int(args[1])
            account = self.accounts[accountNumber]

            if not account:
                raise InvalidAccountNumberException

            account.withdraw(amount)
            return account.check_balance()
        except BankingExcpetion as e:
            message.print(e.message())
        except:
            message.print("An error occurred")


    def transfer(self, args):
        fromAccountNumber = int(args[0])
        toAccountNumber = int(args[1])
        amount = int(args[2])

        if (amount > 10000): #6 added transfer amount limit
            raise TransferAmtLimitException
        
        if (self.session_transfers >= 3): #7 added transfer number limit
            raise TransferNumberLimitException

        account1 = self.accounts[fromAccountNumber]
        account2 = self.accounts[toAccountNumber]

        if not account1 or not account2:
            raise InvalidAccountNumberException

        account1.withdraw(amount)
        account2.deposit(amount)
        self.session_transfers += 1