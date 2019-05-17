# make sure to run previous codes


# Summarize all numeric columns
print(df.describe())


# Summarize all columns
print(df.describe(include='all'))
print(df.describe(include=['object']))      # limit to one or more types


# statistics per group (groupby)
print(df.groupby("job").mean())
print(df.groupby("job")["age"].mean())
print(df.groupby("job").describe(include='all'))


# Groupby in a loop
for grp, data in df.groupby("job"):
    print(grp, data)