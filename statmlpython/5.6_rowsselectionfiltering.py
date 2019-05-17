# Run code 5.1_createdataframe

# simple logical filtering
users[users.age < 20]           # only show users with age < 20
young_bool = users.age < 20     # or, create a Series of booleans
young = users[young_bool]       # ...and use that Series to filter rows
users[users.age < 20].job        # select one column from the filtered results
print(young)

# advanced logical filtering
users[users.age < 20][['age', 'job']]               # select multiple columns
users[(users.age > 20) & (users.gender == 'M')]     # use multiple conditions
users[users.job.isin(['student', 'engineer'])]      # filter specific values