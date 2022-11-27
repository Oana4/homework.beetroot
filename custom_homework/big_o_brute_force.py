from random import choices
from string import digits
from time import time
from itertools import product


# simple measuring time decorator
def timer_func(func):
    def wrap_func(*args):
        t1 = time()
        result = func(*args)
        t2 = time()
        print(f'Function {func.__name__} executed in {(t2 - t1)}s')
        return result
    return wrap_func


# really simplified version of our password generator
@timer_func
def password_generator():
    length = 6

    final_alphabet = digits

    password = ''.join(choices(final_alphabet, k=length))
    return password


new_password = password_generator()
print("Your new generated password is:\n", new_password)
new_password_tuple = tuple(new_password)
print(new_password_tuple)       # I'm creating a tuple of digits to be able to compare with itertools product outcome


# our brute force function to crack the password
@timer_func
def brute_force():
    guessed_password = ['0'] * len(new_password)

    # here I use the cartesian dot product of digits string which is an iterable, as an alternative of N-dimensional
    # nested for-loops (it has the same complexity, but it allows me to select the number of repetitions of for loops,
    # so it's more elegant). Let's not forget that our big O here will be O(n^len(new_password)) <=> really baaad
    possible_passwords = list(product(digits, repeat=len(new_password)))
    for possible_pass in possible_passwords:
        if possible_pass == new_password_tuple:
            guessed_password = possible_pass
            print(f"You have been hacked! Our guess was {guessed_password}")

    return guessed_password


brute_force()

# Here are my statistical results:

# So for the len(new_password) == 5:
# Function password_generator executed in 1.1682510375976562e-05s
# Function brute_force executed in 0.01829671859741211s
# So you can see that it's 3 orders of magnitude worse!

# For len(new_password) == 6 I obtained the following results:
# Function password_generator executed in 8.821487426757812e-06s
# Function brute_force executed in 0.13010501861572266s
# So you can see that it's almost 5 orders of magnitude worse!

