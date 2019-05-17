# Run code 5.1_createdataframe

df = users.copy()

df.age.sort_values()                                # sort out values in ascending order, only works for a series
df.sort_values(by = 'age')                          # sort rows of a specific column in ascending order
df.sort_values(by = 'age', ascending = False)       # use descending order
df.sort_values(by = ['job', 'age'])                 # sort by multiple columns, sort job column in ascending order, then sort age in ascending order
df.sort_values(by = ['job', 'age'], inplace = True) # modify df

print(df)