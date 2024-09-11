class BankingExcpetion(Exception):
    pass

class InsufficientFundsException(BankingExcpetion):
    def message(self):
        return 'An error occurred: Insufficent Funds'

class InvalidAccountNumberException(BankingExcpetion):
    def message(self):
        return "An error occurred: Invalid Account Number"
    
class TransferAmtLimitException(BankingExcpetion):
    def message(self):
        return "An error occured: Amount Limit of 10000 Per Transfer Exceeded"

class TransferNumberLimitException(BankingExcpetion):
    def message(self):
        return "An error occured: Transfer Limit of 3 Transfers Per Session Exceeded"