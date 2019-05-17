# Selection: Single item

from __future__ import print_function
import numpy as np

arr = np.arange(10, dtype=float).reshape((2,5))

arr[0]      # 0th element (slices like a list), returns the first row of elements
arr[0, 3]   # row 0, column 3, returns 3.0
arr[0][3]   # same result as above, alternative syntax