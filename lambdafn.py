"""x = lambda a:a+8
print(x(10))

y = lambda a,b,c:a*b+c
print(y(2,4,10))"""

def fn(n):
    return lambda a:a*n
b = fn(5)#parameter
print(b(8))#argument
