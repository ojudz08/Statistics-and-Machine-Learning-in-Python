# Dealing with outliers

size = pd.Series(np.random.normal(loc=175, size=20, scale=10))

# Corrupt the first 3 measures
size[:3] += 500