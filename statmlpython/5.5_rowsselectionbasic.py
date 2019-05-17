# Run code 5.1_createdataframe

# iloc is strictly integer position based
df = users.copy()           # copies data from users to df (new DataFrame)
df.iloc[0]                  # 1st row
df.iloc[0, 0]               # 1st item of 1st row
df.iloc[0, 0] = 55          # replaces the 1st item of 1st row with 55
       
for i in range(users.shape[0]):
    row = df.iloc[i]
    row.age *= 100          # setting a copy, and not the original frame data

print(df)                   # df is not modified

     

# ix supports mixed integer and label based access
df = users.copy()
df.ix[0]                    # 1st row
df.ix[0, "age"]             # 1st item of 1st row
df.ix[0, "age"] = 55        # 1st item of 1st row replaces with 55

for i in range(df.shape[0]):
    df.ix[i, "age"] *= 10

print(df)                   # df is modified