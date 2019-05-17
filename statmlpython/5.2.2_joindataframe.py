# Run code 5.1_createdataframe

user4 = pd.DataFrame(dict(name=['alice', 'john', 'eric', 'julie'],
                          height=[165, 180, 175, 171]))
print(user4)

# Use intersection of keys from both frames
merge_inter = pd.merge(users, user4, on="name")
print(merge_inter)

# Use union of keys from both frames
users = pd.merge(users, user4, on="name", how="outer")
print(users)