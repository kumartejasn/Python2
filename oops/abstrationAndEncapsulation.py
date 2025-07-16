# #abstracting
# #hiding the implementation details

# class Vehicle:
#     def __init__(self):
#         self.clutch=False
#         self.acc=False
#         self.brk=False

#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("vehicle started")

#     def stop(self):
#         self.clutch=False
#         self.acc=False
#         self.brk=True
#         print("vehicle stopped")

# v=Vehicle()
# v.start()  # starts the vehicle
# v.stop()  # stops the vehicle


# class Account:
#     def __init__(self,balance, accountNumber):
#         self.balance=balance
#         self.accountNumber=accountNumber

#     def debit(self,amount):
#         self.balance-=amount
#         print(f"debitinf {amount} from account {self.accountNumber} and the new balance is {self.balance}")
    
#     def credit(self,amount):
#         self.balance+=amount
#         print(f"crediting {amount} to account {self.accountNumber} and the new balance is {self.balance}")
    
#     def balanceAmount(self):
#         return self.balance

# a=Account(1100000, 1454154)
# print(a.debit(100000))  # debits 100000 from the account
# print(a.credit(1))  # credits 100000 to the account
# print(a.balanceAmount())


# #private attributes
# # Private attributes are attributes that cannot be accessed from outside the class.

# class Account:
#     def __init__(self, user,password):
#         self.user=user
#         self.__password=password # two underscores before the attribute name make it private
        
#     def login(self):
#         print(f"User {self.user} logged in with password {self.__password}")
#         # here u can access the private attribute __password because it is within the class

# a=Account("tgrsd",45125)
# print(a.login())  # this will print "User tgrsd logged in with password 45125" because login method is within the class
# print(a.user, a.__password)  # this will raise an error because __password is private




#private methods
# Private methods are methods that cannot be accessed from outside the class.


class Phone:
    def __init__(self,os,company):
        self.__os=os
        self.company=company
    
    def __phoneDetailes(self):
        print(f"the phone is {self.company} and the os is {self.__os}")

    def samsung(self):
        self.__phoneDetailes()  

p=Phone("android","samsung")
print(p.samsung())

