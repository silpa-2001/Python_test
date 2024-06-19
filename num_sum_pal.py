def rev_num(n):
    rev=0
    n=num
    while n!=0:
        rev=rev*10+n%10
        n//=10
    sum=num+rev
    srev=0
    s=sum
    while s!=0:
        srev=srev*10+s%10
        s//=10
    
    if srev==sum:
        print("The sum",srev,"of the number and its reverse is a palindrome")
    else:
        rev_num(sum)
    return srev

num=int(input("Enter a number: "))
rev_num(num)