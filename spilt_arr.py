import numpy as np

#a=np.array([1,2,3,4,5,6,7,8])
a= np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
#newarr=np.array_split(a,3)
#print(newarr)
newarr=np.hsplit(a,3)
print(newarr[0])
print(newarr[1])
print(newarr[2])