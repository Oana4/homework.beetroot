# Write a Python program that accepts a string and calculate the number of digits,
# letters and other characters in the input string

string = input("input string: ")

# all characters:
# summary = 0
#
# for char in string:
#     summary += 1
#
# print(summary)

# only for digits:

no_of_digits = 0

for char in string:
    if char.isdigit():
        no_of_digits += 1

print("Number of digits is: ", no_of_digits)