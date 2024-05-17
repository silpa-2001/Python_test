import numpy as np

arr=np.array([1,2,3,4])
#x=arr.copy()
x=arr.view()
arr[0]=7

print(arr)
print(arr.base)
print(x)
print(x.base)
