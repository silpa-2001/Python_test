import numpy as np

arr=np.array([13,28,45,80])
"""bindx=[True,False,True,False]

newarr=arr[bindx]

print(newarr)

#Filter array
filtr_arr=[]

for ele in arr:
    #if ele>40:
    if ele%2==0: #for even elements in array
        filtr_arr.append(True)
    else:
        filtr_arr.append(False)
newarr=arr[filtr_arr]
print(newarr)"""

#filtr_arr=arr>40
filtr_arr=arr%2==0

new_arr=arr[filtr_arr]
print(new_arr)