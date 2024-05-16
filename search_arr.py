import numpy as np
#positions of search element
a = np.array([18,20,22,25,34])
#x = np.where(a==18)
#print(x)
"""
#even values' indices
x = np.where(a%2 == 0)
print(x)

#odd values' indices
x = np.where(a%2 == 1)
print(x)

#searchsorted returns where to insert the element (default from lhs)
x = np.searchsorted(a,34)
print(x)
#searchsorted from rhs
x = np.searchsorted(a,34,side = 'right')
print(x)"""

#positions to insert multiple values
x = np.searchsorted(a,[24,21,10])
print(x)
