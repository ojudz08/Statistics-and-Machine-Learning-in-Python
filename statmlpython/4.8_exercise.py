from __future__ import print_function
import numpy as np

# For each column find the row index of the minimum value.
# Write a function standardize(X) that return an array whose columns are centered and scaled (by std-dev)

X = np.random.randn(4, 2)       # random normals 4 x 2


# My answer below
X.argmin()              # finds the row index of minimum value