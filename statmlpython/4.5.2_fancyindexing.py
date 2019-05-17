# Fancy indexing returns a copy not a view.

from __future__ import print_function
import numpy as np

# run code 4.5_selection

# Integer array indexing
arr2 = arr[:, [1, 2, 3]]        # return a copy
print(arr2)
arr2[0, 0] = 44                 # replaces element 1 with 44
print(arr2)
print(arr)


# Boolean arrays indexing
arr2 = arr[arr > 5]             # return a copy
print(arr2)
arr2[0] = 44                    # replaces element 6 with 44
print(arr2)
print(arr)


# However, in the context of lvalue indexing (left hand side value
# of an assignment) Fancy authorizes the modification of the original array

arr[arr > 5] = 0
   

# Boolean arrays indexing continues
names = np.array(['Bob', 'Joe', 'Will', 'Bob'])
names == 'Bob'                          # returns a boolean array
names[names != 'Bob']                   # logical selection, returns an array not equal to Bob
(names == 'Bob') | (names == 'Will')    # keywords and/or don't work with boolean arrays
names[names != 'Bob'] = 'Joe'           # assign based on a logical selection, 'Will 'replaces with 'Joe'
np.unique(names)                        # set function