def find_hcf(x, y):
    while(y):
        x, y = y, x % y
    return x

def find_gcd(x, y):
    gcd = 1
    for i in range(1, min(x, y) + 1):
        if x % i == 0 and y % i == 0:
            gcd = i
    return gcd

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print("The HCF of", num1, "and", num2, "is:", find_hcf(num1, num2))
print("The GCD of", num1, "and", num2, "is:", find_gcd(num1, num2))
