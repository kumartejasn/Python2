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


# # radius of a cricle
# radius = float(input("enter the radius value: "))
# area=(22/7) * (radius**2)
# print(area)
# circum=2*(22/7)*radius
# print(circum)


# number=int(input("enter the number: "))

# if(number%5==0 and number%7==0):
#     print("the number is multiple of both 5 and 7")
# else:
#     print("the number is not the multiple of both 5 and 7")




# def find_roots(a, b, c):
#     if a == 0:
#         print("Error: Coefficient 'a' cannot be zero. This is not a quadratic equation.")
#         return

#     discriminant = (b**2) - (4 * a * c)

#     if discriminant >= 0:
#         root1 = (-b - (discriminant ** 0.5)) / (2 * a)
#         root2 = (-b + (discriminant ** 0.5)) / (2 * a)
        
#         print("\nThe roots of the equation are real.")
#         print(f"Root 1 = {root1}")
#         print(f"Root 2 = {root2}")
#     else:
#         print("\nThe roots of the equation are complex (imaginary).")

# if __name__ == "__main__":
#     print("Quadratic Equation Solver (Real Roots Only)")
#     print("Enter the coefficients for the equation ax^2 + bx + c = 0")

#     coeff_a = float(input("Enter coefficient a: "))
#     coeff_b = float(input("Enter coefficient b: "))
#     coeff_c = float(input("Enter coefficient c: "))

#     find_roots(coeff_a, coeff_b, coeff_c)



def fun1(a,b):
    result=a/b
    print(result)
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
fun1(a,b)