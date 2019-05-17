# create a string
s = str(42)                         # convert another data type into a string
s = 'I like you'

# examine a string
s[0]                                # returns 'I'
len(s)                              # returns 10

# string slicing like lists
s[:6]                               # returns 'I like'
s[7:]                               # returns 'you'
s[-1]                               # returns 'u'

# basic string methods (does not modify the original string)
s.lower()                           # returns 'i like you'
s.upper()                           # returns 'I LIKE YOU'
s.startswith('I')                   # returns True
s.endswith('you')                   # returns True
s.isdigit()                         # returns False (returns True if every character in the string is a digit)
s.find('like')                      # returns index of first occurrence (2), but doesn't support regex
s.find('hate')                      # returns -1 since not found
s.replace('like','love')            # replaces all instances of 'like' with 'love'

# split a string into a list of substrings separated by a delimiter
s.split(' ')                        # returns ['I','like','you']
s.split()                           # same thing
s2 = 'a, an, the'
s2.split(',')                       # returns ['a',' an',' the']

# join a list of strings into one string using a delimiter
stooges = ['larry','curly','moe']
' '.join(stooges)                   # returns 'larry curly moe'

# concatenate strings
s3 = 'The meaning of life is'
s4 = '42'
s3 + ' ' + s4                       # returns 'The meaning of life is 42'
s3 + ' ' + str(42)                  # same thing

# remove whitespace from start and end of a string
s5 = ' ham and cheese '
s5.strip()                          # returns 'ham and cheese'

# string substitutions: all of these return 'raining cats and dogs'
'raining %s and %s' % ('cats','dogs')                           # old way
'raining {} and {}'.format('cats','dogs')                       # new way
'raining {arg1} and {arg2}'.format(arg1='cats',arg2='dogs')     # named arguments

# string formatting
# more examples: http://mkaz.com/2012/10/10/python-string-format/
'pi is {:.2f}'.format(3.14159)      # returns 'pi is 3.14'