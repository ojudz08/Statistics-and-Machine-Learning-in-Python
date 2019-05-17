from __future__ import print_function
import numpy as np

data1 = [1, 2, 3, 4, 5]             # list
arr1 = np.array(data1)              # 1D array
data2 = [range(1, 5), range(5, 9)]  # list of lists
arr2 = np.array(data2)              # 2D array
arr2.tolist()                       # convert array back to list

           
# Create special arrays
np.zeros(10)
np.zeros((3, 6))
np.ones(10)
np.linspace(0, 1, 5)                # 0 to 1 (inclusive) wiht 5 points
np.logspace(0, 3, 4)                # 10^0 to 10^3 (inclusive) with 4 points


# arrange is like range, except it returns an array (not a list)
int_array = np.array(5)
float_array = int_array.astype(float)