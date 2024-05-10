n= int(input("Enter the start number:"))
n2= int(input("Enter the end number:"))
for i in range(n,n2):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
