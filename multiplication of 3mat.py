import numpy as np

matrix1 = np.array([[1,1,1],[2,2,2],[3,3,3]])
matrix2 = np.array([[1,1,1],[2,2,2],[3,3,3]])
matrix3 = np.array([[1,1,1],[2,2,2],[3,3,3]])

result = matrix1 @ matrix2 @ matrix3 
print("Multiplication of the matrices:")
print(result)