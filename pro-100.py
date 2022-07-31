class atm:
    def __init__ (self, pinNumber ):
        self.pinNumber = pinNumber

    def withdraw(self):
        print("Cash Withrawn")

    def deposit(self):
        print("Cash Deposited")


myAtm = atm(1234)

myAtm.withdraw()
myAtm.deposit()


