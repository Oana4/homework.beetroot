import random

num_generated = random.randint(1, 10)
my_guess = input('Type a number in range(1,10): ')

if int(my_guess) == num_generated:
    print('Correct! You must be a wizard!')
else:
    print(f"Maybe you'll be more lucky next time! \n The number was {num_generated} ")


