# Remove duplicate data


df = users.append(df.iloc[0], ignore_index=True)

print(df.duplicated())                  # Series of booleans
# (True if a row is identical to a previous row)
df.duplicated().sum()                   # count of duplicates
df[df.duplicated()]                     # only show duplicates
df.age.duplicated()                     # check a single column for duplicates
df.duplicated(['age', 'gender']).sum()  # specify columns for finding duplicates
df = df.drop_duplicates()