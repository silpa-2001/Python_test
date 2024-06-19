sum=0
print("Numbers between 100 and 200 that are divisible by 7 are:")
for x in range(100,200):
    if x % 7 == 0:
        print(x,end=",")
        sum+=x

print("\nSum of numbers between 100 and 200 that are divisible by 7 is",sum)