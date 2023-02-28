## a Python program to square and cube every number in a given list of integers using Lambda

# Define a list of integers
integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map function is used to apply a function on all the elements of specified iterable and return map object.
# list then converts the map iterable into a list.
sq_integers = list(map(lambda x: x**2, integers)) # list of integers is passed to map function. 

cube_integers = list(map(lambda x: x**3, integers)) # list of integers is passed to map function.

print("The list of integers is: ", integers)
print("The list of squares of integers is: ", sq_integers)
print("The list of cubes of integers is: ", cube_integers)

# Output:
# The list of integers is:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# The list of squares of integers is:  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# The list of cubes of integers is:  [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]
