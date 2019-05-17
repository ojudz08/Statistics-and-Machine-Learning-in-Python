from __future__ import print_function
import numpy as np

nums = np.arange(5)
nums * 10                   # multiply each element by 10
nums = np.sqrt(nums)        # square root of each element
np.ceil(nums)               # also floor, rint (round to nearest int)
np.isnan(nums)              # checks for NaN
nums + np.arange(5)         # add element-wise
np.maximum(nums, np.array([1, -2, 3, -4, 5]))   # compare element-wise, returns the max value between two arrays


# Compute Euclidean distance between 2 vectors
vec1 = np.random.randn(10)
vec2 = np.random.randn(10)
dist = np.sqrt(np.sum(vec1 - vec1) ** 2)        # returns 0.0


# math and stats
rnd = np.random.randn(4, 2) # random normals in 4x2 array
rnd.mean()
rnd.std()
rnd.argmin()                # index of minimum element
rnd.sum()                     
rnd.sum(axis=0)             # sum of columns
rnd.sum(axis=1)             # sum of rows

       
# methods for boolean arrays
(rnd > 0).sum()             # counts number of positive values
(rnd > 0).any()             # checks if any value is True
(rnd > 0).all()             # checks if all values are True


# random numbers
np.random.seed(12234)       # Set the seed
np.random.rand(2, 3)        # 2x3 matrix in [0, 1]
np.random.randn(10)         # 10 randomly picked 0 or 1
np.random.randn(0, 2, 10)   # random normals (mean 0, sd 1) 