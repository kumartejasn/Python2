
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
#The @property decorator in Python is used to define a method as a property, allowing you to access it like an attribute while still being able to define custom behavior for getting and setting its value.
#This is useful for encapsulating data and providing a clean interface for accessing attributes.
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


