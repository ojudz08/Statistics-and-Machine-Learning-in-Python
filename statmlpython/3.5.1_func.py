# define a function with no arguments and no return values
def print_text():
    print('this is text')

print_text()            # call the function


# define a function with one argument and no return values
def print_this(x):
    print(x)

print_this(3)           # call the function, prints 3
n = print_this(3)       # call the function, prints 3 but doesn't assign 3 to n
                        # because the function has no return statement
# print(n)              # prints None, confirms that 3 was not assigned to n


# define a function with one argument and one return value
def square_this1(x):
    return x ** 2

# include an optional docstring to desribe the effect of a function
def square_this(x):
    """Return the square of a number."""
    return x ** 2

square_this(3)          # call the function, to print 9 enclose the statement in print
var = square_this(3)    # call the function, assigns 9 to var, but does not print 9


# default arguments
def power_this(x, power=2):
    return x ** power

power_this(2)           # enclose in print, to print 4
power_this(2, 3)        # enclose in print, to print 8


# use 'pass' as a placeholder if you haven't written the function body
def stub():
    pass


# return two values from a single function
def min_max(nums):
    return min(nums), max(nums)
    
nums = [1, 2, 3]                # return values can be assigned to a single variable as a tuple
min_max_num = min_max(nums)     # min_max_num = (1, 3)
# print(min_max_num)            # print to return values of min_max_num

min_num, max_num = min_max(nums) # return values can be assigned into multiple variables using tuple unpacking
# print(min_num, max_num)        # min_num = 1, max num = 3