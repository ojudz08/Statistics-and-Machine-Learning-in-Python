# create an empty dictionary (two ways)
empty_dict = {}
empty_dict = dict()

# create a dictionary (two ways)
family = {'dad':'homer', 'mom':'marge', 'size':6}
family = dict(dad='homer', mom='marge', size=6)

# convert a list of tuples into a dictionary
list_of_tuples = [('dad','homer'), ('mom','marge'), ('size', 6)]
family = dict(list_of_tuples)

# examine a dictionary
family['dad']               # returns 'homer'
len(family)                 # returns 3
family.keys()               # returns list: ['dad', 'mom', 'size']
family.values()             # returns list: ['homer', 'marge', 6]
family.items()              # returns list of tuples:

# [('dad', 'homer'), ('mom', 'marge'), ('size', 6)]
'mom' in family             # returns True
'marge' in family           # returns False (only checks keys)

# modify a dictionary (does not return the dictionary)
family['cat'] = 'snowball'                          # add a new entry
family['cat'] = 'snowball ii'                       # edit an existing entry
del family['cat']                                   # delete an entry
family['kids'] = ['bart', 'lisa']                   # value can be a list
family.pop('dad')                                   # removes an entry and returns the value ('homer')
family.update({'baby':'maggie', 'grandpa':'abe'})   # add multiple entries

# accessing values more safely with 'get'
family['mom']               # returns 'marge'
family.get('mom')           # same thing
try:
    family['grandma']       # throws an error
except KeyError as e:
    print("\nError", e)

family.get('grandma')                   # returns None
family.get('grandma', 'not found')      # returns 'not found' (the default)

# accessing a list element within a dictionary
family['kids'][0]               # returns 'bart'
family['kids'].remove('lisa')   # removes 'lisa'

# string substitution using a dictionary
'youngest child is %(baby)s' % family   # returns 'youngest child is maggie'