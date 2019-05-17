print('\n')
print('first line\nsecond line')        # normal strings allow for escaped characters
print('\n')                             # included \n for me to see the output easily

print(r'frist line\nfirst line')        # raw strings treat backlashes as literal characters
print(r'frist line\nsecond line')
print('\n')

s = b'first line\nsecond line'          # sequence of bytes are not strings, should be decodded before some operations
print(s)
print('\n')

print(s.decode('utf-8').split())