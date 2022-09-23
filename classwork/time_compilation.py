import copy
from random import shuffle
from time import time

# create list

my_list = [i for i in range(1000000)]

copied_list = copy.deepcopy(my_list)

shuffle(copied_list)

time_start_1 = time()
odd_elements_1 = [i for i in my_list if i % 2]
print(time() - time_start_1)

time_start_2 = time()
odd_elements_2 = [i for i in my_list if i % 2]
print(time() - time_start_2)










