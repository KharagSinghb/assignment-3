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

    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid amount")
        elif self.theBalance - amount < -self.overdraftLimit:
            print("Withdraw denied. Overdraft limit exceeded")
        else:
            self.theBalance -= amount
            print(f"Withdrawn {amount}. New balance is {self.theBalance}")


class SavingsAccount(Account):
    def _init_(self, account_number, account_name, rate_interest, current_balance, minimum_balance):
        super()._init_(account_number, account_name, rate_interest, current_balance)
        self.minimumBalance = minimum_balance

    def withdraw(self,amount):
        if amount <=0:
            print("Invalid amount")
        elif self.theBalance - amount < self.minimumBalance:
            print("Denied, you dont have enough money")
        else:
            self.theBalance -= amount
            print(f"withdrawn {amount}. New balance is {self.theBalance}")


class Bank:
    def _init_(self, bank_name):
        self.bankName = bank_name
        self.accounts = []

    def openAccount(self,account):
        self.accounts.append(account)
        print(f"Account opened for {account.getAccountHolderName()}")

    def searchAccount(self, account_number):
        for account in self.accounts:
            if account.getAccountNumber() == account_number:
                return account
            else :
                print("account not found")



        