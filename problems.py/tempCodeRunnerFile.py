
class Device:
    def contactSaving(self, a, b):
        print(a, b)

class Phone(Device):
    def contactSaving(self, a, b):
        print(a, b)

class SmartPhone(Phone):
    def contactSaving(self, a, b):
        print(a, b)
        Phone.contactSaving(self, a, b)
        Device.contactSaving(self, a, b)


try:
    mobile = SmartPhone()
    mobile.contactSaving("tejas", "8310361634")
except Exception as e:
    print("error:", e)
finally:
    print("Program executed.")