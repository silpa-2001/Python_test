sel=input("do you want a set of numbers or alphabets(N/A)?: ")
if sel.upper()=="N":
    n=int(input("Enter the number of elements: "))
    s=set()
    for i in range(n):
        s.add(int(input("Enter element {}: ".format(i+1))))
    print("The set is: ",s)
    n=int(input("Enter the number of elements for second set: "))
    s2=set()
    for i in range(n):
        s2.add(int(input("Enter element {}: ".format(i+1))))
    print("The set is: ",s2)
    while True:
        print("1.Set Union\n2.Set Intersection\n3.Set Difference\n4.Exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
            print("The union of the two sets is: ",s.union(s2))
        elif ch==2:
            print("The intersection of the two sets is: ",s.intersection(s2))
        elif ch==3:
            print("The difference of the two sets is: ",s.difference(s2))
        elif ch==4:
            break
        else:
            print("Invalid choice...")
elif sel.upper()=="A":
    n=int(input("Enter the number of elements: "))
    s=set()
    for i in range(n):
        s.add(input("Enter element {}: ".format(i+1)))
    print("The set is: ",s)
    n=int(input("Enter the number of elements for second set: "))
    s2=set()
    for i in range(n):
        s2.add(input("Enter element {}: ".format(i+1)))
    print("The set is: ",s2)
    while True:
        print("1.Set Union\n2.Set Intersection\n3.Set Difference\n4.Exit")
        ch=int(input("Enter your choice: "))
        if ch==1:
            print("The union of the two sets is: ",s.union(s2))
        elif ch==2:
            print("The intersection of the two sets is: ",s.intersection(s2))
        elif ch==3:
            print("The difference of the two sets is: ",s.difference(s2))
        elif ch==4:
            break
        else:
            print("Invalid choice...")
else:
    print("Invalid selection...")