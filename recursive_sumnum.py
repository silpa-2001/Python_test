def rec_sum(n):
    if n == 0:
        return 0
    else:
        return n+rec_sum(n-1)
    
sum=rec_sum(10)
print("Sum of numbers from 0 to 10 is",sum)