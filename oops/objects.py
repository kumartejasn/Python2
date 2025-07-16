# class Students:
#     school="venu"
#     location="srinivaspur"

# s1=Students()
# print(s1.school)  # this will raise an error because name is not defined in the class
# print(s1.location)  # this will print "srinivaspur"

# class Students:
#     collegeName="vijaya"

#     def __init__(self, fullname, location):
#         self.name=fullname
#         self.loc=location

# s1=Students("tejas kumar", "Kamalavaripalli")
# print(s1.name, s1.loc)
# print(s1.collegeName)  # this will print "vijaya"
# s2=Students("dhoni","srinivaspur")
# print(s2.name, s2.loc)  # this will print "dhoni srinivaspur"
# print(Students.collegeName)


# class Cars:
#     company="BMW"
#     def __init__(self,model,color,country):
#         self.model=model
#         self.colour=color
#         self.country=country
    
#     def owners(self,owned):
#         print(f"the owner of {self.model} is {owned} and the colour is {self.colour} and his country is {self.country} ")

# c1=Cars("M4 CS","Black","India")
# print(c1.company)  # this will print "BMW"
# print(Cars.company)  # this will also print "BMW"
# c1.owners("dhoni")  # this will print the owner details
# print(c1.model, c1.colour, c1.country)  # this will print the model, colour and country of the car



# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
    
#     def average(self):
#         sum=0
#         for val in self.marks:
#             sum += val

#         print(f"{self.name} has an average of {sum/3} marks")

# s1=Student("tribhu",[99,90,98])
# print(s1.average())


#Static methods
# Static methods are methods that belong to the class rather than an instance of the class.
# They do not require an instance to be called and can be called directly on the class.
# Static methods are defined using the @staticmethod decorator.


class Person:
    @staticmethod
    def person(name,age):
        print(f"Name:{name}, Age:{age}")

p1=Person()
print(p1.person("tejas", 24) ) # this will print "Name:tejas, Age:24"


class Education:
    @staticmethod
    def college(collegeName,location):
        print(f"collegeName:{collegeName}, location:{location}")

e=Education()
print(e.college("east point","bengaluru"))  # this will print "collegeName:east point, location: bengaluru" 


#del 
# The del statement is used to delete an object or a variable.
# It can be used to delete an entire object or a specific attribute of an object.

class LivingBeing:
    def __init__(self,name,kingdom):
        self.name=name
        self.kingdom=kingdom
    
    def details(self):
        print(f"name:{self.name},kingdom:{self.kingdom}")

l=LivingBeing("human","animalia")
print(l.details())  # this will print "name:human, kingdom:animalia"
del l.name  # this will delete the name attribute of the object l
print(l.details())  # this will raise an error because name attribute is deleted