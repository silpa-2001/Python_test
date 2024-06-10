
n=int(input("Enter a number: "))
s=n*2//2
e=s-1
for i in range(n):
    for j in range(n*2):
        if j in range(s,e):
            print("*",end="")
        else:
            print(" ",end="")
    s=s-1
    e=e+1
    print()