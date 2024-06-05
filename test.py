a=10
b=21.6
c=13+8j
print("the variable type is:",type(a))
print("the variable type is:",type(b))
print("the variable type is:",type(c))

first_name="Silpa"
middle_name="Chandrika"
last_name="Anil"
print("My name is",first_name,middle_name,last_name)
clist=["Red","Green","Yellow","Blue","Purple"]
nlist=[21,13,32,26,60]
flist=list(["Apple","Grapes","Mango","Berry"])
flist[0]="Pineapple"
flist.sort()
list1=flist.copy()
list1.append("Orange")
print(list1[::])
print(flist[::])
print(len(flist))
for i in clist:
    print(i,end=" ")
for i in nlist:
    print(i,end=" ")
for i in flist:
    print(i,end=" ")
print(type(clist))
print(type(nlist))
print(type(flist))

set1={1,2,3,4,5,6}
set2={"A","B","C","D",21,45,55,"B","32"}
print(set1)
print(set2)

import numpy as np

arr=np.array([1,2,3,4,5,6])
print(arr)