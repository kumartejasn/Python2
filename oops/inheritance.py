#inheritance
#inheritance is a way to form new classes using classes that have already been defined.
# It allows us to create a new class that inherits attributes and methods from an existing class.   
# The new class is called the derived class or child class, and the existing class is called the base class or parent class.

# class Car:
#     color="black"

#     def __init__(self,suv,sedan):
#         self.suv=suv
#         self.sedan=sedan
    
#     def sed(self):
#         print(f"{self.sedan} give smooth ride and has good maileage with a good speed")

#     def suv1(self):
#         print(f"{self.suv} is more used for off-road driving and has a good ground clearance")

# class Bmw(Car):
#     def __init__(self,comfort,speed):
#         self.comfort=comfort
#         self.speed=speed
    
#     def bmW(self):
#         print(f"BMW is a luxury car with {self.comfort} comfort and {self.speed} speed")

# c=Car("wrangler","M3")
# print(c.suv1())
# c1=Bmw("high", "fast")
# print(c1.suv1()) # this will not print self.suv or it does not have value assignes to self.suv and it will print remaining all the things inside the method



# class Animal:
#     @staticmethod

#     def tiger():
#         print("Tiger is a carnivore and it is a wild animal")

#     @staticmethod
#     def cow():
#         print("Cow is a herbivore and it is a domestic animal")

# class Carnivore(Animal):
#     def __init__(self,name):
#         self.name=name
    
#     def carnivore(self):
#         print(f"{Animal.tiger()} and {self.name} is a carnivore animal")

# c=Carnivore("tiger")
# print(c.carnivore())  # this will print "None and tiger is a carnivore animal"
# print(c.tiger())  # this will print "Tiger is a carnivore and it is a wild animal"
# print(c.cow())



# multilevel inheritance


class Animal:
    @staticmethod

    def tiger():
        print("Tiger is a carnivore and it is a wild animal")

    @staticmethod
    def cow():
        print("Cow is a herbivore and it is a domestic animal")

class Carnivore(Animal):
    def __init__(self,name):
        self.name=name
    
    def carnivore(self):
        print(f"{Animal.tiger()} and {self.name} is a carnivore animal")

class Mammal(Carnivore):
    def __init__(self,name):
        self.name1=name
    
    def cor(self):
        print(self.name1)
        super().tiger()

m=Mammal("lion")
print(m.cor())
print(m.tiger())



#Multiple inheritance
# a child class can inherit from multiple parent classes.

class A:
    varA="class A"

class B:
    varB="class B"

class C(A,B):
    varC="class C"

c=C()
print(c.varA)



#super()
#via super() we can call the parent class methods and attributes from the child class.

class Parent:
    def __init__(self):
        self.name = "Parent Class"

    def parent(self):
        print(f"parent name is A.")

class Child(Parent):
    def __init__(self,name):
        self.name=name
     
    def child(self):
        print(f"child name B.")
        super().parent()

ch=c=Child(B)
print(ch.child())




#classmethod
#A class method is a method that is bound to the class and not the instance of the class.
# It can be called on the class itself, rather than on instances of the class.  
# Class methods are defined using the @classmethod decorator and take a reference to the class as the first parameter, conventionally named cls.

class NewClass:
    var="hello"
    
    
    @classmethod

    def classMethod(cls,var):
        cls.var=var

cm=NewClass()
cm.classMethod("world")
print(cm.var)


class Newclass2:
    new1="vesfc"
    @classmethod
    def classMethod2(cls,new1):
        cls.new1=new1
    
nc=Newclass2()
print(nc.new1)
nc.classMethod2("hello")
print(nc.new1)


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    @classmethod
    def birthYear(cls,name,birthyear):
        age=2025-birthyear
        return cls(name,age)
    
p=Person("tejas",24)
p2=Person.birthYear("teja",2001)
print(p.name,p.age)
print(p2.name,p2.age)



#@property 
#The @property decorator in Python is used to define a method as a property, allowing you to access it like an attribute while still being able to define custom behavior for getting and setting its value. This is useful for encapsulating data and providing a clean interface for accessing attributes.
# It allows you to define methods that can be accessed like attributes, providing a way to control access to the underlying data

class Avg:
    def __init__(self,phy,math,chem):
        self.phy=phy
        self.math=math
        self.chem=chem
    
    @property 
    def percentage(self):
        return str((self.phy + self.math + self.chem)/3 ) + "%"

a=Avg(98,88,89)
print(a.percentage) 
a.phy=100
print(a.percentage)
