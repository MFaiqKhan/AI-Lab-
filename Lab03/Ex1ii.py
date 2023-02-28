# a Python program to find if a given string starts with a given character using Lambda.

# Define a string
string = "Python is a programming language."

# lambda function to check if the string starts with a given character
starts_with = lambda x: True if string.startswith(x) else False

# print the result
print("Does the string start with 'P'? ", starts_with('P'))
print("Does the string start with 'p'? ", starts_with('p'))