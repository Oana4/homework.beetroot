import random

first_list = random.sample(range(1, 11), 10)
second_list = random.sample(range(1, 11), 10)

# simple way
# first_set = set(first_list)
# second_set = set(second_list)
# common_set = first_set.intersection(second_set)
#
# print(list(common_set))

# harder way

i = 0
common_list = []

while i < len(first_list):
    if first_list[i] in second_list:
        common_list.append(first_list[i])
    i += 1

print(list(set(common_list)))
