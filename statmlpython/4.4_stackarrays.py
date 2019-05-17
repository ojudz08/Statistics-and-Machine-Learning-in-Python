# Stack flat arrays in columns

from __future__ import print_function
import numpy as np

a = np.array([0, 1])
b = np.array([2, 3])

ab = np.stack((a, b)).T
# or
np.hstack((a[:, None], b[:, None]))

print(ab)