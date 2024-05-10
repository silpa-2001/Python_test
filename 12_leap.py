y=int(input("Enter a year"))

if y%4==0 and y%100!=0:
    print("Is a leap year")
elif y%400==0 and y%100==0:
    print("Is a leap year")
else:
    print("Not a leap year")






