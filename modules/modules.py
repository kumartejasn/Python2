from math import pi # importing pi from math module
def area(r):
    return pi *( r**2)

def circum(r):
    return 2*pi*r
r=int(input("Enter the radius of the circle: "))
print(circum(r))
print(area(r))
print(pi)  # prints the value of pi


# some examples of math module

import math
x=2.3
y1=4
y2=2
print(math.ceil(x))
print(math.floor(x))
print(math.sqrt(y1))
print(math.pow(y1,y2))  # y1 raised to the power of y2


def fib(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
print(fib(10))

