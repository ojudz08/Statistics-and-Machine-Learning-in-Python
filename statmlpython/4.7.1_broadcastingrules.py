# Broadasting is an implicit conversion to allow operations on arrays
# of different sizes. - The smaller array is stretched or "broadcasted"
# across the larger array so that they have compatible shapes. - Fast vectorized
# operation in C instead of Python. - No needless copies

from __future__ import print_function
import numpy as np


# RULES
# Starting with the trailing axis and working backward, Numpy compares arrays dimensions.
#    - If two dimensions are equal then continues
#    - If one of the operand has dimension 1 stretches it to match the largest one
#    - When one of the shapes runs out of dimensions (because it has less dimensions
#      than the other shape), Numpy will use 1 in the comparison process until the other
#      shape's dimension run out as well.

a = np.array([[ 0,  0,  0],
              [10, 10, 10],
              [20, 20, 20],
              [30, 30, 30]])

b = np.array([0, 1, 2])

print(a + b)


# Shapes of operands a, b and result
#   a       (2d array):   5 x 4
#   b       (1d array):       1
#   result  (2d array):   5 x 4
#
#   a       (2d array):   5 x 4
#   b       (1d array):       4
#   result  (2d array):   5 x 4
#
#   a       (3d array):   15 x 3 x 5
#   b       (3d array):   15 x 1 x 5
#   result  (3d array):   15 x 3 x 5
#
#   a       (3d array):   15 x 3 x 5
#   b       (2d array):        3 x 5
#   result  (3d array):   15 x 3 x 5
#
#   a       (3d array):   15 x 3 x 5
#   b       (2d array):        3 x 1
#   result  (3d array):   15 x 3 x 5
    