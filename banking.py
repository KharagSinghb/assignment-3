# the start
class Account:
    def __init__(self, account_number, account_name, rate_interest, current_balance):
        self.accNumber = account_number
        self.accName = account_name
        self.rateInterest = rate_interest
        self.theBalance = current_balance

    def getAccountNumber(self):
        return self.accNumber

    def getAccountHolderName(self):
        return self.accName

    def getRateOfInterest(self):
        return self.rateInterest

    def getCurrentBalance(self):
        return self.theBalance

    def setRateofInterest(self, rate):
        self.rateInterest = rate

    def setAccountHolderName(self, name):
        self.accName = name

    def deposit(self, amount):
        if amount > 0:
            self.theBalance += amount
            print(f"Deposited {amount}. New balance is {self.theBalance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount > self.theBalance:
            print("Insufficient balance for withdrawal")
        else:
            self.theBalance -= amount
            print(f"Withdrawn {amount}. New balance is {self.theBalance}")


class ChequingAccount(Account):
    def __init__(self, account_number, account_name, rate_interest, current_balance, overdraft_limit):
        super().__init__(account_number, account_name, rate_interest, current_balance)
        self.overdraftLimit = overdraft_limit

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif self.theBalance - amount < -self.overdraftLimit:
            print("Withdraw denied. Overdraft limit exceeded.")
        else:
            self.theBalance -= amount
            print(f"Withdrawn {amount}. New balance is {self.theBalance}")


class SavingsAccount(Account):
    def __init__(self, account_number, account_name, rate_interest, current_balance, minimum_balance):
        super().__init__(account_number, account_name, rate_interest, current_balance)
        self.minimumBalance = minimum_balance

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid amount")
        elif self.theBalance - amount < self.minimumBalance:
            print("Withdrawal denied. Minimum balance requirement not met.")
        else:
            self.theBalance -= amount
            print(f"Withdrawn {amount}. New balance is {self.theBalance}")


class Bank:
    def __init__(self, bank_name):
        self.bankName = bank_name
        self.accounts = []

    def openAccount(self, account):
        self.accounts.append(account)
        print(f"Account opened for {account.getAccountHolderName()}")

    def searchAccount(self, account_number):
        for account in self.accounts:
            if account.getAccountNumber() == account_number:
                return account
        print("Account not found")
        return None


class Application:
    def run(self):
        bank = Bank("TD Bank")
        while True:
            self.showMainMenu(bank)

    def showMainMenu(self, bank):
        print("\n===== Main Menu =====")
        print("1. Open Account")
        print("2. Search Account")
        print("3. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            self.openAccount(bank)
        elif choice == "2":
            self.showAccountMenu(bank)
        elif choice == "3":
            print("Exiting the application.")
            exit()
        else:
            print("Invalid choice. Please try again.")

    def openAccount(self, bank):
        account_type = input("Enter account type (savings/chequing): ").lower()
        account_number = input("Enter account number: ")
        account_holder_name = input("Enter account holder name: ")
        rate_of_interest = float(input("Enter rate of interest: "))
        current_balance = float(input("Enter current balance: "))

        if account_type == "savings":
            minimum_balance = float(input("Enter minimum balance: "))
            account = SavingsAccount(account_number, account_holder_name, rate_of_interest, current_balance, minimum_balance)
        elif account_type == "chequing":
            overdraft_limit = float(input("Enter overdraft limit: "))
            account = ChequingAccount(account_number, account_holder_name, rate_of_interest, current_balance, overdraft_limit)
        else:
            print("Invalid account type. Account not created.")
            return

        bank.openAccount(account)

    def showAccountMenu(self, bank):
        account_number = input("Enter account number: ")
        account = bank.searchAccount(account_number)

        if account:
            print("\n===== Account Menu =====")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. View Balance")
            choice = input("Enter choice: ")

            if choice == "1":
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            elif choice == "3":
                print(f"Current balance: {account.getCurrentBalance()}")
            else:
                print("Invalid choice. Returning to main menu.")
        else:
            print("Account not found.")


# Run the application
if __name__ == "__main__":
    app = Application()
    app.run()