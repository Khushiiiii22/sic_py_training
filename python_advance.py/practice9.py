import numpy as np

vector = np.arange(5) #1D array
print('Vector shape:', vector.shape)

matrix = np.ones([3, 2]) #2D array
print('Matrix:', matrix)
print('Matrix shape:', matrix.shape)

tensor = np.zeros([2, 3, 3]) #3D array
print('Tensor:', tensor)
print("Tensor shape:", tensor.shape)

#matix stack upon another is tensor