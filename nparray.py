import numpy as np
"""x = np.array([18,20,45,7])
print(x)
print(type(x))"""

#array dimensions
"""x1 = np.array(42) #0-D
x2 = np.array([1,2,3,4,5]) #1-D
x3 = np.array([[1,2,3],[4,5,6]]) #2-D
x4 = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]]) #3-D

print(np.ndim(x1))
print(np.ndim(x2))
print(np.ndim(x3))
print(np.ndim(x4))
"""
#higher dimensional
x2 = np.array([1,2,3,4,5], ndmin=5)
print(x2)
