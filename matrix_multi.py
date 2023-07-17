import numpy as np

matrix1 = np.array([1,2,3,4,5,6,7,8,9]) 
matrix2 = np.array([1,2,3,4,5,6,7,8,9])

matrix1 = matrix1.reshape(3,3)
matrix2 = matrix2.reshape(3,3)

result = np.dot(matrix1,matrix2) # or matrix1 @ matrix2 gives same answer

print(result)