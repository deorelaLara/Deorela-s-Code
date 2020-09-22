import numpy as np

a = [[11,2,4],[4,5,6],[10,8,-12]]
b = np.asarray(a)
#print(a)
print(b)
print('Diagonal (sum): ' , np.trace(b))
print('Diagonal (elements): ', np.diagonal(b))

"""
    11  2  4
    4   5  6
    10  8 -12
"""