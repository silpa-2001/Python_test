fact={}
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        if n in fact:
            return fact[n]
        else:
            fact[n]=n*factorial(n-1)
    return fact[n]

n=int(input("Enter the number to find the factorial: "))
print("The factorial of",n,"is",factorial(n))
print("calculated factorial: ",fact)