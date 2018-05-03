class BankAccount(object):
    def __init__(self):
        print("-------------------Begining of code--------------------")
        self.balance = 1000
        print("Account created")
        print("----------------------------------------")

    def deposit(self, amount):
        try:
            self.balance += amount
            print("Deposit successful, {} added to account".format(amount))
            print("Curent balance is {}".format(self.balance))
        except:
            print("")
        print("----------------------------------------")

    def withdraw(self, amount):
        self.balance -= amount
        print("Withdrawal successful, {} removed from account".format(amount))
        print("Current balance is {}".format(self.balance))
        print("----------------------------------------")

    def get_balance(self):
        print("Your balance is {}".format(self.balance))
        print("------------------end of code ------------------")

kcb_account = BankAccount()
kcb_account.deposit(10000)
kcb_account.withdraw(2000)
kcb_account.get_balance()


