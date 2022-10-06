# Create a function that will take pronouns + name, and print something like “She is Cat”. From this function -
# create a partial function, which will have predefined argument “pronouns”.
# Assign this new function to variable “he/she/it_pronouns_function” and make it print a few names.

from functools import partial


def ProName(pronouns, name):
    print(f"{pronouns} is an {name}")


it_pronouns_function = partial(ProName, pronouns="it")
user_input = input("Can you please type the name: ")

it_pronouns_function(name=user_input)
