while True:
    print("welcome to simple calculator")
    print("1 is for addition")
    print("2 is for subtraction")
    print("3 is for multiplication")
    print("4 is for division")
    print("5 for square root")
    print("6 is for exit")

    i=int(input("enter your choice: "))

    if(i==1):
        a=int(input("enter the value of a: "))
        b=int(input("enter the value of b: "))
        print("sum is", a+b)
    elif(i==2):
        a=int(input("enter the value of a: "))
        b=int(input("enter the value of b: "))
        print("subtraction is", a-b)
    elif(i==3):
        a=int(input("enter the value of a: "))
        b=int(input("enter the value of b: "))
        print("multiplication is", a*b)
    elif(i==4):
        a=int(input("enter the value of a: "))
        b=int(input("enter the value of b: "))
        print("division is", a/b)
    elif(i==5):
        a=int(input("enter the value of a: "))
        print("square root is", a**0.5)
    elif(i==6):
        break
    else:
        print("invalid choice")