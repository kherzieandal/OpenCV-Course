import numpy as np
list1 = [0,1,2,3,4,5,6,7,8]
matrix = np.array([list1[:3],list1[3:6],list1[6:]],dtype=float)
print(matrix)

print([array.mean() for array in matrix.T])