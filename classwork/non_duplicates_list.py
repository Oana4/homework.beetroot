# Create a function that takes on an input random ints (between 1 and 10) and returns the list,
# without duplicates. Try to create two versions of this function -
# first with usage set and list constructors and second only using for-in loops.

# 1st way
def list_of_randoms(*rand_int):
    return list(set(rand_int))


our_randoms = list_of_randoms(1, 2, 2, 5, 6)
print(our_randoms)


# 2nd way

def new_list_of_rands(*rand_ints):
    rands_set = set()
    for item in rand_ints:
        rands_set.add(item)
    return list(rands_set)


print(new_list_of_rands(1, 1, 2, 5, 8, 8))
