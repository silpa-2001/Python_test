def find_gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

def find_lcm(x, y):
    lcm = (x*y) // find_gcd(x, y)
    return lcm

num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))

print("The LCM of", num1, "and", num2, "is:", find_lcm(num1, num2))
