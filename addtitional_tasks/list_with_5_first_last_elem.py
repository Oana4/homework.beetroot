# Write a Python program to generate and print a list of first and last 5 elements
# where the values are square of numbers between 1 and 30 (both included).

list_of_squared = [i**2 for i in range(1, 31)]
print(list_of_squared[:5]+list_of_squared[-5:])