
import numpy as np
from scipy import stats

array = np.array([[1, 1, 3, 3, 4, 4, 4, 5, 7, 7, 8, 9, 12]])

mean   = np.mean(array)
median = np.median(array)
mode   = stats.mode(array)

print(f'Mean = ', mean)
print(f'Median = ', median)
print(f'Mode Count = ', mode)