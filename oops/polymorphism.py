#polymorphism
# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def showNumber(self):
#         print(self.real,"i +",self.img,"j")
    
#     def add(self,num2):
#         newReal=self.real + num2.real
#         newImg=self.img + num2.img
#         return Complex(newReal, newImg)

# num=Complex(4,5)
# num.showNumber() # prints "4 i + 5 j"

# num1=Complex(6,2)
# num1.showNumber()  # prints "6 i + 2 j"

# num3=num.add(num1)
# num3.showNumber()


# class Complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img
    
#     def showNumber(self):
#         print(self.real,"i +",self.img,"j")

#     def __add__(num1,num2):
#         newReal=num1.real+num2.real
#         newImg=num1.img + num2.img
#         return Complex(newReal,newImg)
    
# n1=Complex(4,2)
# n1.showNumber()
# n2=Complex(9,7)
# n2.showNumber()
# n4=Complex(1,1)
# n4.showNumber()
# n3=n1+n2+n4  # this will call the __add__ method
# n3.showNumber()


#__sub__ dunder method
class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    
    def showNumber(self):
        print(self.real,"i -",self.img,"j")
    
    def __sub__(num1,num2):
        newReal=num1.real-num2.real
        newImg=num1.img-num2.img
        return Complex(newReal,newImg)
    
n1=Complex(8,9)
n1.showNumber()
n2=Complex(5,6)
n2.showNumber()
n3=n1-n2
n3.showNumber()






class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return (22/7)*(self.radius**2)
    
    def parimeter(self):
        return (22/7)*2*self.radius

c=Circle(33)
print(c.area())
