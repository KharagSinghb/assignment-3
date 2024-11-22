# the start
class Account:
    def getAccountNumber(self):
        self.accNumber

    def getAccountHolderName(self):
        self.accName

    def getRateOfInterest(self):
        self.rateInterest

    def GetCurrentBalance(self):
        self.theBalance

    def _init_(self,account_number,account_name,rate_interest,current_balance):

        self.accNumber = account_number
        self.accName = account_name
        self.rateInterest = rate_interest
        self.theBalance = current_balance

    def setRateofInterest(self,rate):
        self.rateInterest = rate

    def setAccountHolderName(self,name):
        self.accName = name

class ChequingAccount(Account):
    def _init_(self,account_number,account_name,rate_interest,current_balance, overdraft_limit):
        super()._init_(account_number,account_name,rate_interest,current_balance)
        self.overdraftLimit = overdraft_limit

    

