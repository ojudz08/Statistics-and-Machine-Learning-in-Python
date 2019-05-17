# for loop to create a list of cubes
nums = [1, 2, 3, 4, 5]
cubes = []
for num in nums:
    cubes.append(num**3)
# print(cubes)                  # prints the result, [1, 8, 27, 64, 125]

# equivalent list comprehension
cubes = [num**3 for num in nums]
# print(cubes)                  # prints the result, [1, 8, 27, 64, 125]



# for loop to create a list of cubes of even numbers
cubes_of_even = []
for num in nums:
    if num % 2 == 0:
        cubes_of_even.append(num**3)
# print(cubes_of_even)          # prints the result, [8, 64]

# equivalent list comprehension
# syntax: [expression for variable in iterable if condition]
cubes_of_even = [num**3 for num in nums if num % 2 == 0]
# print(cubes_of_even)          # prints the result, [8, 64]



# for loop to cube even numbers and square odd numbers
cubes_and_squares = []
for num in nums:
    if num % 2 == 0:
        cubes_and_squares.append(num**3)
    else:
        cubes_and_squares.append(num**2)
# print(cubes_and_squares)        # prints the result, [1, 8, 9, 64, 25]

# equivalent list comprehension (using ternary expression)
# syntax: [true_condition if condition else false_condition for variable in iterable]
cubes_and_squares = [num**3 if num % 2 == 0 else num**2 for num in nums]
# print(cubes_and_squares)        # prints the result, [1, 8, 9, 64, 25]



# for loop to flatten a 2d-matrix
matrix = [[1, 2], [3, 4]]
items = []
for row in matrix:
    for item in row:
        items.append(item)
# print(items)                  # prints the result, [1, 2, 3, 4]

# equivalent list comprehension
items = [item for row in matrix
              for item in row]
# print(items)                  # prints the result, [1, 2, 3, 4]



# set comprehension
fruits = ['apple', 'banana', 'cherry']
unique_lengths = {len(fruit) for fruit in fruits}
# print(unique_lengths)         # prints the result, {5, 6} apple length = 5, banana&cherry lenght = 6



# dictionary comprehension
fruit_lengths = {fruit:len(fruit) for fruit in fruits}
# print(fruit_lengths)          # prints the result {'apple': 5, 'banana': 6, 'cherry': 6}