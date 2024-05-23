def find_fact(num):
    factors = []
    for x in range(1, num + 1):
        if num % x == 0:
            factors.append(x)
    return factors

num = int(input("Enter the number: "))
print("The factors of", num, "are:", find_fact(num))
