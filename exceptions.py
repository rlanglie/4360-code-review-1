class BankingException(Exception): #10 spelling error
    pass

class InsufficientFundsException(BankingException):
    def message(self):
        return 'An error occurred: Insufficent Funds'

class InvalidAccountNumberException(BankingException):
    def message(self):
        return "An error occurred: Invalid Account Number"
    
class TransferAmtLimitException(BankingException):
    def message(self):
        return "An error occured: Amount Limit of 10000 Per Transfer Exceeded"

class TransferNumberLimitException(BankingException):
    def message(self):
        return "An error occured: Transfer Limit of 3 Transfers Per Session Exceeded"

class LoginAttemptAmtException(BankingException):
    def message(self):
        return "An error occured: Too Many Login Attempts"
class PositiveAmountException(BankingException):
    def message(self):
        return "An error occured: Deposit Must Be a Positive Value"