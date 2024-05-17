import numpy as np

#arr=np.array([[1,2,3,4],[5,6,7,8]])
#arr=np.array([1,2,3,4],ndmin=5)
arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#rarr=arr.reshape(2,6)
#rarr=arr.reshape(2,3,2)
#rarr=arr.reshape(2,2,-1) #unknown dim
rarr=arr.reshape(-1) #flattening

#print(rarr.base)
print(rarr)