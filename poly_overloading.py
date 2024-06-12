from multipledispatch import dispatch

@dispatch(int,int)
def product(a,b):
    print(a*b)

@dispatch(float,float,float)
def product(a,b,c):
    print(a*b*c)

product(2,3)
product(5.0,4.2,7.1)