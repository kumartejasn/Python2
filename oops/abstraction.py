#abstracting
#hiding the implementation details

class Vehicle:
    def __init__(self):
        self.clutch=False
        self.acc=False
        self.brk=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("vehicle started")

    def stop(self):
        self.clutch=False
        self.acc=False
        self.brk=True
        print("vehicle stopped")

v=Vehicle()
v.start()  # starts the vehicle
v.stop()  # stops the vehicle


class Account:
    def __init__(self,balance, accountNumber):
        self.balance=balance
        self.accountNumber=accountNumber

    def debit(self,amount):
        self.balance-=amount
        print(f"debitinf {amount} from account {self.accountNumber} and the new balance is {self.balance}")
    
    def credit(self,amount):
        self.balance+=amount
        print(f"crediting {amount} to account {self.accountNumber} and the new balance is {self.balance}")
    
    def balanceAmount(self):
        return self.balance

a=Account(1100000, 1454154)
print(a.debit(100000))  # debits 100000 from the account
print(a.credit(1))  # credits 100000 to the account
print(a.balanceAmount())



