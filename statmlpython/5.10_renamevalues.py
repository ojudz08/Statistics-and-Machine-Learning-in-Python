# Run code 5.1_createdataframe

df = users.copy()
print(df.columns)
df.columns = ['age', 'genre', 'travail', 'nom', 'taille']

df.travail = df.travail.map({'student':'etudiant', 'manager':'manager',
                             'engineer':'ingenieur', 'scientist':'scientific'})

assert df.travail.isnull().sum() == 0
                        
df['travail'].str.contains("etu|inge")