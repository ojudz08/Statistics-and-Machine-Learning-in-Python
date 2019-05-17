# Run 5.11

# Based on parametric statistics: use the mean

# Assume random variable follows the normal distribution Exclude data outside
# 3 standard-deviations: - Probability that a sample lies within 1 sd: 99.73%
# (68.27 + 2 * 15.73)

size_outlr_mean = size.copy()
size_outlr_mean[((size - size.mean()).abs() > 3 * size.std())] = size.mean()
print(size_outlr_mean.mean())