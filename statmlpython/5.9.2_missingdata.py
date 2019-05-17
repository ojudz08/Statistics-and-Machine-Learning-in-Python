# Missing data


# Missing values are often just excluded
df = users.copy()

df.describe(include='all')          # exclude missing values

# find missing values in a series
df.height.isnull()                  # True if NaN, False otherwise
df.height.notnull()                 # False if NaN, True otherwise
df[df.height.notnull()]             # only show rows where age is not NaN
df.height.isnull().sum()            # count the missing values, returns 2

# find missing values in a DataFrame
df.isnull()                         # DataFrame of booleans
df.isnull().sum()                   # calculate the sum of each column



# Strategy 1: drop missing values
df.dropna()                         # drop a row if ANY values are missing
df.dropna(how='all')                # drop a row only if ALL values are missing

# Strategy 2: fill in missing values
df.height.mean()
df = users.copy()
df.ix[df.height.isnull(), "height"] = df["height"].mean()

print(df)