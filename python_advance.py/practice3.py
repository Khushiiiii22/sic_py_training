import numpy as np

array1 = np.zeros(3)
print(f'Array1 = {array1}') # 1d array of 3 zeros

array2 = np.zeros((1,4))
print(f'Array2 = {array2}') #2d array of 1, 1d array of 4 zeros

array3 = np.zeros((2,5))
print(f'Array3 = {array3}')

print(type(array1))
print(type(array1[0]))