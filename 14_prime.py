n= int(input("Enter a number: "))
f=0
if n==1:
    print("Not prime number")
else:
    for i in range(2,n):
        if n%i==0:
            f=1
    if f==0:
        print("Prime number")
    else:
        print("Not prime number")

    
        

