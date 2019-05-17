# Run the code one by one

arr = np.arange(10, dtype=float).reshape((2, 5))
print(arr.shape)
print(arr.reshape(5, 2))

# Add an axis
a = np.array([0, 1])
a_col = a[: np.newaxis]
print(a_col)
# or
a_col = a[: None]

# Transpose
print(a_col.T)

# Flatten: always return a flat copy of the original array
arr_flt = arr.flatten()
arr_flt[0] = 33
print(arr_flt)
print(arr)

# Ravel: returns a view of the original array whenever possible
arr_flt = arr.ravel()
arr_flt[0] = 33
print(arr_flt)
print(arr)