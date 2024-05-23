

print("Choose:\n1.ADD\n2.SUBRACT\n3.MULTIPLE\n4.DIVIDE\n5.Exit\n")
while True:

    choice=int(input("Enter (1/2/3/4/5):"))

    if choice==5:
        print("You have exited from the program!")
        break

    if choice==1:
        x=int(input("Enter a number :"))
        y= int(input("Enter another number :"))   
        print(x+y)
        
    elif choice==2:
        x=int(input("Enter a number :"))
        y= int(input("Enter another number :"))   
        print(x-y)
        
    elif choice==3:
        x=int(input("Enter a number :"))
        y= int(input("Enter another number :"))   
        print(x*y)
        
    elif choice==4:
        x=int(input("Enter a number :"))
        y= int(input("Enter another number :"))
        if y==0:
            print("Error... Divison by zero not possible!")
        else:
            print(x/y)
    else:
        print("Invalid Input...")
            
    