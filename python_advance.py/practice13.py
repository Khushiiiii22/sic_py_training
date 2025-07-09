'''import numpy as np

arr1 = np.arange(1, 10)     #arange always generates 1D array
arr2 = np.arange(2, 25, 2)
arr3 = arr1.reshape(3, -1)   #reshape generates 1D 2D and #d arrays and so on
arr4 = arr2.reshape(4, -1)
arr5 = arr2.reshape(2, -1)
arr6 = arr2.reshape(3, -1)
arr7 = arr2.reshape(-1, 4) # Numpy predicts and fixes number of rows
arr8 = arr2.reshape(-1, -1) #ValueError. Can only specify one unknown dimension

print('Arr1:\n', arr1)
print('Arr2:\n', arr2)
print('Arr3:\n', arr3)
print('Arr4:\n', arr4)
print('Arr5:\n', arr5)
print('Arr6:\n', arr6)
print('Arr7:\n', arr7)
print('Arr8:\n', arr8)'''



'''import numpy as np

array1 = np.array([1, 3, 5, 0, 2, 3, 4, 5, 13, 17, 23, 29])
print(array1.shape)
print(type(array1))
print(array1)'''



'''import numpy as np

array1 = np.array([1, 3, 5, 0, 2, 3, 4, 5, 13, 17, 23, 29])

array1.shape = (6, 2)
print(array1.shape)
print(array1)

array1.shape = (3, 4)
print(array1.shape)
print(array1)

array1.shape = (4, 3)
print(array1.shape)
print(array1)

#array1.shape = (4, 2) # Error New shape of the array must consist of same number of elements as that of original array
#print(array1.shape)
#print(array1)'''



'''import numpy as np

matrix1 = np.array([[3, 4, 5], [2, 6, 9]])
matrix2 = np.array([[3, 4], [3, 5], [2, 6]])

matrix3 = np.dot(matrix1, matrix2)

print('Matrix3=\n', matrix3)'''

