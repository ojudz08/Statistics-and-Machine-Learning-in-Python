# Run code 5.1_createdataframe


users['gender']             # select one column
type(users['gender'])       # series
users.gender                # select one column using the DataFrame

# select multiple columns
users[['age', 'gender']]    # select two columns
my_cols = ['age', 'gender'] # or, create a list...
users[my_cols]              # ...and use that list to select columns
type(users[my_cols])        # DataFrame