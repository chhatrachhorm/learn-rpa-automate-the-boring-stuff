from __future__ import print_function
import numpy as np

# create nd-array from lists

data1 = [1, 2, 3, 4, 5]
arr1 = np.array(data1)  # 1D array

data2 = [range(1, 10), range(20, 30)]  # list of lists
arr2 = np.array(data2)  # 2D array

# from array => list
back_list = arr2.tolist()

# property
print(arr1.dtype, arr1.ndim, arr1.shape, arr1.size, len(arr1))