'''# Create a checkerboard 8x8 matrix using the tile function 
import numpy as np

#my_matrix = np.array([[0,1],[1,0]])
#print(my_matrix)

chess_board = np.tile( np.array([[1, 0],[0, 1]]), (4,4))
# chess_board = np.tile( np.array([['*', ' '],[' ', '*']]), (4,4))
#print('\n', chess_board)

list1 = []
for array in chess_board:
    list1 = list(array)
    string = ' '.join(map(str, list1))
    print(string)'''




    # Normalize a 5x5 random matrix
import numpy as np

my_array = np.random.random((5,5))
#print(my_array)

values = my_array - np.mean (my_array)
print('\n', values)

values = np.std (my_array)
print('\n', values)

my_array = (my_array - np.mean (my_array)) / (np.std (my_array))
print(my_array)