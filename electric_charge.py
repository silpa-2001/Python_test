rate=int(input("Enter the consumption unit: "))

if rate in range(0,200):
    amt=rate*0.50
    print("Amount to pay for the electric bill is: Rs.",amt)
elif rate in range(201,400):
    amt=rate*0.65
    print("Amount to pay for the electric bill is: Rs.",amt)
elif rate in range(401,600):
    amt=rate*0.80
    print("Amount to pay for the electric bill is: Rs.",amt)
else:
    amt=rate*1.00
    print("Amount to pay for the electric bill is: Rs.",amt)

if amt>400:
    amt=amt+rate*0.15
    print("Amount to pay for the electric bill including surcharge is: Rs.",amt)

if amt<100:
    print("Amount to pay for the electric bill is: Rs.100")