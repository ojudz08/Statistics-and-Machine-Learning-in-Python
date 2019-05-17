# Run code 5.1_createdataframe


# "Unpivots" a DataFrame from wide format to long (stacked) format
stacked = pd.melt(users, id_vars="name", var_name="variable", value_name="value")


# "pivots" a DataFrame from long (stacked) format to wide format
print(stacked.pivot(index='name', columns='variable', values='value'))