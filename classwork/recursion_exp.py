# Let’s play with recursion.
# Make a function with argument index: int - call itself with index + 1.
# Create an if statement, before recursion call, like index < 10, to no get recursion exception

def recursion(my_index):
    if my_index >= 10:
        print(my_index)
        return 1

    return recursion(my_index + 1) + 1


print("result", recursion(3))
