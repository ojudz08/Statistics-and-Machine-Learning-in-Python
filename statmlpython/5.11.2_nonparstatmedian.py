# Based on non-parametric statistics: use the median

# Median absolute deviation (MAD), based on the medium, is a robust non-parametric
# statistics. 

mad = 1.4826 * np.median(np.abs(size - size.median()))
size_outlr_mad = size.copy()

size_outlr_mad[((size - size.median()).abs() > 3 * mad)] = size.median()
print(size_outlr_mad.mean(), size_outlr_mad.median())