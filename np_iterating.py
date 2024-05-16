import numpy as np

arr=np.array([[1,2,3,4],[2,3,4,5]])

"""for x in arr:
    for y in x:
        for z in y: 
            print(z)"""

#for x in np.nditer(arr,flags=['buffered'],op_dtypes=['S']):
#for x in np.nditer(arr[:,::2]):
for indx,x in np.ndenumerate(arr):
    print(indx,x)