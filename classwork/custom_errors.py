# ou have a list [1, 2, 3, 4, 5, 6, 7, 0]. Write a function "try_to_return_a_number", which will take
# an argument "number" and raise an exception OddError if number is odd, and ZeroError if number is zero.
# Write a high level function, which will take an argument "list_of_numbers", go through it in for in loop,
# put every item from list to "try_to_return_a_number" function, and print a number
# or a message depends on exception on each loop step.

numbers_list = [1, 2, 3, 4, 5, 6, 7, 0]


class Error(Exception):
    pass


class ZeroError(Error):
    pass


class OddError(Error):
    pass


def try_to_return_a_number(number):
    if number == 0:
        raise ZeroError
    if number % 2:
        raise OddError


def high_level_function(list_of_numbers):
    for number in list_of_numbers:
        try:
            try_to_return_a_number(number)
        except ZeroError:
            print("Your number is 0! Can't be right")
        except OddError:
            print("Your number is odd!")
        else:
            print(number)


print(high_level_function(numbers_list))

