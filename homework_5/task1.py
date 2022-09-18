import random

# without while loop
# random_list = random.sample(range(1, 50), 10)
#
# print(random_list)
# print(max(random_list))

# with while loop
i, length_of_list = 1, 10
new_random_list = []

while i <= length_of_list:
    new_random_list.append(random.randint(0, 50))
    i += 1

print(new_random_list)       # print new random list (with while loop)
print(max(new_random_list))  # print max value in list
