


# class Device:
#     def contactSaving(self, a, b):
#         print(a, b)

# class Phone(Device):
#     def contactSaving(self, a, b):
#         print(a, b)

# class SmartPhone(Phone):
#     def contactSaving(self, a, b):
#         print(a, b)
#         Phone.contactSaving(self, a, b)
#         Device.contactSaving(self, a, b)


# mobile = SmartPhone()
# mobile.contactSaving("tejas", "8310361634")






# class Device:
#     def contactSaving(self, a, b):
#         print(a, b)

# class Phone(Device):
#     def contactSaving(self, a, b):
#         print(a, b)

# class SmartPhone(Phone):
#     def contactSaving(self, a, b):
#         print(a, b)
#         Phone.contactSaving(self, a, b)
#         Device.contactSaving(self, a, b)


# try:
#     mobile = SmartPhone()
#     mobile.contactSaving("tejas", "8310361634")
# except Exception as e:
#     print("error:", e)
# finally:
#     print("Program executed.")







# class Device:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def contactSaving(self, a, b):
#         print(self.a, self.b)

# class Phone(Device):
#     def __init__(self, a, b):
#         super().__init__(a, b)

#     def contactSaving(self, a, b):
#         print(self.a, self.b)

# class SmartPhone(Phone):
#     def __init__(self, a, b):
#         super().__init__(a, b)

#     def contactSaving(self, a, b):
#         print(a, b)
#         print(self.a, self.b)
#         super().contactSaving(a, b)
#         Device.contactSaving(self, a, b)


# try:
#     mobile = SmartPhone("tejas", "8310361634")
#     mobile.contactSaving("teja", "4528654452")
# except Exception as e:
#     print("An error occurred:", e)
# finally:
#     print("Program execution completed.")





