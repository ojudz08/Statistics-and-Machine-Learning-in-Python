x = 3
# if statement
if x > 0:
    print('positive')
    
# if/else statement
if x > 0:
    print('positive')
else:
    print('zero or negative')
    
# if/elif/else statement
if x > 0:
    print('postive')
elif x == 0:
    print('zero')
else:
    print('negative')
    
# single-line if statement (sometimes discouraged)
if x > 0: print('positive')

# single-line if statement (sometimes discouraged)
# known as a 'ternary operator'
'positive' if x > 0 else 'zero or negative'