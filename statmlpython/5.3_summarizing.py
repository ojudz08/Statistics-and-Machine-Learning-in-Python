# Run code 5.1_createdataframe


# examine the users data

users
type(users)             # DataFrame
users.head()            # print the first 5 rows (default), indicate inside () 
users.tail()            # print the last 5 rows (defualt)


users.index             # "the index" (aka "the labels")
users.columns           # column names (which is "an index")
users.dtypes            # data types of each column
users.shape             # number of rows and columns
users.values            # underlying numpy array
users.info()            # concise summary (includes memory usage)