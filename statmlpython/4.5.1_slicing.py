# Slicing

# Syntax: start:stop:step with start(default) stop(default last) step(default 1)

from __future__ import print_function
import numpy as np

arr[0, :]       # row 0: returns 1d array ([0, 1, 2, 3, 4])
arr[:, 0]       # column 0: returns 1d array ([0, 5])
arr[:, :2]      # coluns before index 2 (first 2 columns)
arr[:, 2:]      # columns after index 2 included
arr2 = arr[:, 1:4]  # columns between index 1 (included) and 4(excluded)
print(arr2)


# Slicing returns a view (not a copy)
arr2[0, 0] = 33
print(arr2)
print(arr)

# Row 0: reverse order
print(arr[0, ::-1])

# The rule of thumb here can be: in the context of 1value indexing (i.e the 
# indices are placed in the left hand side value of an assignment), no view
# or copy of the array is created (because there is no need to). However, with
# regular values, the above rules for creating views does apply.
