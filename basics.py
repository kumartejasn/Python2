# print("hello world")
# x=2
# x+=3
# print(x)

# a=int(input("Enter a number:"))
# print(x+a)
# y=4

# # type cast y to string and concatenate with name\

# c=str(y)
# name="tejas"
# print(c)
# print(name+c)


# v="4"  # here v is a string

# # type cast v to integer and add to x
# c=int(v)

# print(x+c) # this will add the integer value of v to x


# a=int(input("enter a intiger: "))
# b=int(input("enter another intiger: "))
# c=(a+b)/2
# print("average of two intigers is",c)


# radius of a cricle
radius = float(input("enter the radius value: "))
area=(22/7) * (radius**2)
print(area)
circum=2*(22/7)*radius
print(circum)


number=int(input("enter the number: "))

if(number%5==0 and number%7==0):
    print("the number is multiple of both 5 and 7")
else:
    print("the number is not the multiple of both 5 and 7")