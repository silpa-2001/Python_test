print("Operators:\n1.ADDITION\n2.SUBSTRACTION\n3.MULTIPLICATION\n4.DIVISION\n")
op=int(input("Choose an Operator(1/2/3/4): "))
if op==1:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    print(a+b)
elif op==2:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    print(a-b)
elif op==3:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    print(a*b)
elif op==4:
    a=int(input("Enter a number: "))
    b=int(input("Enter another number: "))
    if b==0:
        print("Division by zero not defined!")
    else:
        print(a/b)
else:
    print("Invalid Input")